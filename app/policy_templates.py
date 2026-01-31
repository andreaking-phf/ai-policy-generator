"""
Policy content templates for document generation
Based on evidence from 50+ AI policies including CDC, HHS, NIST, and state/local sources
"""

POLICY_TEMPLATES = {
    "Data Privacy & Security": {
        "high": {
            "title": "Data Privacy and Security",
            "content": """
## Purpose
This organization maintains the highest standards for protecting protected health information (PHI), personally identifiable information (PII), and sensitive data when using artificial intelligence systems.

## Requirements

### Data Classification and Handling
- All data must be classified according to sensitivity level before AI processing
- PHI and PII are strictly prohibited from input into external AI systems including but not limited to ChatGPT, Claude, Gemini, and similar services
- Only de-identified or aggregate data may be used with external AI tools
- Staff must complete data classification training before AI system access

### Technical Safeguards
- All AI systems must comply with HIPAA Security Rule requirements
- Encryption at rest and in transit is mandatory for all AI data processing
- Multi-factor authentication required for all AI system access
- Regular security audits of AI systems conducted quarterly
- Vendor security assessments completed before AI tool procurement

### Data Retention and Disposal
- AI-generated outputs containing sensitive data must follow existing retention schedules
- Secure deletion protocols apply to all AI training data and outputs
- Data breach notification procedures apply to AI systems
- Annual review of data retention practices for AI applications

### Monitoring and Compliance
- Privacy officer reviews all new AI use cases
- Automated monitoring systems track data flows to AI systems
- Regular privacy impact assessments for high-risk AI applications
- Staff violations of data privacy requirements result in immediate access suspension
"""
        },
        "medium": {
            "title": "Data Privacy and Security",
            "content": """
## Purpose
This organization protects sensitive health information when using AI systems, ensuring compliance with applicable privacy laws and regulations.

## Requirements

### Data Protection Standards
- Protected health information (PHI) and personally identifiable information (PII) shall not be input into external AI systems
- Staff must use only de-identified or aggregate data with AI tools
- All AI systems must meet HIPAA compliance standards where applicable

### Security Measures
- Encryption required for AI data processing
- Access controls implemented for all AI systems
- Regular security reviews of AI vendors and tools
- Data breach protocols apply to AI systems

### Accountability
- Privacy officer approves new AI use cases
- Staff training on data privacy in AI contexts
- Documentation of AI data handling practices
"""
        },
        "low": {
            "title": "Data Privacy and Security",
            "content": """
## Purpose
Protect sensitive information when using AI systems.

## Requirements
- Do not input PHI or PII into external AI tools
- Use de-identified data only
- Follow existing data security policies
- Report suspected data breaches
"""
        }
    },
    "Bias, Equity & Discrimination": {
        "high": {
            "title": "Bias Mitigation and Health Equity",
            "content": """
## Purpose
This organization ensures AI systems promote health equity and do not perpetuate or amplify bias, discrimination, or health disparities.

## Requirements

### Pre-Deployment Assessment
- Mandatory equity impact assessment for all AI systems before deployment
- Analysis of training data for representation of protected classes and vulnerable populations
- Evaluation of AI performance across demographic groups including race, ethnicity, age, disability status, language, and socioeconomic status
- Community stakeholder consultation for AI systems affecting public-facing services
- Documentation of potential disparate impacts and mitigation strategies

### Fairness Standards
- AI systems must demonstrate comparable accuracy across all demographic groups
- Performance variance between groups may not exceed 5% without documented justification and mitigation plan
- Proxy discrimination analysis required for all decision-support AI systems
- Regular testing for emergent bias in deployed systems

### Accessibility Requirements
- All AI interfaces must meet WCAG 2.1 Level AA accessibility standards
- Multilingual support required for AI systems serving diverse populations
- Alternative non-AI pathways available for all critical services
- Plain language outputs required for all AI-generated public communications

### Monitoring and Remediation
- Quarterly equity audits of AI system outputs
- Disaggregated data analysis by demographic factors
- Community feedback mechanisms for reporting bias concerns
- Rapid response protocol for identified bias issues
- Annual public reporting of equity metrics for AI systems

### Training and Accountability
- Mandatory bias awareness training for all AI system users and developers
- Leadership accountability for equity outcomes in AI deployment
- Performance evaluations include equity considerations
"""
        },
        "medium": {
            "title": "Bias Mitigation and Health Equity",
            "content": """
## Purpose
Ensure AI systems support health equity and do not discriminate against protected groups.

## Requirements

### Assessment and Testing
- Equity impact assessment required before deploying new AI systems
- Testing for bias across demographic groups
- Analysis of training data representativeness
- Documentation of fairness considerations

### Standards
- AI systems should perform equitably across populations
- Accessibility standards apply to AI interfaces
- Alternative pathways available for AI-driven services
- Plain language in AI communications

### Monitoring
- Regular review of AI system equity impacts
- Mechanisms for reporting bias concerns
- Annual equity reporting for major AI systems
"""
        },
        "low": {
            "title": "Bias and Equity",
            "content": """
## Purpose
Prevent discrimination in AI use.

## Requirements
- Consider equity impacts before using AI
- Test AI systems for bias when possible
- Make AI systems accessible
- Provide alternatives to AI when needed
"""
        }
    },
    "Transparency & Explainability": {
        "high": {
            "title": "Transparency and Explainability",
            "content": """
## Purpose
Maintain public trust through transparent AI practices and ensure AI decision-making processes can be understood and explained.

## Requirements

### Public Disclosure
- Maintain public registry of all AI systems in use, updated quarterly
- Publish AI system documentation including purpose, data sources, and limitations
- Disclose when AI is used in public-facing services or communications
- Annual public report on AI use, impacts, and governance

### Model Documentation
- "Model card" documentation required for all AI systems including:
  - Intended use cases and known limitations
  - Training data sources and characteristics
  - Performance metrics across demographic groups
  - Maintenance and update schedules
  - Known failure modes and risks
- Version control and change logs for all AI models
- Documentation of AI system decision logic and key variables

### User Notification
- Clear disclosure when individuals interact with AI systems
- Notification when AI contributes to decisions affecting individuals
- Explanation of AI's role in decision-making processes
- Information on how to request human review

### Explainability Standards
- AI systems must provide explanation for outputs when requested
- Decision-support AI must show key factors influencing recommendations
- Technical documentation available to oversight bodies
- Non-technical explanations available for affected individuals

### Accountability and Access
- Designated point of contact for AI transparency questions
- Process for public information requests about AI systems
- Regular stakeholder briefings on AI initiatives
- Board and leadership reporting on AI use and impacts
"""
        },
        "medium": {
            "title": "Transparency and Explainability",
            "content": """
## Purpose
Ensure transparency in AI use and maintain public trust.

## Requirements

### Disclosure
- Public listing of AI systems in use
- Disclosure when AI is used in public services
- Documentation of AI system purposes and limitations
- Annual reporting on AI activities

### Documentation
- Record AI system capabilities and constraints
- Track AI system versions and updates
- Document data sources for AI systems

### User Communication
- Notify individuals when AI affects them
- Explain AI's role in decisions
- Provide contact for AI-related questions
"""
        },
        "low": {
            "title": "Transparency",
            "content": """
## Purpose
Be transparent about AI use.

## Requirements
- Disclose AI use to the public
- Keep records of AI systems
- Tell people when AI affects them
- Provide information on request
"""
        }
    },
    "Human Oversight & Accountability": {
        "high": {
            "title": "Human Oversight and Accountability",
            "content": """
## Purpose
Ensure human judgment remains central to decision-making and establish clear accountability for AI system outcomes.

## Requirements

### Human-in-the-Loop Requirements
- AI systems may not make final decisions on matters affecting individual rights, health outcomes, or resource allocation without human review
- Licensed professionals must review and approve AI recommendations in clinical or diagnostic contexts
- Supervisory review required for AI-generated enforcement or compliance decisions
- Override mechanisms available for all AI recommendations

### Professional Judgment
- AI serves as decision support, not decision replacement
- Healthcare providers retain full professional responsibility for patient care decisions
- Public health professionals maintain authority over AI-assisted analyses
- Staff empowered to question or override AI outputs with documentation

### Accountability Framework
- Clear assignment of responsibility for each AI system
- Named system owners accountable for AI outcomes
- Performance metrics include AI system impacts
- Regular audits of AI decision quality and accuracy

### Appeal and Review
- Documented process for individuals to contest AI-influenced decisions
- Timely human review of appeals within 10 business days
- Tracking and analysis of AI decision appeals
- Annual review of appeal patterns and outcomes
"""
        },
        "medium": {
            "title": "Human Oversight and Accountability",
            "content": """
## Purpose
Maintain human control over AI systems and ensure accountability.

## Requirements

### Human Review
- Critical decisions require human review
- Professional judgment takes precedence over AI
- Staff can override AI recommendations
- Appeal process available for AI-influenced decisions

### Accountability
- Designated owners for each AI system
- Clear responsibility for AI outcomes
- Documentation of AI use in decision-making
"""
        },
        "low": {
            "title": "Human Oversight",
            "content": """
## Purpose
Keep humans in control of AI.

## Requirements
- Humans make final decisions
- Staff can override AI
- Clear responsibility for AI systems
"""
        }
    },
    "Accuracy & Validation": {
        "high": {
            "title": "Accuracy, Reliability and Validation",
            "content": """
## Purpose
Ensure AI systems meet rigorous standards for accuracy and reliability in public health applications.

## Requirements

### Pre-Deployment Validation
- Independent validation testing required before deployment
- Performance benchmarks established for each use case
- Testing with representative data samples
- Documentation of validation methodology and results

### Ongoing Monitoring
- Continuous performance monitoring for all deployed AI systems
- Regular accuracy audits against established benchmarks
- Automated alerts for performance degradation
- Quarterly performance reports

### Quality Assurance
- Quality assurance protocols for AI outputs
- Random sampling and review of AI decisions
- Comparison against expert judgment
- Documentation of error rates and correction procedures
"""
        },
        "medium": {
            "title": "Accuracy and Validation",
            "content": """
## Purpose
Ensure AI systems produce reliable results.

## Requirements
- Test AI systems before deployment
- Monitor ongoing performance
- Document accuracy benchmarks
- Regular quality checks
"""
        },
        "low": {
            "title": "Accuracy",
            "content": """
## Purpose
Ensure AI produces accurate results.

## Requirements
- Test AI before use
- Check AI outputs for errors
- Report accuracy concerns
"""
        }
    },
    "Governance & Risk Management": {
        "high": {
            "title": "AI Governance and Risk Management",
            "content": """
## Purpose
Establish comprehensive governance structures and risk management processes for AI systems.

## Requirements

### Governance Structure
- AI Governance Committee with cross-functional representation
- Clear authority and decision-making processes
- Regular committee meetings and documented decisions
- Executive sponsorship and accountability

### Risk Assessment
- Mandatory risk assessment for all AI use cases
- Risk classification framework (high, medium, low)
- Enhanced review for high-risk applications
- Documentation of risk mitigation strategies

### Approval Processes
- Tiered approval based on risk level
- Technical review for all AI procurements
- Legal and privacy review requirements
- Documented approval workflows

### Inventory and Management
- Comprehensive inventory of all AI systems
- Regular review and recertification
- Sunset and decommissioning procedures
- Change management protocols
"""
        },
        "medium": {
            "title": "Governance and Risk Management",
            "content": """
## Purpose
Manage AI systems through appropriate governance and risk processes.

## Requirements
- Governance oversight for AI systems
- Risk assessment for new AI use cases
- Approval process for AI tools
- Inventory of AI systems in use
"""
        },
        "low": {
            "title": "Governance",
            "content": """
## Purpose
Provide oversight for AI use.

## Requirements
- Leadership approval for AI tools
- Track AI systems in use
- Assess risks before deployment
"""
        }
    },
    "Training & Capacity Building": {
        "high": {
            "title": "AI Training and Capacity Building",
            "content": """
## Purpose
Build organizational capacity to effectively and responsibly use AI technologies.

## Requirements

### AI Literacy Program
- Baseline AI literacy training for all staff
- Role-specific training for AI system users
- Advanced training for AI developers and managers
- Regular refresher training

### Competency Assessment
- Skills assessment before AI system access
- Competency verification for advanced users
- Tracking of training completion
- Performance evaluation integration

### Knowledge Management
- Central repository of AI resources and guidance
- Best practices documentation
- Lessons learned sharing
- Community of practice for AI users
"""
        },
        "medium": {
            "title": "Training and Capacity Building",
            "content": """
## Purpose
Ensure staff have skills to use AI effectively.

## Requirements
- AI training for staff using AI tools
- Training documentation and tracking
- Resources for learning about AI
- Ongoing skill development
"""
        },
        "low": {
            "title": "Training",
            "content": """
## Purpose
Train staff on AI use.

## Requirements
- Basic AI training for users
- Training materials available
- Ongoing learning opportunities
"""
        }
    },
    "Use Case Appropriateness": {
        "high": {
            "title": "AI Use Case Appropriateness",
            "content": """
## Purpose
Ensure AI is applied appropriately and establish clear boundaries for AI use.

## Requirements

### Permitted Uses
- Clear criteria for appropriate AI applications
- Pre-approved use case categories
- Innovation within defined boundaries
- Regular review of permitted uses

### Prohibited Uses
- Explicit prohibition of autonomous high-stakes decisions
- No AI for final determinations on rights or benefits
- Restrictions on surveillance applications
- Prohibition on uses violating civil rights

### Use Case Review
- Review process for novel AI applications
- Evaluation criteria for appropriateness
- Documentation of use case decisions
- Appeal process for denied use cases
"""
        },
        "medium": {
            "title": "Use Case Appropriateness",
            "content": """
## Purpose
Apply AI to appropriate use cases.

## Requirements
- Define appropriate AI uses
- Establish prohibited uses
- Review new use cases before deployment
- Document use case decisions
"""
        },
        "low": {
            "title": "Use Case Review",
            "content": """
## Purpose
Ensure AI is used appropriately.

## Requirements
- Consider whether AI is appropriate
- Avoid inappropriate uses
- Get approval for new uses
"""
        }
    },
    "Procurement & Vendor Management": {
        "high": {
            "title": "AI Procurement and Vendor Management",
            "content": """
## Purpose
Ensure AI vendors and products meet organizational standards and requirements.

## Requirements

### Vendor Assessment
- Security assessment for all AI vendors
- Privacy practices evaluation
- Bias and equity review
- Technical capability verification

### Contract Requirements
- Standard AI contract provisions
- Data handling and ownership terms
- Audit rights and transparency requirements
- Performance guarantees and remedies

### Ongoing Management
- Regular vendor performance reviews
- Compliance monitoring
- Issue escalation procedures
- Contract renewal assessments
"""
        },
        "medium": {
            "title": "Procurement and Vendor Management",
            "content": """
## Purpose
Manage AI vendors and procurement appropriately.

## Requirements
- Assess vendors before procurement
- Include AI-specific contract terms
- Monitor vendor performance
- Regular vendor reviews
"""
        },
        "low": {
            "title": "Procurement",
            "content": """
## Purpose
Procure AI tools responsibly.

## Requirements
- Evaluate vendors before purchase
- Include relevant contract terms
- Monitor vendor performance
"""
        }
    },
    "Legal & Regulatory Compliance": {
        "high": {
            "title": "Legal and Regulatory Compliance",
            "content": """
## Purpose
Ensure all AI activities comply with applicable laws, regulations, and legal requirements.

## Requirements

### Regulatory Compliance
- Compliance with all applicable federal laws and regulations
- State and local law compliance
- Industry-specific requirements (HIPAA, etc.)
- Regular compliance assessments

### Civil Rights Protection
- Compliance with civil rights laws
- Non-discrimination requirements
- Accessibility compliance
- Due process protections

### Legal Review
- Legal review for high-risk AI applications
- Contract review for AI procurements
- Liability assessment and mitigation
- Regulatory change monitoring
"""
        },
        "medium": {
            "title": "Legal and Regulatory Compliance",
            "content": """
## Purpose
Comply with applicable laws and regulations.

## Requirements
- Follow applicable laws and regulations
- Protect civil rights
- Legal review for significant AI uses
- Monitor regulatory changes
"""
        },
        "low": {
            "title": "Legal Compliance",
            "content": """
## Purpose
Comply with laws and regulations.

## Requirements
- Follow applicable laws
- Protect individual rights
- Seek legal guidance as needed
"""
        }
    },
    "Community Engagement": {
        "high": {
            "title": "Community Engagement and Stakeholder Involvement",
            "content": """
## Purpose
Engage community stakeholders in AI governance and ensure public input in AI decisions.

## Requirements

### Public Participation
- Community input opportunities for major AI initiatives
- Public comment periods for AI policies
- Stakeholder advisory processes
- Community representation in governance

### Communication
- Public communication about AI use
- Accessible information about AI systems
- Response to community concerns
- Regular public updates

### Trust Building
- Proactive community outreach
- Education about AI capabilities and limitations
- Address community concerns transparently
- Demonstrate accountability through action
"""
        },
        "medium": {
            "title": "Community Engagement",
            "content": """
## Purpose
Engage stakeholders in AI governance.

## Requirements
- Seek community input on major AI uses
- Communicate about AI activities
- Address community concerns
- Build public trust
"""
        },
        "low": {
            "title": "Community Input",
            "content": """
## Purpose
Consider community perspectives.

## Requirements
- Seek input when appropriate
- Communicate about AI use
- Address concerns raised
"""
        }
    },
    "Sustainability & Evaluation": {
        "high": {
            "title": "Sustainability and Continuous Evaluation",
            "content": """
## Purpose
Ensure long-term sustainability and continuous improvement of AI programs.

## Requirements

### Evaluation Framework
- Defined metrics for AI system success
- Regular evaluation against objectives
- Cost-benefit analysis
- Impact assessment

### Continuous Improvement
- Lessons learned processes
- Regular policy and practice updates
- Innovation and advancement
- Best practice adoption

### Sustainability Planning
- Long-term resource planning
- Skill development pipeline
- Technology roadmap
- Budget sustainability
"""
        },
        "medium": {
            "title": "Sustainability and Evaluation",
            "content": """
## Purpose
Evaluate and sustain AI programs over time.

## Requirements
- Evaluate AI system effectiveness
- Plan for long-term sustainability
- Continuous improvement processes
- Regular program review
"""
        },
        "low": {
            "title": "Evaluation",
            "content": """
## Purpose
Evaluate AI effectiveness.

## Requirements
- Assess AI system results
- Improve based on experience
- Plan for sustainability
"""
        }
    }
}


def get_template(element_name, priority_level):
    """Get the policy template for a given element and priority level."""
    if element_name in POLICY_TEMPLATES:
        templates = POLICY_TEMPLATES[element_name]
        if priority_level in templates:
            return templates[priority_level]
        return templates.get('medium', templates.get('low', None))
    return None
