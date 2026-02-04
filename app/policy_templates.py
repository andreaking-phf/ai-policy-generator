"""
Policy content templates for document generation
Based on evidence from 50+ AI policies including CDC, HHS, NIST, and state/local sources
Structured as formal government policy language ready for adoption
"""

POLICY_TEMPLATES = {
    "Data Privacy & Security": {
        "high": {
            "title": "Data Privacy and Security",
            "content": """
### 1. Policy Statement

It is the policy of this organization that all artificial intelligence (AI) systems and tools shall be deployed, operated, and maintained in full compliance with applicable federal, state, and local privacy laws and regulations, including but not limited to the Health Insurance Portability and Accountability Act of 1996 (HIPAA), 42 C.F.R. Part 2, the Privacy Act of 1974, and any applicable state health information privacy statutes. This organization shall protect protected health information (PHI), personally identifiable information (PII), and all sensitive data from unauthorized access, use, or disclosure when processed by or in connection with AI systems.

### 2. Definitions

For purposes of this section:

- **Protected Health Information (PHI):** Individually identifiable health information as defined under 45 C.F.R. Section 160.103, including demographic data, medical histories, test results, insurance information, and any other information that can be used to identify a patient or individual and relates to their past, present, or future health condition, provision of care, or payment for care.
- **Personally Identifiable Information (PII):** Information that can be used to distinguish or trace an individual's identity, either alone or when combined with other information that is linked or linkable to a specific individual, consistent with OMB Circular A-130.
- **External AI System:** Any AI tool, platform, or service hosted, operated, or maintained by a third-party vendor or accessible via the public internet, including but not limited to ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Copilot (Microsoft), and similar generative AI services.
- **De-identified Data:** Data that has been processed to remove or obscure all identifiers in accordance with the HIPAA Safe Harbor method (45 C.F.R. Section 164.514(b)) or the Expert Determination method (45 C.F.R. Section 164.514(a)), such that the remaining information cannot reasonably be used to identify an individual.
- **Data Classification Level:** A designation assigned to information assets based on sensitivity: Level 1 (Public), Level 2 (Internal), Level 3 (Confidential), Level 4 (Restricted/PHI/PII).

### 3. Data Classification and Handling Requirements

3.1. All data intended for processing by an AI system shall be classified according to the organization's data classification framework prior to use. No data classified at Level 3 (Confidential) or Level 4 (Restricted/PHI/PII) shall be entered into, uploaded to, or otherwise processed by any External AI System.

3.2. Only de-identified data meeting the HIPAA Safe Harbor or Expert Determination standard, or data classified at Level 1 (Public) or Level 2 (Internal), may be used with External AI Systems. Staff shall verify the classification of all data before submitting it to any AI system and shall document such verification when processing data at Level 2 or above.

3.3. The Privacy Officer or designee shall maintain a current register of all approved AI systems and the maximum data classification level each system is authorized to process. This register shall be updated within five (5) business days of any change in system authorization.

3.4. Staff shall not copy, paste, upload, or otherwise transfer the following into any External AI System: patient names, dates of birth, Social Security numbers, medical record numbers, health plan beneficiary numbers, addresses, telephone numbers, email addresses, biometric identifiers, full-face photographs, or any other HIPAA-defined identifier.

3.5. All staff who access or use AI systems shall complete data classification training within thirty (30) calendar days of initial assignment and annually thereafter. Training shall include hands-on exercises in identifying PHI and PII, proper de-identification techniques, and the use of the organization's data classification register.

### 4. Technical Safeguards

4.1. All AI systems that process organization data at Level 2 or above shall comply with the HIPAA Security Rule (45 C.F.R. Part 164, Subpart C), including the implementation of administrative, physical, and technical safeguards appropriate to the sensitivity of the data processed.

4.2. Data encryption shall be required at rest (AES-256 or equivalent) and in transit (TLS 1.2 or higher) for all data processed by AI systems. No exceptions to this requirement shall be granted without written approval from the Chief Information Security Officer (CISO) or equivalent authority.

4.3. Access to AI systems that process Level 3 or Level 4 data shall require multi-factor authentication (MFA). Access credentials shall not be shared among staff. Individual user accounts shall be provisioned, and access logs shall be maintained for a minimum of six (6) years consistent with HIPAA retention requirements.

4.4. The IT Security team shall conduct security assessments of all AI systems prior to procurement and deployment, including vulnerability scanning, penetration testing for high-risk systems, and review of vendor security certifications (e.g., SOC 2 Type II, HITRUST, FedRAMP). Quarterly security audits shall be conducted for all deployed AI systems processing Level 3 or Level 4 data.

4.5. AI vendors shall provide evidence of compliance with applicable security standards, including a current SOC 2 Type II report or equivalent certification, prior to contract execution. Vendor security assessments shall be reviewed and updated annually.

### 5. Data Retention and Disposal

5.1. AI-generated outputs containing data classified at Level 2 or above shall be subject to the organization's existing records retention schedule. Staff shall apply the appropriate retention period based on the highest classification level of data used to generate the output.

5.2. When AI-generated records reach the end of their retention period, or when an AI system is decommissioned, all associated data shall be disposed of using NIST SP 800-88-compliant media sanitization methods. Certificates of destruction shall be obtained and retained for records classified at Level 3 or above.

5.3. Prompt and conversation history stored within AI systems shall be reviewed quarterly by the Privacy Officer to assess whether retained data complies with applicable retention requirements. Data retained beyond its authorized period shall be purged within thirty (30) calendar days of identification.

### 6. Incident Response and Breach Notification

6.1. Any suspected or confirmed unauthorized access to, use of, or disclosure of PHI, PII, or other sensitive data through an AI system shall be reported immediately to the Privacy Officer and the IT Security team in accordance with the organization's existing Incident Response Plan.

6.2. The Privacy Officer shall conduct a risk assessment consistent with 45 C.F.R. Section 164.402 to determine whether an impermissible use or disclosure of PHI constitutes a breach requiring notification under the HIPAA Breach Notification Rule (45 C.F.R. Sections 164.404-164.408).

6.3. The organization shall maintain documentation of all AI-related security incidents, including the date of discovery, nature of the incident, data affected, remediation actions taken, and any notifications issued. Such records shall be retained for a minimum of six (6) years.

### 7. Monitoring and Compliance

7.1. The Privacy Officer shall review and approve all proposed new AI use cases involving data at Level 2 or above prior to implementation. Approval shall be documented using the organization's AI Use Case Request Form and retained in the AI governance record.

7.2. The IT Security team shall implement automated monitoring to detect and alert on unauthorized data transfers to external AI systems, including data loss prevention (DLP) tools where technically feasible.

7.3. The Privacy Officer shall conduct or commission a Privacy Impact Assessment (PIA) for all AI applications classified as high-risk under the organization's AI Risk Classification Framework, and shall update existing PIAs when material changes are made to an AI system's data processing practices.

7.4. Staff who violate this section's requirements shall be subject to immediate suspension of AI system access pending investigation. Confirmed violations shall be addressed through the organization's disciplinary procedures and may result in corrective action up to and including termination of employment or contract, and referral to appropriate authorities where required by law.
"""
        },
        "medium": {
            "title": "Data Privacy and Security",
            "content": """
### 1. Policy Statement

It is the policy of this organization to protect all protected health information (PHI), personally identifiable information (PII), and sensitive data when using artificial intelligence systems, consistent with the Health Insurance Portability and Accountability Act (HIPAA), applicable state privacy laws, and organizational data governance policies.

### 2. Data Protection Standards

2.1. Protected health information and personally identifiable information shall not be entered into, uploaded to, or otherwise processed by external AI systems, including but not limited to ChatGPT, Claude, Gemini, Copilot, and similar services. Staff shall use only de-identified or aggregate data when working with these tools.

2.2. De-identification shall be performed in accordance with the HIPAA Safe Harbor method (removal of 18 specified identifiers) or the Expert Determination method prior to any use of data with external AI systems. Staff are responsible for verifying that data has been properly de-identified before submission.

2.3. All AI systems used within the organization shall meet HIPAA Security Rule requirements where applicable, including encryption at rest and in transit, access controls with individual user credentials, and audit logging of system access and data transactions.

### 3. Security Measures

3.1. The IT Security team shall conduct a security assessment of all AI tools prior to procurement and deployment, including review of vendor security certifications and data handling practices. AI vendors processing organizational data shall provide evidence of SOC 2 Type II compliance or equivalent certification.

3.2. Access to AI systems processing confidential or restricted data shall require multi-factor authentication. Access shall be granted based on role-based permissions consistent with the principle of least privilege.

3.3. The organization's data breach notification and incident response procedures shall apply to all AI systems. Any suspected unauthorized disclosure of sensitive data through an AI system shall be reported to the Privacy Officer immediately upon discovery.

### 4. Accountability

4.1. The Privacy Officer shall review and approve all new AI use cases that involve data classified as confidential or above prior to implementation. Approvals shall be documented and maintained in the AI governance record.

4.2. All staff who use AI systems shall complete training on data privacy requirements specific to AI within sixty (60) calendar days of assignment and annually thereafter. Training shall address data classification, de-identification procedures, and prohibited uses of sensitive data with AI tools.

4.3. The organization shall maintain documentation of all AI data handling practices, including records of which AI systems process which categories of data, applicable data retention periods, and access control configurations.
"""
        },
        "low": {
            "title": "Data Privacy and Security",
            "content": """
### 1. Policy Statement

This organization shall protect sensitive health and personal information when using AI systems, consistent with HIPAA and applicable privacy laws.

### 2. Requirements

2.1. Staff shall not enter protected health information (PHI) or personally identifiable information (PII) into external AI tools such as ChatGPT, Claude, Gemini, or similar services. Only de-identified or publicly available data may be used with these tools.

2.2. All AI systems used by the organization shall comply with existing data security policies, including encryption requirements and access controls.

2.3. Staff shall report any suspected unauthorized disclosure of sensitive data through AI systems to their supervisor and the Privacy Officer immediately upon discovery, consistent with the organization's incident response procedures.

2.4. Staff shall complete data privacy training as it relates to AI use as part of their annual compliance training.
"""
        }
    },
    "Bias, Equity & Discrimination": {
        "high": {
            "title": "Bias Mitigation and Health Equity",
            "content": """
### 1. Policy Statement

This organization is committed to ensuring that all AI systems used in the delivery of public health services promote health equity and do not perpetuate, amplify, or introduce bias, discrimination, or health disparities against any individual or population group. AI systems shall be assessed for equity impacts before deployment and monitored throughout their operational lifecycle, consistent with Title VI of the Civil Rights Act of 1964, Section 504 of the Rehabilitation Act of 1973, the Americans with Disabilities Act (ADA), Executive Order 13985 on Advancing Racial Equity, and applicable state and local civil rights protections.

### 2. Definitions

- **Algorithmic Discrimination:** The condition in which an AI system contributes to unjustified differential treatment or disparate impact on individuals or groups based on race, color, ethnicity, national origin, sex, gender identity, sexual orientation, age, disability status, religion, language proficiency, socioeconomic status, or other protected characteristics.
- **Equity Impact Assessment (EIA):** A structured evaluation conducted prior to AI system deployment to identify potential disparate impacts on protected classes and vulnerable populations, assess the representativeness of training data, and document mitigation strategies.
- **Disparate Impact:** A facially neutral practice or system output that disproportionately and adversely affects members of a protected class, as measured by statistically significant differences in outcomes across demographic groups.
- **Proxy Variable:** A data element that, while not itself a protected characteristic, is highly correlated with a protected characteristic and may serve as a substitute for that characteristic in AI decision-making, resulting in indirect discrimination.

### 3. Pre-Deployment Equity Assessment

3.1. A mandatory Equity Impact Assessment (EIA) shall be completed for all AI systems before deployment. The EIA shall be conducted by or in consultation with the Equity Officer or designated equity review body and shall evaluate: (a) the representativeness of training data across demographic groups; (b) the system's performance metrics disaggregated by race, ethnicity, age, sex, disability status, language proficiency, and socioeconomic status; (c) the potential for proxy discrimination through correlated variables; and (d) the availability of alternative non-AI pathways for individuals who may be adversely affected.

3.2. For AI systems that directly affect public-facing services, resource allocation, or individual health outcomes, the organization shall conduct community stakeholder consultation prior to deployment. Consultation shall include representatives of communities disproportionately affected by health disparities and shall provide meaningful opportunity for input on system design, data practices, and potential impacts.

3.3. The EIA shall document all identified potential disparate impacts and shall include a written mitigation plan for each identified risk. AI systems that present unmitigable risks of significant disparate impact shall not be deployed without written approval from the agency head or designee, accompanied by a documented public interest justification.

### 4. Fairness Standards

4.1. AI systems shall demonstrate comparable accuracy, precision, recall, and false positive/negative rates across all demographic groups for which data are available. Performance variance between any two demographic groups shall not exceed five percent (5%) without a documented justification and an approved mitigation plan.

4.2. The organization shall conduct proxy discrimination analysis for all AI systems used in decision-support contexts to identify data elements that may serve as proxies for protected characteristics. Where proxy effects are identified, the organization shall implement appropriate corrective measures, which may include variable exclusion, algorithmic adjustment, or system redesign.

4.3. AI systems used in the allocation of public health resources, enforcement actions, or benefit determinations shall be subject to enhanced fairness review, including independent third-party audit where feasible, prior to deployment and at least annually thereafter.

### 5. Accessibility Requirements

5.1. All AI-powered interfaces, outputs, and communications accessible to the public or to staff shall conform to Web Content Accessibility Guidelines (WCAG) 2.1 Level AA, consistent with Section 508 of the Rehabilitation Act and ADA Title II requirements.

5.2. AI systems serving linguistically diverse populations shall provide multilingual support in the languages most commonly spoken in the jurisdiction, as determined by the most recent American Community Survey data or equivalent assessment. At minimum, outputs shall be available in English and Spanish; additional languages shall be added based on community need.

5.3. For all critical public health services in which AI systems play a role, the organization shall maintain alternative non-AI pathways that are equally accessible and do not disadvantage individuals who cannot or choose not to interact with AI-driven processes.

5.4. All AI-generated public communications shall use plain language at or below an eighth-grade reading level, consistent with federal plain language guidelines.

### 6. Ongoing Monitoring and Remediation

6.1. The Equity Officer or designee shall conduct equity audits of all deployed AI systems on a quarterly basis. Audits shall include disaggregated analysis of system outputs and outcomes by available demographic factors and comparison against established fairness benchmarks.

6.2. The organization shall maintain an accessible mechanism (e.g., web form, telephone hotline, in-person reporting) through which community members, staff, and stakeholders can report concerns about bias or discriminatory impacts of AI systems. All reports shall be acknowledged within five (5) business days and investigated within thirty (30) calendar days.

6.3. When bias or disparate impact is identified in a deployed AI system, the organization shall implement its Rapid Response Protocol, which shall include: (a) immediate assessment of severity and scope; (b) interim mitigation measures, including suspension of the system if warranted; (c) root cause analysis; (d) corrective action plan with defined timelines; and (e) notification to affected communities where appropriate.

6.4. The organization shall publish an annual public report summarizing equity metrics for all AI systems, including identified bias issues, corrective actions taken, and outcomes of community feedback received.

### 7. Training and Accountability

7.1. All staff who develop, deploy, or use AI systems shall complete bias awareness and health equity training within sixty (60) calendar days of assignment and annually thereafter. Training shall address structural determinants of health, the mechanisms by which algorithmic bias arises, and staff obligations under this policy.

7.2. Leadership and management personnel with oversight of AI systems shall be accountable for equity outcomes within their areas of responsibility. Equity performance related to AI systems shall be incorporated into annual performance evaluations for relevant supervisory staff.
"""
        },
        "medium": {
            "title": "Bias Mitigation and Health Equity",
            "content": """
### 1. Policy Statement

This organization shall ensure that AI systems support health equity and do not discriminate against individuals or groups based on race, ethnicity, age, sex, disability status, language, socioeconomic status, or other protected characteristics, consistent with Title VI of the Civil Rights Act, the ADA, and applicable state civil rights laws.

### 2. Assessment and Testing

2.1. An Equity Impact Assessment shall be completed for all new AI systems prior to deployment. The assessment shall evaluate training data representativeness, performance across demographic groups, and potential for disparate impact. The Equity Officer or designee shall review and approve the assessment before the system is authorized for use.

2.2. AI systems shall be tested for bias across available demographic categories, including at minimum race, ethnicity, age, sex, and disability status. Testing results shall be documented and retained in the AI governance record.

2.3. AI systems used in decision-support, resource allocation, or public-facing services shall receive enhanced review, including analysis of proxy variables that may correlate with protected characteristics.

### 3. Standards

3.1. AI systems shall perform equitably across all population groups served by the organization. Where performance disparities are identified, the responsible system owner shall develop and implement a corrective action plan within sixty (60) calendar days.

3.2. AI interfaces accessible to the public shall meet WCAG 2.1 Level AA accessibility standards. Multilingual support shall be provided for AI-driven services that interact with linguistically diverse communities.

3.3. Alternative non-AI pathways shall remain available for all services in which AI plays a decision-support or service delivery role, ensuring no individual is disadvantaged by the use of AI.

3.4. AI-generated public communications shall use plain language consistent with federal plain language guidelines.

### 4. Monitoring

4.1. The organization shall conduct regular reviews of AI system equity impacts, including disaggregated outcome analysis, at least annually for all deployed systems.

4.2. The organization shall provide a mechanism for community members and staff to report concerns about AI bias. Reports shall be reviewed by the Equity Officer and addressed within thirty (30) calendar days.

4.3. The organization shall produce an annual summary of equity metrics for major AI systems, including any identified issues and corrective actions taken.
"""
        },
        "low": {
            "title": "Bias and Equity",
            "content": """
### 1. Policy Statement

This organization shall ensure that AI systems do not discriminate against individuals or groups based on protected characteristics, consistent with applicable civil rights laws and the organization's commitment to health equity.

### 2. Requirements

2.1. Staff shall consider potential equity impacts before deploying or using AI systems, particularly for applications that affect public-facing services, resource allocation, or individual health outcomes.

2.2. AI systems shall be tested for bias across demographic groups when feasible. Where bias is identified, staff shall report findings to their supervisor and the AI governance lead, and corrective action shall be taken before continued use.

2.3. AI interfaces and outputs intended for public use shall be accessible to individuals with disabilities and, where possible, available in languages commonly spoken in the jurisdiction served.

2.4. Alternative non-AI pathways shall remain available for individuals who cannot or choose not to interact with AI-driven processes.
"""
        }
    },
    "Transparency & Explainability": {
        "high": {
            "title": "Transparency and Explainability",
            "content": """
### 1. Policy Statement

This organization shall maintain the highest standards of transparency regarding its use of AI systems. The public has a right to know when and how AI is used in the delivery of public health services, and individuals have a right to understand how AI-generated outputs may affect them. This policy establishes requirements for public disclosure, system documentation, user notification, and explainability of AI systems, consistent with principles articulated in the NIST AI Risk Management Framework, Executive Order 14110 on Safe, Secure, and Trustworthy AI, and applicable state transparency requirements.

### 2. Definitions

- **AI System Registry:** A publicly accessible inventory of all AI systems in operational use by the organization, including each system's name, purpose, data inputs, vendor (if applicable), deployment date, and responsible system owner.
- **Model Card:** A standardized documentation artifact for an AI system that describes its intended use cases, known limitations, training data characteristics, performance metrics across demographic groups, maintenance schedule, and known failure modes, consistent with the format recommended by the NIST AI RMF.
- **Explainability:** The capacity of an AI system to provide a clear, understandable account of how it arrived at a specific output, recommendation, or decision, in terms appropriate to the intended audience.

### 3. Public Disclosure

3.1. The organization shall establish and maintain a public AI System Registry, accessible via the organization's website, listing all AI systems in operational use. The Registry shall be updated within fifteen (15) business days of any new AI system deployment, material system modification, or system decommissioning.

3.2. For each AI system listed in the Registry, the organization shall publish: (a) the system name and vendor; (b) a plain-language description of the system's purpose and function; (c) the categories of data processed; (d) known limitations and risks; (e) the name and contact information of the responsible system owner; and (f) the date of most recent review or update.

3.3. The organization shall disclose, through signage, website notice, or direct communication, whenever AI systems are used in public-facing services, public communications, or interactions with members of the public. Disclosure shall be made at or before the point of interaction.

3.4. The organization shall publish an annual public report on AI governance, including: the number and types of AI systems in use; new deployments and decommissions during the reporting period; summary equity and performance metrics; community feedback received and organizational response; and plans for the coming year.

### 4. Model Documentation

4.1. A Model Card shall be prepared and maintained for each AI system deployed by the organization. Model Cards shall include: (a) intended and prohibited use cases; (b) a description of training data, including source, size, and demographic composition; (c) performance metrics, including accuracy, precision, recall, and fairness metrics disaggregated by available demographic categories; (d) known failure modes and edge cases; (e) maintenance and retraining schedule; and (f) version history and change log.

4.2. Model Cards shall be reviewed and updated by the responsible system owner at least annually, or within thirty (30) calendar days of any material change to the AI system's model, training data, or operational parameters.

4.3. Model Cards for AI systems classified as high-risk shall be made available to oversight bodies, including the AI Governance Committee, upon request. Redacted versions excluding proprietary information shall be available to the public upon written request through the organization's public records process.

### 5. User and Individual Notification

5.1. The organization shall clearly disclose to individuals when they are interacting with an AI system, including chatbots, automated decision tools, and AI-assisted communication systems. Disclosure shall be provided in plain language and in accessible formats.

5.2. When an AI system contributes to a decision that materially affects an individual's rights, benefits, health services, or legal status, the organization shall notify the affected individual of: (a) the fact that AI was used; (b) the role AI played in the decision; (c) the key factors that influenced the AI output; and (d) the individual's right to request human review.

5.3. The organization shall designate a point of contact for public inquiries regarding AI systems. Contact information shall be published on the organization's website and included in the AI System Registry.

### 6. Explainability Standards

6.1. AI systems used in decision-support contexts shall be capable of providing an explanation of the key factors and data inputs that influenced a specific output or recommendation. Explanations shall be sufficient to allow a qualified reviewer to understand and evaluate the basis for the AI output.

6.2. For non-technical audiences, including affected individuals and community members, the organization shall provide plain-language explanations of how AI systems work, what data they use, and how their outputs are used in organizational decision-making.

6.3. Technical documentation sufficient to support audit, regulatory review, and legislative oversight shall be maintained for all AI systems and made available to authorized oversight bodies upon request.

6.4. The organization shall regularly brief senior leadership and governance bodies on AI initiatives, system performance, and emerging issues. Briefings shall occur at least quarterly for the AI Governance Committee and annually for the governing board or equivalent authority.
"""
        },
        "medium": {
            "title": "Transparency and Explainability",
            "content": """
### 1. Policy Statement

This organization shall maintain transparency in its use of AI systems, ensuring the public and affected individuals are informed about when and how AI is used in public health services, consistent with organizational values of openness and accountability.

### 2. Disclosure Requirements

2.1. The organization shall maintain a public listing of AI systems in operational use, including each system's purpose, the categories of data it processes, and the responsible system owner. The listing shall be published on the organization's website and updated at least semi-annually.

2.2. The organization shall disclose to the public, through appropriate means, when AI systems are used in public-facing services or communications. Disclosure shall be made in plain language.

2.3. The organization shall produce an annual report summarizing AI activities, including systems deployed, performance outcomes, and community feedback.

### 3. Documentation

3.1. The organization shall maintain documentation for each AI system, including its capabilities, limitations, data sources, and performance characteristics. Documentation shall be reviewed and updated at least annually by the responsible system owner.

3.2. Changes to AI systems, including model updates, data source modifications, and operational parameter adjustments, shall be recorded in a change log maintained by the responsible system owner.

### 4. User Communication

4.1. When AI contributes to a decision that affects an individual's services, benefits, or rights, the organization shall notify the affected individual of the AI's involvement and provide information on how to request human review.

4.2. The organization shall designate a point of contact for questions about AI systems. Contact information shall be available on the organization's website.

4.3. AI outputs directed at the public shall be provided in plain language and accessible formats.
"""
        },
        "low": {
            "title": "Transparency",
            "content": """
### 1. Policy Statement

This organization shall be transparent about its use of AI systems, consistent with its obligations of public accountability.

### 2. Requirements

2.1. The organization shall disclose to the public that it uses AI systems in its operations, including a general description of the purposes for which AI is used. This disclosure shall be available on the organization's website.

2.2. Staff shall inform individuals when AI has contributed to a decision that affects them, when practicable, and shall provide information on how to request human review.

2.3. The organization shall maintain internal records of all AI systems in use, including system name, purpose, vendor, and responsible staff member.

2.4. Staff shall respond to public inquiries regarding the organization's use of AI in a timely and informative manner.
"""
        }
    },
    "Human Oversight & Accountability": {
        "high": {
            "title": "Human Oversight and Accountability",
            "content": """
### 1. Policy Statement

This organization shall ensure that human judgment, professional expertise, and ethical reasoning remain central to all decision-making processes in which AI systems participate. AI systems shall function as decision-support tools and shall not autonomously render final determinations on matters affecting individual rights, health outcomes, public safety, enforcement actions, or the allocation of public resources. Clear lines of accountability shall be established for every AI system, and individuals affected by AI-assisted decisions shall have meaningful access to human review.

### 2. Definitions

- **Human-in-the-Loop (HITL):** An operational model in which a qualified human decision-maker reviews, approves, modifies, or rejects every AI system output before it is implemented or communicated as a final determination.
- **Human-on-the-Loop (HOTL):** An operational model in which a qualified human decision-maker monitors AI system operations and retains the authority and capability to intervene, override, or halt the system at any time, but does not review every individual output.
- **System Owner:** The designated individual with managerial accountability for the performance, compliance, and outcomes of a specific AI system, including responsibility for ensuring adherence to this policy.
- **High-Stakes Decision:** Any determination that materially affects an individual's legal rights, access to health services, receipt of public benefits, employment status, or exposure to enforcement or regulatory action.

### 3. Human Review Requirements

3.1. All high-stakes decisions shall require Human-in-the-Loop review. AI systems shall not render autonomous final determinations on matters including but not limited to: (a) individual eligibility for health services or public benefits; (b) clinical diagnoses or treatment recommendations; (c) public health enforcement or compliance actions; (d) allocation of emergency resources; (e) personnel actions including hiring, discipline, or termination; and (f) any determination that restricts an individual's rights or liberty.

3.2. Licensed professionals, including physicians, epidemiologists, environmental health specialists, and other credentialed public health practitioners, shall retain full professional responsibility for decisions within their scope of practice, regardless of any AI system recommendation. AI outputs in clinical or professional contexts shall be treated as advisory only.

3.3. For AI systems operating in a Human-on-the-Loop model, the organization shall establish documented monitoring protocols specifying: (a) the frequency of human review of system outputs; (b) the thresholds and conditions under which human intervention is required; (c) the mechanisms available for overriding or halting the system; and (d) the qualifications and training required for monitoring personnel.

3.4. All AI systems shall include a readily accessible override mechanism that allows authorized staff to modify or reject any AI-generated output. The exercise of professional override shall be documented but shall not require prior supervisory approval, and staff shall not be penalized for exercising good-faith professional judgment in overriding AI recommendations.

### 4. Accountability Framework

4.1. Every AI system deployed by the organization shall have a named System Owner who is accountable for the system's performance, compliance with this policy, and the quality of outcomes produced. The System Owner shall be identified in the AI System Registry and shall hold sufficient authority to modify or suspend system operations.

4.2. Department heads and division directors shall be accountable for AI use within their organizational units, including ensuring that staff are trained, that AI systems are used in accordance with this policy, and that adverse outcomes are reported and addressed.

4.3. The AI Governance Committee shall maintain oversight of all AI systems and shall receive quarterly reports from System Owners on system performance, compliance, incidents, and user feedback.

4.4. The organization shall conduct regular audits of AI-assisted decisions, including random sampling and review by qualified staff, to assess decision quality, accuracy, and consistency with professional standards. Audit results shall be reported to the AI Governance Committee.

### 5. Appeal and Redress

5.1. Any individual affected by a decision in which an AI system played a role shall have the right to: (a) be informed that AI contributed to the decision; (b) receive a clear explanation of the factors considered; (c) request a full human review of the decision by a qualified staff member who was not involved in the original determination; and (d) receive a written response to their appeal.

5.2. Human review of appeals shall be completed within ten (10) business days of receipt, unless a shorter timeframe is required by applicable law or regulation. The reviewing official shall have the authority to affirm, modify, or reverse the original determination.

5.3. The organization shall track and analyze all appeals of AI-assisted decisions, including the number of appeals received, the outcomes of appeals (affirmed, modified, reversed), and patterns or trends in appeal subject matter. The AI Governance Committee shall review appeal data at least annually and direct corrective action where patterns indicate systemic issues.
"""
        },
        "medium": {
            "title": "Human Oversight and Accountability",
            "content": """
### 1. Policy Statement

This organization shall maintain meaningful human oversight of AI systems and establish clear accountability for AI-assisted decisions. AI shall serve as a decision-support tool, and human judgment shall remain authoritative in all final determinations, particularly those affecting individual rights, health outcomes, or access to services.

### 2. Human Review Requirements

2.1. Decisions that materially affect individual rights, health services, benefits, or enforcement actions shall require human review before being finalized. AI system outputs in these contexts shall be treated as recommendations, not determinations.

2.2. Licensed professionals shall retain full professional authority over decisions within their scope of practice. AI recommendations shall be advisory only in clinical, diagnostic, and professional practice contexts.

2.3. Staff shall have the ability to override AI recommendations when, in their professional judgment, the AI output is inaccurate, incomplete, or inappropriate. Overrides shall be documented but shall not require prior approval.

2.4. An appeal process shall be available to individuals affected by decisions in which AI played a role. Individuals shall be informed of their right to request human review, and reviews shall be completed within ten (10) business days.

### 3. Accountability

3.1. Each AI system shall have a designated System Owner who is accountable for the system's performance and compliance with this policy. The System Owner shall be documented in the organization's AI inventory.

3.2. Department heads shall be responsible for ensuring appropriate AI use within their units, including staff training and compliance with this policy.

3.3. AI-assisted decisions shall be documented, including the AI system used, the output generated, and the human decision-maker's final determination.
"""
        },
        "low": {
            "title": "Human Oversight",
            "content": """
### 1. Policy Statement

This organization shall ensure that human decision-makers retain authority over all final determinations in which AI systems participate. AI shall support but not replace human judgment.

### 2. Requirements

2.1. Staff shall make all final decisions on matters affecting individuals' rights, health services, or benefits. AI outputs shall be used as one input among others and shall not be the sole basis for such decisions.

2.2. Staff may override AI recommendations when their professional judgment warrants it. Overrides shall be briefly documented for the record.

2.3. Each AI system shall have a designated staff member responsible for its appropriate use and performance.

2.4. Individuals who believe they have been adversely affected by an AI-assisted decision may request human review through the organization's existing complaint or grievance process.
"""
        }
    },
    "Accuracy & Validation": {
        "high": {
            "title": "Accuracy, Reliability, and Validation",
            "content": """
### 1. Policy Statement

This organization shall ensure that all AI systems meet rigorous standards for accuracy, reliability, and validity before deployment and throughout their operational lifecycle. AI systems used in public health practice must produce outputs that are scientifically sound, clinically appropriate where applicable, and fit for their intended purpose. The organization shall implement validation, monitoring, and quality assurance processes proportionate to the risk level of each AI application.

### 2. Pre-Deployment Validation

2.1. All AI systems shall undergo independent validation testing before being authorized for operational use. Validation shall be conducted using data representative of the populations and conditions the system will encounter in practice, and shall be performed by personnel who were not involved in the system's development or selection.

2.2. Performance benchmarks shall be established for each AI use case prior to deployment, including minimum acceptable thresholds for accuracy, precision, recall, specificity, and other metrics appropriate to the application. AI systems that fail to meet established benchmarks shall not be deployed without written justification and approval from the AI Governance Committee.

2.3. Validation results shall be documented in the system's Model Card, including the methodology used, the composition and size of the validation dataset, performance metrics achieved, and any identified limitations or failure modes.

### 3. Ongoing Performance Monitoring

3.1. All deployed AI systems shall be subject to continuous or periodic performance monitoring appropriate to their risk classification. High-risk systems shall be monitored continuously or at least monthly; standard-risk systems shall be monitored at least quarterly.

3.2. The responsible System Owner shall establish performance monitoring protocols, including automated alerting for performance degradation beyond defined thresholds, and shall ensure that monitoring results are documented and reviewed.

3.3. Quarterly performance reports shall be prepared for all AI systems and submitted to the AI Governance Committee. Reports shall include current performance metrics compared against established benchmarks, any incidents of performance degradation, and corrective actions taken.

3.4. AI systems that experience sustained performance degradation below established benchmarks shall be suspended from operational use pending investigation, recalibration, or replacement. The System Owner shall notify the AI Governance Committee within five (5) business days of any system suspension.

### 4. Quality Assurance

4.1. The organization shall implement quality assurance protocols for AI outputs, including random sampling and expert review of AI-generated recommendations, predictions, or classifications. Sample size and frequency shall be proportionate to the system's risk level and output volume.

4.2. AI outputs shall be periodically compared against expert professional judgment to assess alignment and identify systematic errors. Significant discrepancies shall be investigated and corrective action taken.

4.3. Error rates, including both false positives and false negatives, shall be tracked and documented for all AI systems. Error rate trends shall be reported in quarterly performance reports and evaluated against established tolerances.

4.4. When errors in AI outputs are identified, the responsible System Owner shall conduct a root cause analysis, implement corrective measures, and assess whether affected decisions or outputs require review or revision. Documentation of the error, root cause, and corrective action shall be maintained in the AI governance record.
"""
        },
        "medium": {
            "title": "Accuracy and Validation",
            "content": """
### 1. Policy Statement

This organization shall ensure that AI systems produce reliable, accurate results appropriate for their intended public health applications, through validation testing, ongoing monitoring, and quality assurance.

### 2. Requirements

2.1. All AI systems shall be tested and validated before deployment using data representative of the populations and conditions the system will serve. Performance benchmarks shall be established and documented for each system.

2.2. Deployed AI systems shall be monitored for ongoing performance on at least a quarterly basis. Performance metrics shall be compared against established benchmarks and any significant degradation investigated and corrected.

2.3. Quality assurance reviews, including random sampling of AI outputs and comparison against expert judgment, shall be conducted regularly for all AI systems used in decision-support or public-facing applications.

2.4. Error rates shall be tracked and documented. When errors are identified, the responsible staff member shall investigate the cause and implement corrective measures. Significant errors shall be reported to the AI governance lead.
"""
        },
        "low": {
            "title": "Accuracy",
            "content": """
### 1. Policy Statement

This organization shall ensure that AI systems produce accurate and reliable results appropriate to their intended use.

### 2. Requirements

2.1. AI systems shall be tested before operational use to verify that outputs are accurate and appropriate for the intended application.

2.2. Staff shall regularly check AI outputs for errors and shall not rely solely on AI-generated results for important decisions.

2.3. Accuracy concerns regarding any AI system shall be reported to the responsible supervisor and the AI governance lead for investigation and corrective action.
"""
        }
    },
    "Governance & Risk Management": {
        "high": {
            "title": "AI Governance and Risk Management",
            "content": """
### 1. Policy Statement

This organization shall establish and maintain a comprehensive governance framework for the oversight, management, and accountability of all AI systems, consistent with the NIST AI Risk Management Framework (AI RMF), OMB Memorandum M-24-10, and applicable state requirements. The governance framework shall include a defined organizational structure, risk classification methodology, tiered approval processes, and inventory management procedures to ensure that AI systems are deployed responsibly and in alignment with the organization's mission, values, and legal obligations.

### 2. Governance Structure

2.1. The organization shall establish an AI Governance Committee with cross-functional representation including, at minimum, senior leadership, information technology, legal counsel, privacy, equity, public health program staff, and procurement. The Committee shall have the authority to approve or deny high-risk AI deployments, establish organization-wide AI policies and standards, and direct corrective action when compliance issues arise.

2.2. The AI Governance Committee shall convene at least quarterly, with additional meetings as needed to address urgent matters. Meeting agendas, attendance records, and decisions shall be documented and retained in the AI governance record.

2.3. The organization shall designate an AI Governance Lead (or equivalent role) responsible for coordinating day-to-day AI governance activities, maintaining the AI System Inventory, supporting the AI Governance Committee, and serving as the primary point of contact for AI governance inquiries.

### 3. Risk Classification and Assessment

3.1. All proposed AI use cases shall undergo a risk assessment prior to approval. The assessment shall evaluate: (a) the sensitivity and classification of data involved; (b) the potential impact on individuals, communities, and public health outcomes; (c) the degree of autonomy in decision-making; (d) regulatory and legal implications; and (e) reputational and operational risks.

3.2. AI use cases shall be classified into risk tiers based on the assessment results: **High Risk** (systems affecting individual rights, health outcomes, enforcement, or resource allocation; systems processing PHI/PII; systems with significant equity implications); **Moderate Risk** (systems supporting internal operations, analytics, or workflow; systems processing de-identified or aggregate data); **Low Risk** (systems performing routine administrative tasks with no significant impact on individuals or public health outcomes).

3.3. The risk classification shall determine the level of review, approval, monitoring, and documentation required for each AI system, with higher-risk systems subject to more rigorous requirements at every stage.

### 4. Approval Processes

4.1. **Low-Risk AI use cases** may be approved by the immediate supervisor and the AI Governance Lead, with documentation submitted to the AI Governance Committee for informational purposes.

4.2. **Moderate-Risk AI use cases** shall require review and approval by the AI Governance Lead and at least one additional functional reviewer (e.g., Privacy Officer, IT Security, Equity Officer), with notification to the AI Governance Committee.

4.3. **High-Risk AI use cases** shall require full review by the AI Governance Committee, including technical review, legal and privacy assessment, equity impact assessment, and documented approval or denial with rationale. No high-risk AI system shall be deployed without AI Governance Committee approval.

4.4. All approval decisions shall be documented, including the risk classification, reviewers involved, conditions or limitations imposed, and the date of authorization. Approval records shall be retained in the AI governance record.

### 5. AI System Inventory

5.1. The AI Governance Lead shall maintain a comprehensive inventory of all AI systems in use, under development, or under evaluation by the organization. The inventory shall record: system name, vendor, purpose, risk classification, data processed, System Owner, deployment date, last review date, and current status.

5.2. The inventory shall be reviewed and reconciled at least semi-annually to ensure completeness and accuracy. System Owners shall be responsible for reporting changes in system status, scope, or configuration to the AI Governance Lead within ten (10) business days.

5.3. AI systems that are no longer in use shall be formally decommissioned through a documented process that includes data disposition, access revocation, vendor notification, and removal from the inventory.

5.4. Changes to existing AI systems, including model updates, data source changes, or scope modifications, shall be subject to a change management process proportionate to the system's risk classification.
"""
        },
        "medium": {
            "title": "Governance and Risk Management",
            "content": """
### 1. Policy Statement

This organization shall maintain governance oversight and risk management processes for all AI systems, ensuring that AI deployments are authorized, appropriate, and managed throughout their lifecycle.

### 2. Requirements

2.1. Governance oversight for AI systems shall be provided by designated leadership, which may include an AI Governance Committee, a designated AI governance lead, or integration into existing governance structures.

2.2. All new AI use cases shall undergo a risk assessment prior to deployment. The assessment shall consider the sensitivity of data involved, the potential impact on individuals and communities, and the regulatory implications. Use cases shall be classified as high, moderate, or low risk, with higher-risk applications subject to additional review and approval requirements.

2.3. An approval process shall be established for new AI tools and use cases, with review requirements proportionate to the assessed risk level. High-risk use cases shall require senior leadership or committee approval.

2.4. The organization shall maintain an inventory of all AI systems in use, including system name, purpose, vendor, risk classification, and responsible staff member. The inventory shall be updated at least annually.
"""
        },
        "low": {
            "title": "Governance",
            "content": """
### 1. Policy Statement

This organization shall provide appropriate oversight and governance for the use of AI systems.

### 2. Requirements

2.1. Staff shall obtain leadership approval before deploying new AI tools or systems for organizational use. Approval requests shall describe the intended purpose, data involved, and expected benefits.

2.2. The organization shall maintain a record of all AI systems in use, including the system name, purpose, and responsible staff member.

2.3. Staff shall assess the risks associated with each AI application before use, considering data sensitivity, potential impacts, and regulatory requirements, and shall escalate concerns to their supervisor.
"""
        }
    },
    "Training & Capacity Building": {
        "high": {
            "title": "AI Training and Workforce Capacity Building",
            "content": """
### 1. Policy Statement

This organization shall invest in the development of workforce capacity to use AI systems effectively, responsibly, and in compliance with organizational policies. The organization recognizes that the responsible use of AI requires a baseline of AI literacy across the workforce, specialized competencies for staff who develop or directly operate AI systems, and ongoing professional development to keep pace with a rapidly evolving technology landscape.

### 2. AI Literacy Program

2.1. All staff shall complete a baseline AI literacy module within ninety (90) calendar days of the effective date of this policy and within thirty (30) calendar days of onboarding for new staff. The baseline module shall cover: (a) what AI is and how it works in general terms; (b) the types of AI systems used by the organization; (c) key risks including bias, privacy, and accuracy; (d) staff obligations under this policy; and (e) how to report concerns about AI systems.

2.2. Staff who directly use AI systems in their work shall complete role-specific training on the particular systems they operate, including their capabilities, limitations, proper use, data handling requirements, and procedures for escalating concerns. Role-specific training shall be completed before the staff member is granted access to the AI system.

2.3. Staff with responsibilities for AI system development, procurement, deployment, or governance shall complete advanced training covering risk assessment, equity impact analysis, vendor evaluation, performance monitoring, and regulatory compliance. Advanced training shall be completed within sixty (60) calendar days of assignment to such responsibilities.

2.4. All AI training shall be refreshed annually. The AI Governance Lead shall update training content at least annually to reflect changes in technology, policy, regulation, and lessons learned.

### 3. Competency Assessment

3.1. Staff shall demonstrate competency through assessment before being granted access to AI systems processing Level 3 or Level 4 data or classified as high-risk. Competency assessments may include written tests, practical demonstrations, or supervisory evaluation.

3.2. The organization shall track training completion and competency assessment results through its learning management system or equivalent record. Reports on training compliance shall be provided to the AI Governance Committee quarterly.

3.3. Supervisors shall incorporate AI competency into annual performance evaluations for staff whose roles involve significant AI use, including assessment of adherence to this policy, appropriate use of AI tools, and professional judgment in evaluating AI outputs.

### 4. Knowledge Management and Continuous Learning

4.1. The organization shall maintain a central repository of AI resources, including this policy, training materials, approved use case guides, best practices, vendor documentation, and frequently asked questions. The repository shall be accessible to all staff through the organization's intranet or equivalent platform.

4.2. The organization shall encourage knowledge sharing through periodic forums, communities of practice, or working groups focused on AI use in public health. Lessons learned from AI deployments shall be documented and shared to improve organizational practice.

4.3. The organization shall monitor developments in AI technology, regulation, and best practices, and shall incorporate relevant developments into its training and guidance materials on a timely basis.
"""
        },
        "medium": {
            "title": "Training and Capacity Building",
            "content": """
### 1. Policy Statement

This organization shall ensure that staff have the knowledge and skills necessary to use AI systems effectively and in compliance with this policy. Training shall be provided to all staff who use AI tools and shall be updated regularly.

### 2. Requirements

2.1. All staff who use AI tools shall complete AI training within sixty (60) calendar days of assignment and annually thereafter. Training shall cover AI capabilities and limitations, data privacy requirements, bias awareness, and staff obligations under this policy.

2.2. The organization shall maintain training documentation and track completion. Training records shall be available for review by management and the AI governance lead.

2.3. The organization shall provide resources for staff to learn about AI, including access to guidance documents, approved use case examples, and vendor documentation.

2.4. The organization shall support ongoing professional development in AI for interested staff, including relevant conferences, webinars, and professional association resources.
"""
        },
        "low": {
            "title": "Training",
            "content": """
### 1. Policy Statement

This organization shall provide training to staff on the appropriate use of AI systems.

### 2. Requirements

2.1. Staff who use AI tools shall receive basic training on proper use, data privacy requirements, and this organization's AI policies before being granted system access.

2.2. Training materials shall be maintained and made available to all staff through the organization's standard training platforms.

2.3. The organization shall provide ongoing learning opportunities as AI technologies and organizational practices evolve, including updates to training materials when this policy is revised.
"""
        }
    },
    "Use Case Appropriateness": {
        "high": {
            "title": "AI Use Case Appropriateness and Boundaries",
            "content": """
### 1. Policy Statement

This organization shall establish clear criteria for appropriate and inappropriate uses of AI systems and shall maintain defined boundaries and guardrails to ensure that AI is applied only in contexts where its use is suitable, proportionate, and consistent with the organization's mission, values, and legal obligations. All proposed AI use cases shall be evaluated against these criteria before deployment.

### 2. Permitted Uses

2.1. AI systems may be used for purposes that advance the organization's public health mission, provided the use case has been assessed and approved in accordance with the organization's AI governance and risk management procedures. Categories of generally permitted uses include: (a) drafting and editing of internal documents, communications, and reports using de-identified or non-sensitive data; (b) analysis of aggregate, de-identified, or publicly available data for epidemiological, programmatic, or operational purposes; (c) literature review, research synthesis, and knowledge management support; (d) administrative workflow automation, including scheduling, form processing, and correspondence management; and (e) translation and plain-language simplification of public communications.

2.2. The AI Governance Committee shall maintain and periodically update a list of pre-approved use case categories for which staff may use AI tools without additional case-by-case approval, subject to compliance with all other provisions of this policy.

### 3. Prohibited Uses

3.1. The following uses of AI are prohibited without exception: (a) entry of PHI, PII, or data classified as confidential or restricted into any External AI System; (b) autonomous AI decision-making on matters affecting individual rights, benefits, health services, enforcement actions, or resource allocation without human review and approval; (c) use of AI for mass surveillance, social scoring, or profiling of individuals based on protected characteristics; (d) creation of deepfakes or synthetic media representing real individuals without their informed written consent; (e) use of AI to generate or disseminate false, misleading, or deceptive public health information; and (f) any use that violates federal, state, or local law, including civil rights protections.

3.2. Staff who are uncertain whether a proposed use is permitted shall consult with their supervisor and the AI Governance Lead before proceeding. Uncertainty shall be resolved in favor of caution.

### 4. Use Case Review Process

4.1. Proposed AI use cases not covered by pre-approved categories shall be submitted for review through the organization's AI Use Case Request process. The review shall evaluate the appropriateness of the proposed use against the criteria in this section, the risk classification, data requirements, equity implications, and expected benefits.

4.2. Use case review decisions shall be documented, including the rationale for approval or denial. Denied use cases may be appealed to the AI Governance Committee.

4.3. Approved use cases shall be subject to periodic review, at least annually, to confirm continued appropriateness given changes in technology, regulation, organizational context, or community needs.
"""
        },
        "medium": {
            "title": "Use Case Appropriateness",
            "content": """
### 1. Policy Statement

This organization shall define appropriate and inappropriate uses of AI systems and shall require review of new AI use cases before deployment to ensure they are suitable, proportionate, and consistent with the organization's mission and legal obligations.

### 2. Requirements

2.1. The organization shall define categories of appropriate AI uses (e.g., data analysis, document drafting, administrative automation) and prohibited uses (e.g., entry of PHI into external AI tools, autonomous high-stakes decisions, surveillance, deepfake creation). These categories shall be documented and communicated to all staff.

2.2. Proposed AI use cases that fall outside pre-approved categories shall be reviewed and approved through the organization's AI governance process before deployment.

2.3. Staff who are uncertain whether a proposed use is appropriate shall consult with their supervisor or the AI governance lead before proceeding.

2.4. Approved use cases shall be reviewed periodically, at least annually, to confirm continued appropriateness.
"""
        },
        "low": {
            "title": "Use Case Review",
            "content": """
### 1. Policy Statement

This organization shall ensure that AI systems are used for appropriate purposes consistent with its public health mission and legal obligations.

### 2. Requirements

2.1. Staff shall consider whether AI is an appropriate tool for the task at hand before using it, and shall not use AI in ways that could compromise data privacy, civil rights, or public trust.

2.2. Uses of AI that are prohibited include entry of sensitive data into external AI tools, autonomous decision-making on matters affecting individuals, and creation of misleading content.

2.3. Staff shall seek supervisor approval before using AI for novel or sensitive applications not previously reviewed by the organization.
"""
        }
    },
    "Procurement & Vendor Management": {
        "high": {
            "title": "AI Procurement and Vendor Management",
            "content": """
### 1. Policy Statement

This organization shall ensure that all AI systems acquired from external vendors meet the organization's standards for security, privacy, equity, transparency, accuracy, and compliance. The procurement process for AI systems shall include structured vendor assessment, AI-specific contract provisions, and ongoing vendor performance management throughout the contract lifecycle.

### 2. Vendor Assessment

2.1. Prior to procurement of any AI system, the organization shall conduct a vendor assessment evaluating: (a) the vendor's data handling practices, including data storage location, encryption, access controls, and incident response procedures; (b) the vendor's security posture, including current SOC 2 Type II, HITRUST, FedRAMP, or equivalent certification; (c) the vendor's bias testing and equity practices, including whether fairness testing has been conducted and results disclosed; (d) the vendor's transparency practices, including the availability of model documentation, data source descriptions, and performance metrics; and (e) the vendor's financial stability and organizational viability.

2.2. Vendors of high-risk AI systems shall provide, upon request: (a) detailed model documentation or Model Cards; (b) bias testing results disaggregated by demographic categories; (c) descriptions of training data sources and composition; (d) evidence of independent third-party audit or review; and (e) references from comparable government or public health customers.

### 3. Contract Requirements

3.1. All contracts for AI systems shall include provisions addressing: (a) ownership and control of organizational data, including the prohibition on vendor use of organizational data for model training or improvement without explicit written consent; (b) data handling, storage, and disposal requirements consistent with organizational policy and applicable law; (c) the organization's right to audit the vendor's data practices, security controls, and system performance; (d) transparency requirements, including the obligation to disclose material changes to the AI model, data sources, or system functionality; (e) performance standards, including accuracy benchmarks, uptime requirements, and service level agreements; (f) compliance with applicable laws and regulations, including HIPAA where relevant; (g) indemnification, liability, and insurance provisions; and (h) termination rights, including data portability and return/destruction of organizational data upon contract termination.

3.2. The organization's legal counsel shall review all AI procurement contracts prior to execution to ensure that AI-specific provisions are adequate and enforceable.

### 4. Ongoing Vendor Management

4.1. The responsible System Owner shall conduct or coordinate vendor performance reviews at least annually for moderate-risk AI systems and semi-annually for high-risk AI systems. Reviews shall assess: compliance with contractual requirements, system performance against benchmarks, security incident history, responsiveness to support requests, and vendor cooperation with transparency and audit requirements.

4.2. Vendors shall be required to notify the organization within forty-eight (48) hours of any security incident, data breach, material system malfunction, or significant change to the AI model that could affect system performance, accuracy, or fairness.

4.3. AI procurement contracts shall be subject to formal renewal assessment, including updated vendor evaluation, prior to extension or renewal.
"""
        },
        "medium": {
            "title": "Procurement and Vendor Management",
            "content": """
### 1. Policy Statement

This organization shall manage the procurement and ongoing oversight of AI vendors to ensure that AI products and services meet organizational standards for security, privacy, equity, and performance.

### 2. Requirements

2.1. The organization shall assess AI vendors prior to procurement, including evaluation of security certifications, data handling practices, bias testing, and transparency disclosures. High-risk AI procurements shall include legal and privacy review.

2.2. AI procurement contracts shall include provisions addressing data ownership, data handling and disposal, audit rights, performance standards, compliance with applicable laws, disclosure of material system changes, and termination and data return.

2.3. The responsible staff member shall monitor vendor performance against contractual requirements on at least an annual basis.

2.4. Vendors shall be required to notify the organization promptly of any security incident, data breach, or material change to the AI system.
"""
        },
        "low": {
            "title": "Procurement",
            "content": """
### 1. Policy Statement

This organization shall procure AI tools and services responsibly, ensuring that vendors meet basic standards for security, privacy, and performance.

### 2. Requirements

2.1. Staff shall evaluate AI vendors before procurement, considering the vendor's security practices, data handling policies, and reputation. Procurement of AI tools shall follow the organization's standard procurement procedures.

2.2. Contracts for AI tools shall include relevant terms addressing data ownership, data handling, compliance with applicable laws, and the organization's right to terminate.

2.3. Staff shall monitor the performance and reliability of AI vendor products during the contract term and report concerns to their supervisor and the procurement lead.
"""
        }
    },
    "Legal & Regulatory Compliance": {
        "high": {
            "title": "Legal and Regulatory Compliance",
            "content": """
### 1. Policy Statement

This organization shall ensure that all AI activities comply with applicable federal, state, and local laws, regulations, and legal requirements. The organization shall proactively monitor the evolving regulatory landscape for AI and shall maintain compliance with all applicable requirements, including but not limited to health information privacy laws, civil rights protections, public records requirements, procurement regulations, and emerging AI-specific legislation.

### 2. Regulatory Compliance Framework

2.1. All AI systems and AI-related activities shall comply with applicable federal laws and regulations, including but not limited to: HIPAA (45 C.F.R. Parts 160 and 164); the Privacy Act of 1974 (5 U.S.C. Section 552a); Title VI of the Civil Rights Act of 1964; Section 504 of the Rehabilitation Act; the Americans with Disabilities Act; the Age Discrimination Act of 1975; Executive Order 14110 on Safe, Secure, and Trustworthy AI; and OMB Memorandum M-24-10 on Advancing Governance, Innovation, and Risk Management for Agency Use of AI.

2.2. All AI systems and activities shall comply with applicable state and local laws, including state health information privacy statutes, state AI-specific legislation, state procurement requirements, and local ordinances governing technology use by government agencies.

2.3. The organization shall conduct regulatory compliance assessments for all high-risk AI use cases prior to deployment, and shall update compliance assessments when material changes occur in applicable law or regulation.

### 3. Civil Rights Protection

3.1. No AI system shall be used in a manner that results in unlawful discrimination based on race, color, national origin, sex, age, disability, religion, or any other characteristic protected by federal, state, or local law.

3.2. The organization shall ensure that AI systems used in public-facing services comply with accessibility requirements under Section 508 of the Rehabilitation Act, Title II of the ADA, and applicable state accessibility laws.

3.3. Due process protections shall apply to all AI-assisted decisions that affect individual rights, benefits, or services. Individuals shall have the right to notice, explanation, and review of such decisions as established in the Human Oversight section of this policy.

### 4. Legal Review and Monitoring

4.1. Legal counsel shall review all high-risk AI use cases, AI procurement contracts, and AI-related policies prior to finalization. Legal review shall address compliance with applicable laws, liability considerations, intellectual property implications, and regulatory obligations.

4.2. The organization shall monitor federal, state, and local legislative and regulatory developments related to AI on an ongoing basis. The AI Governance Lead, in coordination with legal counsel, shall evaluate the impact of new or proposed requirements on organizational AI practices and shall recommend policy updates as needed.

4.3. The organization shall maintain documentation of legal compliance assessments, legal reviews, and regulatory change analyses in the AI governance record.
"""
        },
        "medium": {
            "title": "Legal and Regulatory Compliance",
            "content": """
### 1. Policy Statement

This organization shall comply with all applicable federal, state, and local laws and regulations in its use of AI systems, including health information privacy laws, civil rights protections, and any applicable AI-specific legislation.

### 2. Requirements

2.1. All AI systems and activities shall comply with applicable laws and regulations, including HIPAA, civil rights laws, accessibility requirements, and state AI legislation. Staff shall not use AI in ways that violate applicable law.

2.2. The organization shall protect civil rights in its use of AI, including compliance with non-discrimination requirements, accessibility standards, and due process protections for individuals affected by AI-assisted decisions.

2.3. Legal counsel shall review high-risk AI use cases and AI procurement contracts prior to finalization to assess compliance and liability implications.

2.4. The AI governance lead shall monitor federal, state, and local regulatory developments related to AI and recommend policy updates as needed.
"""
        },
        "low": {
            "title": "Legal Compliance",
            "content": """
### 1. Policy Statement

This organization shall comply with applicable federal, state, and local laws and regulations in its use of AI systems.

### 2. Requirements

2.1. Staff shall not use AI systems in ways that violate applicable laws, including health information privacy laws, civil rights protections, or other legal requirements.

2.2. Staff shall protect individual rights when using AI, including non-discrimination, accessibility, and due process.

2.3. Staff shall seek guidance from legal counsel when uncertain about the legal implications of a proposed AI use.
"""
        }
    },
    "Community Engagement": {
        "high": {
            "title": "Community Engagement and Stakeholder Participation",
            "content": """
### 1. Policy Statement

This organization is committed to meaningful community engagement in AI governance, recognizing that public trust is essential to the effective use of AI in public health and that the communities served by this organization have a right to participate in decisions about technologies that may affect them. The organization shall provide opportunities for community input, ensure accessible communication about AI activities, and demonstrate responsiveness to community concerns.

### 2. Public Participation

2.1. The organization shall provide structured opportunities for community input on major AI initiatives, including new deployments of AI systems that directly affect public-facing services, changes to AI systems that materially alter their impact on community members, and development or revision of AI governance policies. Input opportunities may include public comment periods, community forums, focus groups, surveys, or advisory committee participation.

2.2. For AI systems with significant community impact, the organization shall conduct stakeholder consultation with affected communities, including populations that have historically been underserved, marginalized, or disproportionately affected by health disparities. Consultation shall be conducted in accessible venues, languages, and formats.

2.3. The organization shall consider establishing a Community AI Advisory Panel, comprising community members, patient advocates, civil rights representatives, and technical experts, to provide ongoing input on AI governance and deployment decisions. Panel recommendations shall be documented and considered by the AI Governance Committee.

### 3. Public Communication

3.1. The organization shall proactively communicate with the public about its AI activities through accessible channels, including the organization's website, social media, newsletters, and community events. Communications shall use plain language and shall be available in the languages most commonly spoken in the jurisdiction.

3.2. The organization shall respond to community inquiries and concerns about AI systems in a timely manner. Initial acknowledgment shall be provided within five (5) business days, and a substantive response within thirty (30) calendar days.

3.3. The organization shall publish regular updates on its AI activities, including new deployments, policy changes, and outcomes of community engagement activities.

### 4. Trust Building and Accountability

4.1. The organization shall demonstrate accountability to the community by publicly reporting on AI governance activities, including equity metrics, community feedback received, and organizational actions taken in response.

4.2. The organization shall address identified community concerns through concrete, documented actions and shall communicate the results of those actions to the concerned parties and the broader community.

4.3. The organization shall provide educational opportunities for community members to learn about AI capabilities, limitations, and the organization's AI practices, with the goal of building informed public engagement.
"""
        },
        "medium": {
            "title": "Community Engagement",
            "content": """
### 1. Policy Statement

This organization shall engage community stakeholders in AI governance to build public trust and ensure that AI systems serve community needs. The organization shall seek community input on significant AI initiatives and communicate transparently about AI activities.

### 2. Requirements

2.1. The organization shall seek community input on major AI initiatives that affect public-facing services. Input may be gathered through public comment periods, community forums, surveys, or other accessible mechanisms.

2.2. The organization shall communicate with the public about its AI activities in plain language through accessible channels. Community inquiries and concerns shall be acknowledged and addressed in a timely manner.

2.3. The organization shall demonstrate accountability by reporting publicly on AI governance activities, community feedback received, and actions taken in response.

2.4. The organization shall provide opportunities for community members to learn about AI and its role in the organization's public health work.
"""
        },
        "low": {
            "title": "Community Input",
            "content": """
### 1. Policy Statement

This organization shall consider community perspectives in its use of AI systems and shall communicate with the public about AI activities.

### 2. Requirements

2.1. The organization shall seek community input when deploying AI systems that significantly affect public services, through mechanisms appropriate to the scope and impact of the deployment.

2.2. The organization shall communicate with the public about its use of AI through its standard public communications channels.

2.3. Staff shall respond to community concerns about AI in a timely and transparent manner and shall escalate significant concerns to the AI governance lead.
"""
        }
    },
    "Sustainability & Evaluation": {
        "high": {
            "title": "Sustainability, Evaluation, and Continuous Improvement",
            "content": """
### 1. Policy Statement

This organization shall ensure the long-term sustainability of its AI program through systematic evaluation, resource planning, and continuous improvement. AI systems shall be regularly assessed against defined metrics to determine whether they are achieving their intended purpose, delivering value proportionate to their cost and risk, and remaining aligned with the organization's evolving mission and priorities.

### 2. Evaluation Framework

2.1. The organization shall establish measurable success criteria for each AI system at the time of deployment, including quantitative performance metrics (e.g., accuracy, throughput, error rate reduction) and qualitative indicators (e.g., user satisfaction, workflow improvement, service quality). Success criteria shall be documented in the system's deployment record.

2.2. Each AI system shall be formally evaluated against its success criteria at least annually. The evaluation shall be conducted by the responsible System Owner and shall include: (a) comparison of actual performance against established metrics; (b) assessment of whether the system continues to address its intended use case effectively; (c) cost-benefit analysis, including direct costs (licensing, infrastructure, staff time), indirect costs (training, governance overhead), and measurable benefits; (d) assessment of continued compliance with this policy; and (e) input from system users and affected stakeholders.

2.3. Evaluation results shall be reported to the AI Governance Committee. Systems that fail to meet success criteria or that no longer provide benefit proportionate to cost and risk shall be referred for remediation, modification, or decommissioning.

### 3. Continuous Improvement

3.1. The organization shall implement a structured lessons-learned process for AI deployments. After each significant AI deployment, modification, or incident, the responsible team shall document: (a) what was planned versus what occurred; (b) what worked well; (c) what did not work as expected; (d) root causes of any problems; and (e) recommendations for future practice. Lessons learned shall be shared with the AI Governance Committee and incorporated into organizational guidance.

3.2. This policy, along with all associated procedures and guidance, shall be reviewed and updated at least annually by the AI Governance Lead in coordination with the AI Governance Committee. Updates shall reflect changes in technology, regulatory requirements, organizational priorities, lessons learned, and community feedback.

3.3. The organization shall monitor and adopt best practices from peer organizations, professional associations, federal guidance, and academic research to improve its AI governance and operational practices.

### 4. Sustainability and Resource Planning

4.1. The organization shall plan for the long-term resource requirements of its AI program, including staff, training, technology infrastructure, vendor contracts, and governance activities. Resource requirements shall be incorporated into the organization's budget planning cycle.

4.2. The organization shall develop and maintain a workforce development pipeline for AI-related competencies, including identification of critical skills, succession planning for key AI governance roles, and professional development pathways.

4.3. The AI Governance Committee shall prepare an annual AI program summary for senior leadership, including an assessment of program maturity, resource adequacy, key accomplishments, challenges, and recommendations for the coming year.
"""
        },
        "medium": {
            "title": "Sustainability and Evaluation",
            "content": """
### 1. Policy Statement

This organization shall evaluate the effectiveness and sustainability of its AI systems to ensure they continue to serve the organization's public health mission and provide value proportionate to their cost and risk.

### 2. Requirements

2.1. Each AI system shall be evaluated against defined success criteria at least annually. Evaluations shall assess system performance, cost-benefit, continued appropriateness, and compliance with this policy.

2.2. The organization shall plan for long-term sustainability of its AI program, including budget, staffing, training, and technology infrastructure needs, as part of its standard planning and budget processes.

2.3. The organization shall implement continuous improvement practices for AI, including documentation of lessons learned, regular policy updates, and adoption of emerging best practices.

2.4. This policy shall be reviewed and updated at least annually to reflect changes in technology, regulation, and organizational priorities.
"""
        },
        "low": {
            "title": "Evaluation",
            "content": """
### 1. Policy Statement

This organization shall evaluate the effectiveness of its AI systems to ensure they continue to serve their intended purpose and provide appropriate value.

### 2. Requirements

2.1. Staff shall periodically assess the results and usefulness of AI systems they use and report findings to their supervisor. Systems that are ineffective or no longer needed shall be flagged for review.

2.2. The organization shall incorporate lessons learned from AI use into its ongoing practices and shall update this policy as needed to reflect experience and changing circumstances.

2.3. The organization shall plan for the sustainability of AI initiatives, including consideration of ongoing costs, staff capacity, and technology requirements.
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
