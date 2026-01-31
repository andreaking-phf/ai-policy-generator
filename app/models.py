"""
Database models for AI Policy Generator
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PrioritizationSession(db.Model):
    """Stores prioritization sessions"""
    __tablename__ = 'prioritization_sessions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    method = db.Column(db.String(50), nullable=False)  # weighted, ranking, pairwise, budget
    rankings_json = db.Column(db.Text, nullable=False)  # JSON string of rankings
    raw_data_json = db.Column(db.Text)  # JSON string of raw input data
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to policies
    policies = db.relationship('GeneratedPolicy', backref='prioritization', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'method': self.method,
            'rankings_json': self.rankings_json,
            'raw_data_json': self.raw_data_json,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class GeneratedPolicy(db.Model):
    """Stores generated policy documents"""
    __tablename__ = 'generated_policies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    org_name = db.Column(db.String(255), nullable=False)
    jurisdiction_type = db.Column(db.String(50), nullable=False)
    org_size = db.Column(db.String(50), nullable=False)
    intensity = db.Column(db.String(50), nullable=False)  # basic, standard, comprehensive
    additional_context = db.Column(db.Text)
    policy_html = db.Column(db.Text, nullable=False)  # Generated HTML content
    policy_markdown = db.Column(db.Text)  # Generated Markdown content
    config_json = db.Column(db.Text)  # Full config as JSON
    prioritization_id = db.Column(db.Integer, db.ForeignKey('prioritization_sessions.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'org_name': self.org_name,
            'jurisdiction_type': self.jurisdiction_type,
            'org_size': self.org_size,
            'intensity': self.intensity,
            'additional_context': self.additional_context,
            'policy_html': self.policy_html,
            'policy_markdown': self.policy_markdown,
            'config_json': self.config_json,
            'prioritization_id': self.prioritization_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class PolicyElement(db.Model):
    """Reference table for policy elements"""
    __tablename__ = 'policy_elements'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    tier = db.Column(db.Integer, nullable=False)  # 1-4 (1 being most common)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tier': self.tier
        }


def init_policy_elements(db):
    """Initialize default policy elements if not present"""
    elements = [
        {"id": 1, "name": "Data Privacy & Security", "description": "Protection of PHI/PII, secure data handling, HIPAA compliance", "tier": 1},
        {"id": 2, "name": "Bias, Equity & Discrimination", "description": "Fairness assessments, addressing disparities, equity impact", "tier": 1},
        {"id": 3, "name": "Transparency & Explainability", "description": "Disclosure requirements, model documentation, public reporting", "tier": 1},
        {"id": 4, "name": "Human Oversight & Accountability", "description": "Human-in-the-loop, professional judgment, clear responsibility", "tier": 1},
        {"id": 5, "name": "Accuracy & Validation", "description": "Performance testing, monitoring, quality assurance", "tier": 2},
        {"id": 6, "name": "Governance & Risk Management", "description": "Oversight committees, risk frameworks, approval processes", "tier": 2},
        {"id": 7, "name": "Training & Capacity Building", "description": "AI literacy, staff development, skills assessment", "tier": 2},
        {"id": 8, "name": "Use Case Appropriateness", "description": "Permitted vs. prohibited uses, boundaries, guardrails", "tier": 3},
        {"id": 9, "name": "Procurement & Vendor Management", "description": "Vendor selection, contracts, third-party risk assessment", "tier": 3},
        {"id": 10, "name": "Legal & Regulatory Compliance", "description": "Federal/state law compliance, civil rights protections", "tier": 3},
        {"id": 11, "name": "Community Engagement", "description": "Stakeholder consultation, public input, building trust", "tier": 4},
        {"id": 12, "name": "Sustainability & Evaluation", "description": "Long-term viability, cost-benefit, continuous improvement", "tier": 4}
    ]

    for element in elements:
        existing = PolicyElement.query.filter_by(id=element['id']).first()
        if not existing:
            new_element = PolicyElement(**element)
            db.session.add(new_element)

    db.session.commit()
