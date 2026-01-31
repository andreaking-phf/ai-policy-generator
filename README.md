# AI Policy Decision Tree System for Health Departments
## Complete Implementation Guide

**Version 1.0** | **Last Updated: January 2026**

---

## Overview

This system provides state and local health departments with evidence-based tools to develop customized AI use policies. The system consists of:

1. **Interactive Prioritization Tool** - Helps users rank 12 policy elements
2. **Policy Document Generator** - Creates customized policy documents based on priorities
3. **Evidence Base** - Built on research from 50+ state/federal/municipal policies

---

## Table of Contents

- [Quick Start](#quick-start)
- [System Components](#system-components)
- [Research Foundation](#research-foundation)
- [Usage Guide](#usage-guide)
- [File Formats](#file-formats)
- [Customization](#customization)
- [Technical Requirements](#technical-requirements)
- [Troubleshooting](#troubleshooting)

---

## Quick Start

### For Users (No Technical Skills Required)

1. **Open `ai-policy-prioritization.html` in your web browser**
   - Works on Chrome, Firefox, Safari, Edge
   - No installation required
   - Works offline after initial load

2. **Choose your prioritization method:**
   - **Weighted Scoring** - Rate each element 1-10
   - **Drag & Rank** - Order from most to least important
   - **Pairwise Comparison** - Choose between pairs (most rigorous)
   - **Budget Allocation** - Distribute 100 points (forces trade-offs)

3. **Complete the prioritization**
   - Follow on-screen instructions
   - Download your rankings as JSON

4. **Open `ai-policy-generator.html` in your browser**
   - Upload your rankings JSON file
   - Fill in your organization details
   - Generate your customized policy document
   - Download in multiple formats

### For Advanced Users

Use the Python script for programmatic DOCX generation:

```bash
# Install dependencies
pip install python-docx --break-system-packages

# Generate policy document
python generate_docx.py config.json output.docx
```

---

## System Components

### 1. Prioritization Tool (`ai-policy-prioritization.html`)

**Purpose:** Interactive web application for ranking policy priorities

**Features:**
- 4 different prioritization methods
- Prevents "everything is critical" problem
- Saves rankings to browser localStorage
- Exports rankings as JSON
- Mobile-responsive design

**Outputs:**
- JSON file with rankings
- Timestamp and method used
- Raw scoring data

**Technical Details:**
- Single HTML file with embedded CSS/JavaScript
- No external dependencies
- Works completely offline
- Uses localStorage API for persistence

---

### 2. Policy Generator (`ai-policy-generator.html`)

**Purpose:** Generate customized policy documents from priorities

**Features:**
- Import rankings from prioritization tool
- Configure organization details
- Three intensity levels (Basic, Standard, Comprehensive)
- Live preview of generated policy
- Multiple export formats

**Outputs:**
- Markdown (.md)
- PDF (via print)
- DOCX (via Python script)
- Plain text (copy/paste)

**Configuration Options:**
- Organization name
- Jurisdiction type (state, local, county, city, tribal)
- Organization size (small, medium, large)
- Policy intensity level
- Additional context

---

### 3. DOCX Generator (`generate_docx.py`)

**Purpose:** Generate professional Word documents from policy configuration

**Features:**
- Custom styles matching design system
- Proper document structure
- Table of contents
- Professional formatting

**Requirements:**
- Python 3.6+
- python-docx library

**Usage:**
```bash
python generate_docx.py [input_config.json] [output_file.docx]
```

**Config JSON Format:**
```json
{
  "orgName": "Your Department Name",
  "jurisdictionType": "local",
  "orgSize": "medium",
  "intensity": "standard",
  "date": "January 28, 2026",
  "rankings": [
    {"name": "Data Privacy & Security", "score": 10, "tier": 1},
    {"name": "Bias, Equity & Discrimination", "score": 9, "tier": 1}
  ]
}
```

---

## Research Foundation

This system is built on comprehensive analysis of AI policies from:

### Federal Sources
- **CDC AI Vision & Strategy** (2023-2025)
- **HHS AI Strategy & Guidance** (2024)
- **OMB M-24-10** - Federal AI Governance (2024)
- **NIST AI Risk Management Framework** (2024)
- **HTI-1 Final Rule** - Health IT Certification (2024)

### State Legislation
- **Colorado SB-205** - Consumer Protection in AI (2024)
- **California** - Multiple AI bills (2023-2024)
- **Utah** - AI Learning Laboratory (2024)
- **Maryland** - AI Governance Act (2024)
- 40+ states with AI legislation introduced (2024)

### Municipal Policies
- **New York City AI Action Plan** (2023)
- **Baltimore Executive Order on AI** (2024)
- **Boston Interim Guidelines** (2023)
- **Seattle AI Policy** (2023-2024)

### Public Health-Specific
- **Kansas Health Institute AI Policy Template** (2025) - PRIMARY SOURCE
- CDC AI Community of Practice guidance
- NACCHO Public Health Informatics Profile (2024)
- ASTHO state AI legislation mapping

### Expert Review
Template development included review by:
- 14 expert reviewers
- Public health institutions
- National public health associations
- Academia
- City government
- AI developers

---

## The 12 Policy Elements

Based on analysis of 50+ policies, these elements appear consistently:

### Tier 1 (Universal - in 90%+ of policies)
1. **Data Privacy & Security**
   - PHI/PII protection
   - HIPAA compliance
   - Encryption requirements
   - Secure data handling

2. **Bias, Equity & Algorithmic Discrimination**
   - Fairness assessments
   - Health equity promotion
   - Disparate impact analysis
   - Accessibility requirements

3. **Transparency & Explainability**
   - Disclosure requirements
   - Model documentation
   - Public reporting
   - User notification

4. **Human Oversight & Accountability**
   - Human-in-the-loop requirements
   - Professional judgment
   - Clear responsibility
   - Appeal processes

### Tier 2 (Very Common - in 60-90% of policies)
5. **Accuracy, Reliability & Validation**
   - Performance testing
   - Ongoing monitoring
   - Quality assurance
   - Error rate standards

6. **Governance & Risk Management**
   - Oversight committees
   - Risk frameworks
   - Approval processes
   - Chief AI Officer

7. **Training & Capacity Building**
   - AI literacy programs
   - Staff development
   - Skills assessment
   - Change management

### Tier 3 (Common - in 40-60% of policies)
8. **Use Case Appropriateness**
   - Permitted vs. prohibited uses
   - Boundaries and guardrails
   - High-risk restrictions
   - Deepfake prohibitions

9. **Procurement & Vendor Management**
   - Vendor selection standards
   - Contract requirements
   - Third-party risk assessment
   - Due diligence

10. **Legal & Regulatory Compliance**
    - Federal law compliance
    - State requirements
    - Civil rights protections
    - Professional standards

### Tier 4 (Emerging - in 20-40% of policies)
11. **Community Engagement**
    - Stakeholder consultation
    - Public input mechanisms
    - Trust building
    - Feedback processes

12. **Sustainability & Evaluation**
    - Long-term viability
    - Cost-benefit analysis
    - Success metrics
    - Continuous improvement

---

## Usage Guide

### Step 1: Prioritize Elements

1. Open `ai-policy-prioritization.html`
2. Select your method:
   - **First-time users:** Try "Weighted Scoring" (simplest)
   - **Team workshops:** Use "Pairwise Comparison" (most rigorous)
   - **Quick assessment:** Use "Drag & Rank" (fastest)
   - **Resource allocation:** Use "Budget Allocation" (strategic)

3. Complete the prioritization
4. Download JSON file (e.g., `my-priorities-2026-01-28.json`)

### Step 2: Generate Policy

1. Open `ai-policy-generator.html`
2. Click "Import Rankings" and select your JSON file
   - OR click "Load Sample Rankings" to see an example
3. Fill in organization details:
   - Organization name (required)
   - Jurisdiction type
   - Organization size
   - Policy intensity level
4. Add any additional context
5. Click "Generate Policy Document"

### Step 3: Export & Customize

1. Review the generated policy in the preview pane
2. Choose your export format:
   - **Markdown** - For GitHub, editing in text editors
   - **PDF** - For distribution, official records
   - **DOCX** - For Microsoft Word editing
   - **Copy/Paste** - For quick edits

3. Customize the document:
   - Add organization-specific details
   - Adjust language to match existing policies
   - Have legal counsel review
   - Get stakeholder input

### Step 4: Implement

1. Present to leadership/governance committee
2. Conduct stakeholder review period
3. Finalize based on feedback
4. Formally adopt through appropriate process
5. Communicate to staff
6. Conduct training
7. Schedule annual review

---

## File Formats

### JSON (Rankings Export)

```json
{
  "method": "weighted",
  "timestamp": "2026-01-28T10:30:00.000Z",
  "rankings": [
    {
      "id": 1,
      "name": "Data Privacy & Security",
      "description": "Protection of PHI/PII, secure data handling...",
      "score": 10,
      "tier": 1,
      "method": "weighted"
    }
  ],
  "rawData": {
    "weight-1": 10,
    "weight-2": 9
  }
}
```

### Markdown (Policy Export)

Standard markdown format compatible with:
- GitHub
- GitLab
- Pandoc (for conversion to other formats)
- Static site generators
- Documentation platforms

### DOCX (Word Document)

Professional formatting with:
- Custom styles
- Proper headings structure
- Table of contents
- Consistent fonts and colors
- Print-ready layout

---

## Customization

### Modifying Priority Elements

Edit the `policyElements` array in `ai-policy-prioritization.html`:

```javascript
const policyElements = [
    {
        id: 1,
        name: "Your Custom Element",
        description: "Description of what this covers",
        tier: 1
    }
    // Add more elements as needed
];
```

### Modifying Policy Content

Edit the `policyTemplates` object in `ai-policy-generator.html`:

```javascript
policyTemplates["Your Element"] = {
    high: {
        title: "Your Element Title",
        content: `Your detailed policy content here...`
    },
    medium: { /* ... */ },
    low: { /* ... */ }
};
```

### Adding New Intensity Levels

The system supports three intensity levels by default. To add more:

1. Add intensity option in HTML
2. Update `currentIntensity` variable handling
3. Add corresponding content to all policy templates

---

## Technical Requirements

### Web Applications (HTML files)

**Minimum Requirements:**
- Modern web browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- JavaScript enabled
- 10MB free disk space for downloads

**Recommended:**
- Desktop/laptop for best experience
- 1280x720 screen resolution or higher
- Mouse/trackpad for drag-and-drop features

**Mobile Support:**
- Works on tablets and phones
- Some features limited on small screens
- Touch-enabled for drag operations

### Python Script

**Requirements:**
- Python 3.6 or higher
- pip (Python package installer)

**Dependencies:**
```bash
pip install python-docx --break-system-packages
```

**Optional (for PDF generation):**
```bash
pip install reportlab --break-system-packages
```

---

## Troubleshooting

### Common Issues

**Q: Rankings aren't saving**
A: Check browser localStorage settings. In private/incognito mode, data won't persist.

**Q: DOCX export not working from web interface**
A: Use the Python script (`generate_docx.py`) or download as Markdown and convert using Word or Pandoc.

**Q: Pairwise comparison taking too long**
A: With 12 elements, you'll make 66 comparisons. This is intentional for rigor. Use a different method if time is limited.

**Q: Can't import my rankings**
A: Ensure you're uploading the JSON file downloaded from the prioritization tool. Check that the file isn't corrupted.

**Q: Policy content seems generic**
A: The generated policy is a starting template. Customize it for your organization's specific context, existing policies, and legal requirements.

### Browser Compatibility

**Fully Supported:**
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

**Partially Supported:**
- Internet Explorer 11 (basic features only)
- Older browsers (may have styling issues)

### Getting Help

1. Check this README first
2. Review comments in the HTML/Python files
3. Consult the source research documents
4. Contact your organization's IT department

---

## Best Practices

### For Health Departments

1. **Form a cross-functional team**
   - IT/Informatics
   - Legal/Privacy
   - Public health programs
   - Equity officer
   - Community engagement

2. **Use the prioritization tool in a workshop**
   - 2-hour facilitated session
   - Discuss trade-offs
   - Build consensus
   - Document rationale

3. **Customize the generated policy**
   - Add organization-specific details
   - Align with existing policies
   - Address local concerns
   - Include relevant examples

4. **Review and validate**
   - Legal counsel review
   - Leadership approval
   - Staff input
   - Community stakeholder feedback

5. **Plan for implementation**
   - Training program
   - Communication strategy
   - Compliance monitoring
   - Annual review process

### For Different Organization Sizes

**Small Health Departments (< 50 staff):**
- Use "Basic" intensity level
- Focus on top 4-6 priorities
- Leverage existing state/county policies
- Consider regional collaboration

**Medium Health Departments (50-200 staff):**
- Use "Standard" intensity level
- Address all 12 elements
- Adapt templates to local context
- Build on CDC/state guidance

**Large Health Departments (200+ staff):**
- Use "Comprehensive" intensity level
- Detailed requirements for each element
- Department-specific addenda
- Robust governance structure

---

## Updates and Maintenance

### Policy Review Schedule

Recommended review frequency:
- **Quarterly:** Monitor for major regulatory changes
- **Annually:** Full policy review and update
- **As needed:** When adopting new AI systems

### Template Updates

This template should be updated when:
- New federal regulations are issued
- State laws change
- Significant AI incidents occur
- New best practices emerge
- Technology capabilities shift

### Version History

**Version 1.0 (January 2026)**
- Initial release
- 12 policy elements
- 4 prioritization methods
- 3 intensity levels
- Multi-format export

---

## Legal Disclaimer

**Important:**

1. This tool provides **template guidance only**
2. Generated policies **must be reviewed by legal counsel**
3. Adapt policies to your **specific legal/regulatory context**
4. Policies should **complement, not replace** existing requirements
5. No warranty or guarantee of legal compliance
6. Users are responsible for policy implementation and outcomes

---

## Credits and Attribution

### Research Base
This system synthesizes research from:
- Kansas Health Institute AI Policy Template (2025)
- CDC AI Vision and Strategy (2023-2025)
- HHS Public Health AI Guidance (2024)
- NYC AI Action Plan (2023)
- Multiple state and municipal policies

### Development
Created for state and local health departments to support evidence-based AI policy development.

### License
This tool is provided for public health purposes. Organizations are free to use, modify, and distribute for non-commercial public health applications.

---

## Contact & Feedback

This system was developed as a research tool. For questions about:

- **Kansas Health Institute Template:** Visit khi.org
- **CDC AI Guidance:** Visit cdc.gov/ai
- **HHS AI Strategy:** Visit hhs.gov

---

## Appendix A: Sample Use Cases

### Use Case 1: County Health Department
**Scenario:** 75-person county health department exploring ChatGPT for drafting public communications

**Approach:**
1. Team workshop using Pairwise Comparison method
2. Top priorities: Data Privacy, Transparency, Human Oversight
3. Generated "Standard" intensity policy
4. Added county-specific examples
5. Approved by county counsel and board of health

### Use Case 2: State Health Department
**Scenario:** 500-person state agency developing comprehensive AI governance

**Approach:**
1. Multi-stakeholder process using Budget Allocation method
2. All 12 elements prioritized
3. Generated "Comprehensive" intensity policy
4. Created department-specific addenda
5. Established AI Governance Committee
6. 6-month stakeholder review period

### Use Case 3: City Health Department
**Scenario:** 150-person city agency updating existing policies

**Approach:**
1. Staff survey using Weighted Scoring method
2. Aligned with city-wide AI policy
3. Generated "Standard" intensity policy
4. Integrated with existing data governance
5. Phased implementation over 12 months

---

## Appendix B: Additional Resources

### Federal Resources
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- OMB AI Guidance: https://www.whitehouse.gov/omb/
- CDC AI Vision: https://www.cdc.gov/ai

### State/Local Resources
- ASTHO State AI Legislation Map
- NACCHO AI Resources for LHDs
- NACo AI Resources for Counties
- USCM AI Resources for Cities

### Policy Examples
- Kansas Health Institute AI Template
- NYC AI Action Plan
- Seattle AI Policy
- Baltimore AI Executive Order

---

## Appendix C: Glossary

**Algorithmic Discrimination:** Unfair or biased treatment resulting from AI systems

**Deepfake:** AI-generated synthetic media that appears real

**Equity Impact Assessment:** Analysis of how AI affects different population groups

**Generative AI:** AI that creates new content (text, images, code)

**HIPAA:** Health Insurance Portability and Accountability Act

**Human-in-the-Loop:** AI systems requiring human oversight/approval

**Model Card:** Documentation of AI model's capabilities, limitations, and performance

**PHI:** Protected Health Information

**PII:** Personally Identifiable Information

**Use Case:** Specific application or purpose for which AI is deployed

---

**End of Documentation**

*Last Updated: January 28, 2026*
*System Version: 1.0*
