"""
AI Policy Generator - Flask Application
A fully functional app for health departments to create AI use policies
"""
import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file
from models import db, PrioritizationSession, GeneratedPolicy, PolicyElement, init_policy_elements
from policy_templates import POLICY_TEMPLATES, get_template

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///policy_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

with app.app_context():
    db.create_all()
    init_policy_elements(db)


# =============================================================================
# Page Routes
# =============================================================================

@app.route('/')
def dashboard():
    """Main dashboard showing overview and recent activity"""
    recent_prioritizations = PrioritizationSession.query.order_by(
        PrioritizationSession.created_at.desc()
    ).limit(5).all()
    recent_policies = GeneratedPolicy.query.order_by(
        GeneratedPolicy.created_at.desc()
    ).limit(5).all()

    stats = {
        'total_prioritizations': PrioritizationSession.query.count(),
        'total_policies': GeneratedPolicy.query.count()
    }

    return render_template('dashboard.html',
                         recent_prioritizations=recent_prioritizations,
                         recent_policies=recent_policies,
                         stats=stats)


@app.route('/prioritize')
def prioritize():
    """Prioritization tool page"""
    elements = PolicyElement.query.order_by(PolicyElement.id).all()
    return render_template('prioritize.html', elements=elements)


@app.route('/generate')
def generate():
    """Policy generator page"""
    prioritizations = PrioritizationSession.query.order_by(
        PrioritizationSession.created_at.desc()
    ).all()
    return render_template('generate.html', prioritizations=prioritizations)


@app.route('/history')
def history():
    """History of all sessions and policies"""
    prioritizations = PrioritizationSession.query.order_by(
        PrioritizationSession.created_at.desc()
    ).all()
    policies = GeneratedPolicy.query.order_by(
        GeneratedPolicy.created_at.desc()
    ).all()
    return render_template('history.html',
                         prioritizations=prioritizations,
                         policies=policies)


@app.route('/policy/<int:policy_id>')
def view_policy(policy_id):
    """View a specific generated policy"""
    policy = GeneratedPolicy.query.get_or_404(policy_id)
    return render_template('view_policy.html', policy=policy)


# =============================================================================
# API Routes - Prioritization
# =============================================================================

@app.route('/api/elements', methods=['GET'])
def get_elements():
    """Get all policy elements"""
    elements = PolicyElement.query.order_by(PolicyElement.id).all()
    return jsonify([e.to_dict() for e in elements])


@app.route('/api/prioritizations', methods=['GET'])
def get_prioritizations():
    """Get all prioritization sessions"""
    sessions = PrioritizationSession.query.order_by(
        PrioritizationSession.created_at.desc()
    ).all()
    return jsonify([s.to_dict() for s in sessions])


@app.route('/api/prioritizations', methods=['POST'])
def create_prioritization():
    """Save a new prioritization session"""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    session = PrioritizationSession(
        name=data.get('name', f"Session {datetime.now().strftime('%Y-%m-%d %H:%M')}"),
        method=data.get('method', 'weighted'),
        rankings_json=json.dumps(data.get('rankings', [])),
        raw_data_json=json.dumps(data.get('rawData', {}))
    )

    db.session.add(session)
    db.session.commit()

    return jsonify(session.to_dict()), 201


@app.route('/api/prioritizations/<int:session_id>', methods=['GET'])
def get_prioritization(session_id):
    """Get a specific prioritization session"""
    session = PrioritizationSession.query.get_or_404(session_id)
    result = session.to_dict()
    result['rankings'] = json.loads(session.rankings_json)
    result['rawData'] = json.loads(session.raw_data_json) if session.raw_data_json else {}
    return jsonify(result)


@app.route('/api/prioritizations/<int:session_id>', methods=['DELETE'])
def delete_prioritization(session_id):
    """Delete a prioritization session"""
    session = PrioritizationSession.query.get_or_404(session_id)
    db.session.delete(session)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'}), 200


# =============================================================================
# API Routes - Policy Generation
# =============================================================================

@app.route('/api/policies', methods=['GET'])
def get_policies():
    """Get all generated policies"""
    policies = GeneratedPolicy.query.order_by(
        GeneratedPolicy.created_at.desc()
    ).all()
    return jsonify([p.to_dict() for p in policies])


@app.route('/api/policies', methods=['POST'])
def create_policy():
    """Generate and save a new policy"""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Required fields
    org_name = data.get('orgName')
    if not org_name:
        return jsonify({'error': 'Organization name is required'}), 400

    rankings = data.get('rankings', [])
    if not rankings:
        return jsonify({'error': 'Rankings are required'}), 400

    # Build policy document
    config = {
        'orgName': org_name,
        'jurisdictionType': data.get('jurisdictionType', 'local'),
        'orgSize': data.get('orgSize', 'medium'),
        'intensity': data.get('intensity', 'standard'),
        'additionalContext': data.get('additionalContext', ''),
        'date': datetime.now().strftime('%B %d, %Y'),
        'rankings': rankings
    }

    policy_html = build_policy_html(config)
    policy_markdown = build_policy_markdown(config)

    policy = GeneratedPolicy(
        name=data.get('name', f"Policy for {org_name}"),
        org_name=org_name,
        jurisdiction_type=config['jurisdictionType'],
        org_size=config['orgSize'],
        intensity=config['intensity'],
        additional_context=config['additionalContext'],
        policy_html=policy_html,
        policy_markdown=policy_markdown,
        config_json=json.dumps(config),
        prioritization_id=data.get('prioritizationId')
    )

    db.session.add(policy)
    db.session.commit()

    result = policy.to_dict()
    result['policy_html'] = policy_html
    result['policy_markdown'] = policy_markdown

    return jsonify(result), 201


@app.route('/api/policies/<int:policy_id>', methods=['GET'])
def get_policy(policy_id):
    """Get a specific policy"""
    policy = GeneratedPolicy.query.get_or_404(policy_id)
    return jsonify(policy.to_dict())


@app.route('/api/policies/<int:policy_id>', methods=['DELETE'])
def delete_policy(policy_id):
    """Delete a policy"""
    policy = GeneratedPolicy.query.get_or_404(policy_id)
    db.session.delete(policy)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'}), 200


@app.route('/api/generate-preview', methods=['POST'])
def generate_preview():
    """Generate policy preview without saving"""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    config = {
        'orgName': data.get('orgName', 'Organization Name'),
        'jurisdictionType': data.get('jurisdictionType', 'local'),
        'orgSize': data.get('orgSize', 'medium'),
        'intensity': data.get('intensity', 'standard'),
        'additionalContext': data.get('additionalContext', ''),
        'date': datetime.now().strftime('%B %d, %Y'),
        'rankings': data.get('rankings', [])
    }

    policy_html = build_policy_html(config)
    policy_markdown = build_policy_markdown(config)

    return jsonify({
        'html': policy_html,
        'markdown': policy_markdown
    })


# =============================================================================
# Helper Functions
# =============================================================================

def build_policy_html(config):
    """Build HTML policy document from config"""
    org_name = config['orgName']
    date = config['date']
    intensity = config['intensity']
    jurisdiction = config['jurisdictionType']
    rankings = config['rankings']

    html = f"""
<h1>Artificial Intelligence Use Policy</h1>
<p><strong>{org_name}</strong></p>
<p><em>Effective Date: {date}</em></p>
<p><em>Policy Version: 1.0</em></p>

<hr>

<h2>I. Purpose and Scope</h2>
<div class="policy-section">
    <p><strong>Purpose:</strong> This policy establishes a framework for the responsible development, procurement, and use of artificial intelligence (AI) technologies at {org_name}. It ensures AI systems align with our mission to protect and promote public health while upholding the highest standards of ethics, equity, privacy, and transparency.</p>

    <p><strong>Scope:</strong> This policy applies to all staff, contractors, and vendors involved in the use, development, or procurement of AI technologies on behalf of {org_name}. It covers all AI systems including but not limited to:</p>
    <ul>
        <li>Generative AI tools (e.g., ChatGPT, Claude, Gemini)</li>
        <li>Machine learning models for data analysis and prediction</li>
        <li>Natural language processing systems</li>
        <li>Computer vision and image analysis tools</li>
        <li>Decision support and automation systems</li>
    </ul>
</div>

<h2>II. Core Principles</h2>
<div class="policy-section">
    <p>{org_name} commits to the following principles in all AI activities:</p>
    <ul>
        <li><strong>Public Health First:</strong> AI serves public health goals and community well-being</li>
        <li><strong>Equity and Justice:</strong> AI promotes health equity and does not perpetuate discrimination</li>
        <li><strong>Transparency:</strong> AI use is open, explainable, and accountable</li>
        <li><strong>Privacy Protection:</strong> AI systems safeguard sensitive health information</li>
        <li><strong>Human Oversight:</strong> Human judgment remains central to all decisions</li>
        <li><strong>Continuous Learning:</strong> AI practices evolve with technology and evidence</li>
    </ul>
</div>

<hr>

<h2>III. Policy Requirements</h2>
<p><em>Requirements are prioritized based on organizational assessment and adapted for {jurisdiction} context.</em></p>
"""

    # Split rankings into priority tiers
    top_priorities = rankings[:4] if len(rankings) >= 4 else rankings
    medium_priorities = rankings[4:8] if len(rankings) >= 8 else rankings[4:]
    lower_priorities = rankings[8:] if len(rankings) > 8 else []

    # High priority sections
    html += '<h3 class="priority-high">High Priority Requirements</h3>'
    for i, item in enumerate(top_priorities):
        template = get_template(item['name'], 'high' if intensity == 'comprehensive' else 'medium' if intensity == 'standard' else 'low')
        if template:
            html += f"""
<div class="policy-section">
    <h3>{chr(65 + i)}. {template['title']}</h3>
    {markdown_to_html(template['content'])}
</div>
"""

    # Standard priority sections
    if medium_priorities:
        html += '<h3 class="priority-medium">Standard Requirements</h3>'
        for i, item in enumerate(medium_priorities):
            template = get_template(item['name'], 'medium' if intensity == 'comprehensive' else 'low')
            if template:
                html += f"""
<div class="policy-section">
    <h3>{chr(65 + len(top_priorities) + i)}. {template['title']}</h3>
    {markdown_to_html(template['content'])}
</div>
"""

    # Additional considerations (comprehensive only)
    if intensity == 'comprehensive' and lower_priorities:
        html += '<h3 class="priority-low">Additional Considerations</h3>'
        for i, item in enumerate(lower_priorities):
            template = get_template(item['name'], 'low')
            if template:
                html += f"""
<div class="policy-section">
    <h3>{chr(65 + len(top_priorities) + len(medium_priorities) + i)}. {template['title']}</h3>
    {markdown_to_html(template['content'])}
</div>
"""

    # Governance section
    html += """
<hr>

<h2>IV. Governance and Implementation</h2>
<div class="policy-section">
    <h3>A. Roles and Responsibilities</h3>
    <ul>
        <li><strong>AI Governance Committee:</strong> Oversees AI policy implementation and approves high-risk AI use cases</li>
        <li><strong>Privacy Officer:</strong> Reviews AI systems for data privacy compliance</li>
        <li><strong>Equity Officer:</strong> Assesses AI systems for bias and equity impacts</li>
        <li><strong>IT Security:</strong> Ensures AI systems meet cybersecurity requirements</li>
        <li><strong>Department Heads:</strong> Accountable for AI use within their units</li>
        <li><strong>All Staff:</strong> Required to comply with this policy</li>
    </ul>

    <h3>B. Policy Review and Updates</h3>
    <p>This policy will be reviewed annually and updated as needed to reflect:</p>
    <ul>
        <li>Changes in AI technology and capabilities</li>
        <li>New legal or regulatory requirements</li>
        <li>Lessons learned from AI implementation</li>
        <li>Stakeholder feedback and concerns</li>
    </ul>

    <h3>C. Compliance and Enforcement</h3>
    <p>Violations of this policy may result in:</p>
    <ul>
        <li>Revocation of AI system access</li>
        <li>Mandatory retraining</li>
        <li>Disciplinary action up to and including termination</li>
        <li>Legal action where applicable</li>
    </ul>
</div>
"""

    html += f"""
<h2>V. Contact Information</h2>
<div class="policy-section">
    <p>Questions about this policy should be directed to:</p>
    <p><strong>AI Policy Coordinator</strong><br>
    {org_name}<br>
    [Contact information to be added]</p>
</div>

<hr>

<p class="footer-note">
    <em>This policy was generated using the AI Policy Priority Builder tool<br>
    Based on evidence-based research from Kansas Health Institute, CDC, and other authoritative sources<br>
    Document should be reviewed by legal counsel and adapted to local requirements</em>
</p>
"""

    return html


def build_policy_markdown(config):
    """Build Markdown policy document from config"""
    org_name = config['orgName']
    date = config['date']
    intensity = config['intensity']
    jurisdiction = config['jurisdictionType']
    rankings = config['rankings']

    md = f"""# Artificial Intelligence Use Policy

**{org_name}**

*Effective Date: {date}*

*Policy Version: 1.0*

---

## I. Purpose and Scope

**Purpose:** This policy establishes a framework for the responsible development, procurement, and use of artificial intelligence (AI) technologies at {org_name}. It ensures AI systems align with our mission to protect and promote public health while upholding the highest standards of ethics, equity, privacy, and transparency.

**Scope:** This policy applies to all staff, contractors, and vendors involved in the use, development, or procurement of AI technologies on behalf of {org_name}. It covers all AI systems including but not limited to:

- Generative AI tools (e.g., ChatGPT, Claude, Gemini)
- Machine learning models for data analysis and prediction
- Natural language processing systems
- Computer vision and image analysis tools
- Decision support and automation systems

## II. Core Principles

{org_name} commits to the following principles in all AI activities:

- **Public Health First:** AI serves public health goals and community well-being
- **Equity and Justice:** AI promotes health equity and does not perpetuate discrimination
- **Transparency:** AI use is open, explainable, and accountable
- **Privacy Protection:** AI systems safeguard sensitive health information
- **Human Oversight:** Human judgment remains central to all decisions
- **Continuous Learning:** AI practices evolve with technology and evidence

---

## III. Policy Requirements

*Requirements are prioritized based on organizational assessment and adapted for {jurisdiction} context.*

"""

    # Split rankings into priority tiers
    top_priorities = rankings[:4] if len(rankings) >= 4 else rankings
    medium_priorities = rankings[4:8] if len(rankings) >= 8 else rankings[4:]
    lower_priorities = rankings[8:] if len(rankings) > 8 else []

    # High priority sections
    md += "### High Priority Requirements\n\n"
    for i, item in enumerate(top_priorities):
        template = get_template(item['name'], 'high' if intensity == 'comprehensive' else 'medium' if intensity == 'standard' else 'low')
        if template:
            md += f"#### {chr(65 + i)}. {template['title']}\n\n{template['content']}\n\n"

    # Standard priority sections
    if medium_priorities:
        md += "### Standard Requirements\n\n"
        for i, item in enumerate(medium_priorities):
            template = get_template(item['name'], 'medium' if intensity == 'comprehensive' else 'low')
            if template:
                md += f"#### {chr(65 + len(top_priorities) + i)}. {template['title']}\n\n{template['content']}\n\n"

    # Additional considerations
    if intensity == 'comprehensive' and lower_priorities:
        md += "### Additional Considerations\n\n"
        for i, item in enumerate(lower_priorities):
            template = get_template(item['name'], 'low')
            if template:
                md += f"#### {chr(65 + len(top_priorities) + len(medium_priorities) + i)}. {template['title']}\n\n{template['content']}\n\n"

    md += f"""---

## IV. Governance and Implementation

### A. Roles and Responsibilities

- **AI Governance Committee:** Oversees AI policy implementation and approves high-risk AI use cases
- **Privacy Officer:** Reviews AI systems for data privacy compliance
- **Equity Officer:** Assesses AI systems for bias and equity impacts
- **IT Security:** Ensures AI systems meet cybersecurity requirements
- **Department Heads:** Accountable for AI use within their units
- **All Staff:** Required to comply with this policy

### B. Policy Review and Updates

This policy will be reviewed annually and updated as needed to reflect:

- Changes in AI technology and capabilities
- New legal or regulatory requirements
- Lessons learned from AI implementation
- Stakeholder feedback and concerns

### C. Compliance and Enforcement

Violations of this policy may result in:

- Revocation of AI system access
- Mandatory retraining
- Disciplinary action up to and including termination
- Legal action where applicable

## V. Contact Information

Questions about this policy should be directed to:

**AI Policy Coordinator**
{org_name}
[Contact information to be added]

---

*This policy was generated using the AI Policy Priority Builder tool*
*Based on evidence-based research from Kansas Health Institute, CDC, and other authoritative sources*
*Document should be reviewed by legal counsel and adapted to local requirements*
"""

    return md


def markdown_to_html(md_content):
    """Simple markdown to HTML converter"""
    html = md_content

    # Headers
    html = html.replace('### ', '<h4>').replace('\n\n<h4>', '</h4>\n\n<h4>')
    html = html.replace('## ', '<h3>').replace('\n\n<h3>', '</h3>\n\n<h3>')

    # Lists
    lines = html.split('\n')
    result = []
    in_list = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('- '):
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append(f'<li>{stripped[2:]}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            if stripped:
                if not stripped.startswith('<'):
                    result.append(f'<p>{stripped}</p>')
                else:
                    result.append(stripped)

    if in_list:
        result.append('</ul>')

    html = '\n'.join(result)

    # Bold
    import re
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    return html


# =============================================================================
# Main Entry Point
# =============================================================================

if __name__ == '__main__':
    app.run(debug=True, port=5000)
