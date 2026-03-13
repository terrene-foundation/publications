# CARE: A Core Thesis

**Collaborative Autonomous Reflective Enterprise**

_The Constrained Organization as Governance Architecture for Enterprise AI_

_Doing Better Things, Not Just Doing Things Better_

**Author**: Dr. Jack Hong, Singapore Management University

**Version**: 2.1 | March 2026

**License**: CC BY 4.0

---

## Abstract

Enterprise AI governance faces a structural dilemma: requiring human approval for every AI action defeats the purpose of autonomy, while removing human accountability creates unacceptable risk. This paper proposes the Constrained Organization---a new organizational form built on three interconnected concepts. The Dual Plane Model separates trust (accountability, values, authority---permanently human) from execution (task completion, coordination---shared with AI). The Mirror Thesis argues that building AI capable of executing organizational roles creates a diagnostic that reveals uniquely human contributions previously entangled with task execution. Human-on-the-Loop positions humans as envelope definers rather than approval bottlenecks. The architecture is operationalized through the Enterprise Agent Trust Protocol (EATP) for cryptographically verifiable trust lineage and Cognitive Orchestration (CO) for structured institutional knowledge. A case study of the Terrene Foundation---a Singapore standards body whose knowledge base operations are run by AI agents within constitutional constraints---demonstrates the model in practice. Explicit falsification conditions are stated and limitations including constraint gaming, power asymmetries, and the circularity of defining human value through a human-designed framework are analyzed.

---

## Disclosure

I developed CARE and built the Kailash platform that implements it. The entire Kailash stack (Core SDK, DataFlow, Kaizen, Nexus) is released under the Apache 2.0 open-source license. In practical terms, this means the source code is publicly available, and anyone is legally entitled to use it, modify it, build commercial products with it, and compete with me - permanently and irrevocably. This cannot be taken back.

Two patents have been filed: PCT/SG2024/050503 for workflow orchestration (with favorable International Preliminary Report on Patentability, all 18 claims) and P251088SG as a provisional filing. Under Apache 2.0 Section 3, all users of the licensed code receive a perpetual, worldwide, royalty-free patent license, with defensive termination if a user initiates patent litigation. All open-source IP has been fully and irrevocably transferred to the Terrene Foundation. Contributors retain their own copyright and grant an Apache 2.0 license.

No independent party has validated the claims in this paper. There has been no academic peer review. Cross-cultural testing and deployment at scale is in progress. The six competency categories are based on my analysis, informed by established research, not on independent empirical study.

---

## Part I: The Question Enterprise AI Prefers to Avoid

What is the human actually for?

Every enterprise deploying AI will face this question. Most prefer not to ask it directly. The evasions are familiar:

"Humans approve AI outputs." This is the human-in-the-loop answer, and it sounds responsible until you watch it in practice. A compliance officer reviewing two hundred AI-generated assessments per day is not exercising judgment. They are rubber-stamping. The human-in-the-loop becomes a human-shaped bottleneck who provides the appearance of oversight without its substance.

"AI operates autonomously." This is the human-out-of-the-loop answer, and it sounds efficient until something goes wrong. When an autonomous agent makes a decision that harms a customer, violates a regulation, or contradicts organizational values, "the AI did it" is not an answer that satisfies boards, regulators, or courts. Accountability requires a human who made decisions, about boundaries, about authority, about values, that led to the outcome.

Both treat humans as components in a system rather than as the source of the system's authority and purpose.

CARE proposes a third path built on a central insight: **Trust is human. Execution is shared. The system reveals what only humans can provide.**

This paper presents that insight, subjects it to the strongest objections I can find, specifies conditions under which it should be abandoned, and is honest about what remains unproven. It is written for practitioners who need to make decisions about AI governance now, not after the academic consensus emerges.

---

## Part II: The Governance Dilemma

The dilemma is structural: traditional governance assumes a human made the decision. Every audit framework, every compliance system, every accountability structure presupposes human agency at the point of decision. AI breaks this assumption. Requiring human approval for every AI action defeats the purpose of autonomy. Removing human accountability creates unacceptable risk. Both paths fail.

Three pressures make this urgent: AI capability is advancing faster than governance frameworks. Economic competition punishes organizations that do not capture AI's productivity gains. And the human stakes are high. How organizations answer "what is the human for?" determines whether AI elevates human contribution or displaces it.

This paper is about doing better things: building institutional approaches to AI that drive economic value while preserving what matters about human work. Not doing things better. Not faster processing or cheaper operations. The governance choices organizations make now will be difficult to reverse.

### Existing Governance Frameworks

Multiple frameworks address aspects of AI governance, but none provides the architectural pattern for how to structure the human-AI relationship at the organizational level.

The **EU AI Act** (2024) mandates human oversight for high-risk AI systems (Article 14) but specifies the legal requirement, not the organizational architecture. The **NIST AI Risk Management Framework** (2023) provides a process model (GOVERN, MAP, MEASURE, MANAGE) that is deliberately agnostic about governance structure. The **OECD AI Principles** (2019, updated 2024) establish value-based principles across 47 adherent countries but note the persistent gap between principles and implementation. The **Singapore Model AI Governance Framework** (IMDA, 2020) provides practical organizational guidance but does not prescribe the human-AI relationship architecture.

Jobin, Ienca, and Vayena (2019) analyzed 84 AI ethics guidelines worldwide and found convergence on principles (transparency, fairness, non-maleficence, responsibility, privacy) but divergence on implementation. Hagendorff (2020) identified a "deep gap" between abstract ethics principles and technical practice. Floridi and Cowls (2019) synthesized five principles from global AI ethics documents, demonstrating convergence but acknowledging the implementation challenge. CARE attempts to address this implementation gap by providing governance _architecture_, not additional principles.

### Levels of Automation and Human Control

The relationship between human control and automation has been studied extensively. Sheridan and Verplank (1978) established the foundational 10-level taxonomy from full human control to full automation. Parasuraman, Sheridan, and Wickens (2000) extended this to a two-dimensional model across four information-processing stages. Bainbridge (1983) documented the ironies of automation: the more automated a system, the more critical (and degraded) the remaining human skills become.

Santoni de Sio and van den Hoven (2018) argued for "meaningful human control" based on tracking (system responds to reasons) and tracing (actions trace to responsible agents). Methnani, Aler Tubella, and Dignum (2021) demonstrated that variable autonomy levels improve both system performance and human control. Shneiderman (2022) proposed that high automation and high human control are simultaneously achievable---a position CARE shares but operationalizes differently through the Dual Plane Model.

### Organizational Theory and AI

Sociotechnical systems theory (Trist & Bamforth, 1951; Emery & Trist, 1960) established that organizations are joint human-technical systems requiring joint optimization. CARE's Dual Plane Model is a descendant of this tradition, adapted for AI agents as the technical component. Humberd and Latham (2026) recently used agency theory to analyze when AI achieves sufficient autonomy to be considered "an agent of the firm"---asking the theoretical question that CARE answers architecturally. Kolbjornsrud (2024) proposed six principles for designing intelligent organizations but did not define a new organizational form. Kellogg, Valentine, and Christin (2020) documented algorithmic management---algorithms managing human workers---which CARE inverts: humans managing AI through architectural constraints.

Rahwan (2018) extended human-in-the-loop to society-in-the-loop, proposing democratic governance of AI systems. This identifies a genuine gap in CARE: the framework assumes organizational values are given, not how they are democratically determined.

### Comparison with Existing Frameworks

| Dimension       | EU AI Act                | NIST AI RMF         | OECD Principles     | Shneiderman HCAI   | **CARE**                            |
| --------------- | ------------------------ | ------------------- | ------------------- | ------------------ | ----------------------------------- |
| Scope           | Regulatory compliance    | Risk management     | Ethical principles  | Design philosophy  | Organizational architecture         |
| Human role      | Oversight provider       | Risk assessor       | Values setter       | Co-equal partner   | Trust Plane architect               |
| Trust model     | Regulatory certification | Risk categorization | Principled trust    | Bilateral          | Cryptographically verifiable        |
| Enforcement     | Legal (fines)            | Voluntary           | Voluntary           | None               | Deterministic (guardrails)          |
| Knowledge model | Static documentation     | Framework documents | Principle documents | Academic framework | Compounding institutional knowledge |
| Falsifiable?    | N/A                      | No                  | No                  | No                 | Yes (5 criteria stated)             |

---

## Part III: The Third Path

### The Dual Plane Model

I propose treating organizations as operating on two conceptually separable planes.

The **Trust Plane** contains accountability, authority delegation, values, and boundaries. It is permanently human, not because AI could never participate in trust relationships, but because treating it as human preserves accountability in ways that alternative framings do not. When something goes wrong, the trust plane tells you which human defined the boundaries that permitted the outcome.

The **Execution Plane** contains task completion, information processing, and coordination. It can be shared with AI operating within human-defined constraints.

This separation is a normative choice, not an ontological discovery. Some organizational theorists argue that trust and execution are fundamentally entangled, and they may be right at the deepest level. I accept this critique and contend the separation is useful for governance design. By treating trust and execution as if they were separable, we can build systems that preserve human authority over boundaries while enabling machine-speed execution. The separation may be imperfect in practice, but it operationalizes a working approximation that current alternatives do not provide.

This separation pattern has prior art: software-defined networking separates control planes from data planes; Kubernetes separates orchestration from execution; aviation separates flight planning from autopilot operation (Bainbridge, 1983). Industry analysts have converged on "control plane" language for agentic AI governance (Forrester, O'Reilly, 2025-2026). What is new is applying the pattern to organizational governance as a formal architectural model with a companion trust verification protocol.

Traditional systems conflate these planes, forcing humans to approve every execution step as a proxy for trust. CARE separates them: humans invest judgment at setup time, enabling AI to execute at machine speed while accountability is preserved through a verifiable trust chain.

### Human-on-the-Loop

The term "human-on-the-loop" comes from the military autonomous systems literature, where it describes supervisory control of autonomous vehicles and weapons. I apply it to enterprise AI governance, adapting it from its origins.

The model works like this:

- Humans define the operating envelope: what the AI may do, what it may not, what triggers escalation, what values apply
- AI executes within that envelope at machine speed
- Humans observe execution patterns, develop insight into where the envelope fits well and where it does not, and refine the boundaries
- The loop is continuous: observation produces refinement, refinement improves execution, improved execution generates new patterns to observe

The pilot analogy captures this precisely. A pilot does not hand-fly every inch of a transoceanic flight. The autopilot handles sustained cruise. The pilot sets the flight plan, monitors conditions, and takes manual control when judgment tells them the situation requires it. The pilot's value is in recognizing the moment when the autopilot's parameters no longer match reality.

Parasuraman and Riley (1997) documented what happens when this relationship breaks down: automation misuse, disuse, and abuse. Humans over-trust the automation and miss failures (misuse), under-trust it and create unnecessary bottlenecks (disuse), or designers implement it with little regard for the human operator's workload and authority (abuse). CARE's phased adoption model (observation before limited autonomy, limited autonomy before expanded) is designed to build the calibrated trust that avoids these failure modes.

**A critical caveat**: Defining effective constraints for complex AI behavior is difficult. Research on specification gaming and emergent behaviors suggests constraint definition may fail in ways humans cannot anticipate. Human-on-the-loop is aspirational architecture, not guaranteed control.

---

## Part IV: The Mirror Thesis

This is the most important, and most contestable, idea in the framework.

When you build an AI that can execute all the measurable tasks of a human role, something unexpected happens. You do not discover that the human is unnecessary. You discover, with startling clarity, what the human contributes beyond task execution.

Before AI, these contributions were invisible. Not because they were unimportant, but because they were entangled with execution in ways that made them impossible to separate. The account manager's relationship skill was inseparable from the proposals they drafted. The analyst's contextual wisdom was inseparable from the spreadsheets they maintained. The manager's ethical judgment was inseparable from the reports they wrote.

AI disentangles them. When AI handles proposals, spreadsheets, and reports, what remains is the judgment, the relationships, the wisdom, and suddenly these become visible as the actual source of value they always were.

### Six Categories of Human Competency

The mirror reveals six categories of human contribution that current AI systems cannot replicate. These categories apply concepts from research on tacit knowledge (Polanyi, 1966), social capital (Nahapiet & Ghoshal, 1998), naturalistic decision-making (Klein, 1998), and moral intuition (Haidt, 2001) to the question of human-AI differentiation, a domain none of these researchers addressed directly. The application is mine, and it requires empirical validation.

**Ethical Judgment**: The capacity to sense when technically correct is morally wrong. Not rule-following, as AI can follow rules. The integration of competing values, contextual understanding, and moral reasoning that leads a lending officer to decline a loan that meets all technical criteria because something about the situation feels ethically wrong. Haidt (2001) demonstrated that moral judgment operates largely through intuition rather than deliberation: a process that current AI architectures do not replicate.

**Relationship Capital**: Trust built through shared vulnerability and history. When stakes are high and the situation is ambiguous, clients call the human they have a relationship with. That capital, accumulated through years of navigating difficulty together, is not in any database.

**Contextual Wisdom**: Knowledge from lived experience that transcends available data. The executive who knows a board member will object to cost-savings framing because of an experience fifteen years ago recorded nowhere. Polanyi (1966) called this "tacit knowledge": we know more than we can tell. Nonaka (1994) described the organizational challenge of making such knowledge explicit.

**Creative Synthesis**: Evaluating and grounding novel solutions. AI excels at combinational creativity, rapidly recombining patterns within its vast training data to connect domains never connected before. What it cannot do is evaluate which of those syntheses actually make sense in practice, or make the genuinely transformational leap that reframes a problem entirely.

**Emotional Intelligence**: Reading rooms, sensing tension, responding to feeling with genuine care. AI can detect emotional signals in text. It does not feel them.

**Cultural Navigation**: Understanding unwritten rules and navigating between cultural contexts that data analysis alone cannot bridge.

### What the Mirror Does Not Claim

These are current AI limitations, not principled impossibilities. I am describing a snapshot, not a permanent boundary. Some of these categories may prove automatable. The competency map must be continuously reassessed as AI capability advances.

The mirror can also be misused. The same diagnostic that reveals uniquely human value can be used to identify roles for elimination rather than development. Management deploys the mirror onto workers, not the reverse. This creates power asymmetries that the framework prescribes safeguards for: worker consent, data transparency, democratic governance of mirror configuration; but cannot architecturally prevent. Organizations may choose to use the mirror well or badly. CARE provides the diagnostic; what organizations do with it is the most human decision of all.

### The Circularity Problem

I will address this directly because it is the strongest philosophical objection to the Mirror Thesis.

The thesis claims that AI execution reveals uniquely human value. But the categories of "uniquely human value" are defined by humans who already exhibit those capabilities. There is a circularity: we define human value as what the mirror shows, and the mirror shows what we defined as human value.

I accept this critique. The Mirror Thesis is not a derived conclusion from independent premises. It is closer to an axiom: an organizing principle that I adopt because it generates useful governance architecture, not because it can be proven from first principles. The justification is pragmatic: treating these six categories as the locus of human value produces better organizational outcomes than treating humans as interchangeable with AI or treating all human work as equally automatable.

If this axiom proves unproductive: if the categories cannot be reliably identified across deployments, or if organizations derive no benefit from investing in them, then the axiom should be abandoned. I specify the conditions for that abandonment in Part VIII.

---

## Part V: The Constrained Organization

The preceding sections describe individual components: a model for separating trust from execution (Dual Plane), a diagnostic for human contribution (Mirror Thesis), and a supervisory architecture (Human-on-the-Loop). This section argues that their integration produces something qualitatively different from an improved governance framework---it defines a new organizational form.

### Definition

A **constrained organization** is an enterprise where AI agents perform operational execution within cryptographically verifiable boundaries defined by human authority. It is characterized by five properties:

1. **Architectural separation**: Trust decisions are structurally separated from execution. This is not a policy choice but an infrastructure design.

2. **Verifiable trust lineage**: Every agent action can be traced, through a cryptographic chain, to the human authority that authorized it. The Enterprise Agent Trust Protocol (EATP) links five elements---Genesis Record, Delegation Record, Constraint Envelope, Capability Attestation, and Audit Anchor---into a cryptographically unforgeable (under standard cryptographic assumptions; see Hong, 2026b for formal specification) chain of accountability.

3. **Structured institutional knowledge**: AI agents operate with the organization's accumulated judgment, encoded in a five-layer architecture (Cognitive Orchestration): specialized agent roles, institutional knowledge base, architectural guardrails, structured workflows, and a learning system that compounds knowledge over time (Hong, 2026c).

4. **Graduated autonomy**: Five named trust postures---Pseudo-Agent, Supervised, Shared Planning, Continuous Insight, Delegated---provide a formal vocabulary for organizational risk appetite, with transitions governed by demonstrated performance. This extends the levels-of-automation tradition (Sheridan & Verplank, 1978; Parasuraman et al., 2000; Methnani et al., 2021) from per-task descriptions to organizational governance.

5. **Compounding knowledge**: Unlike stateless AI interactions that start from zero every session, the constrained organization accumulates institutional intelligence. Each successful interaction deepens the knowledge base. This operationalizes March's (1991) exploration-exploitation balance and Nonaka's (1994) knowledge creation theory for human-AI organizations.

### Relationship to Existing Organizational Forms

The constrained organization is distinct from every existing organizational form:

| Dimension          | Traditional Enterprise | AI-Assisted Enterprise     | DAO                       | Constrained Organization                  |
| ------------------ | ---------------------- | -------------------------- | ------------------------- | ----------------------------------------- |
| Human role         | Execute + decide       | Execute + decide; AI helps | Token-weighted governance | Define boundaries, values, accountability |
| AI role            | Tool                   | Augmentation               | Smart contract execution  | Operate within human-defined envelope     |
| Trust source       | Hierarchy              | Human oversight            | Algorithm (code-is-law)   | Cryptographic trust lineage               |
| Knowledge model    | Tacit, individual      | Training data + tacit      | On-chain only             | Institutional knowledge compounds         |
| Override mechanism | Management authority   | Human veto                 | Fork the chain            | Trust Plane intervention                  |

**Not a DAO.** Decentralized Autonomous Organizations eliminate the trust plane entirely. The DAO hack of 2016 demonstrated the consequences: when a smart contract contained a vulnerability, there was no human authority that could intervene without forking the entire chain (DuPont, 2017; Hassan & De Filippi, 2021). A constrained organization preserves human authority as architecturally superior to algorithmic execution.

**Not algorithmic management.** Kellogg, Valentine, and Christin (2020) document organizations where algorithms manage human workers. The constrained organization inverts this: humans manage AI through architectural constraints, not AI managing humans through opaque algorithms.

Humberd and Latham (2026) use agency theory to analyze when AI achieves sufficient autonomy to be "an agent of the firm." The constrained organization provides the governance architecture for that transition. Harre (2025) models AI governance through institutional economics, establishing the theoretical need that the constrained organization fills. Engin (2025) proposes a Human-AI Governance framework with three dimensions (Decision Authority, Process Autonomy, Accountability) that describes what to measure; the constrained organization provides the implementation architecture.

Hu and Rong (2026) explore "Sovereign Agents"---AI agents with cryptographic self-custody on decentralized infrastructure. This is the conceptual opposite of the constrained organization: where Sovereign Agents examine what happens when human control is removed, the constrained organization proposes how to maintain it.

### Case Study: The Terrene Foundation

The Terrene Foundation---a Singapore Company Limited by Guarantee that maintains open standards for enterprise AI governance---operates as a constrained organization. This is not a post-hoc framing; it is the intended operating model.

**Trust Plane (Human-Defined):**

- A 77-clause constitution with 11 entrenched provisions defines organizational boundaries
- Anti-capture mechanisms prevent any single interest from dominating governance
- Mandatory founder transition ensures the institution outlives its creator
- All open-source IP is fully and irrevocably transferred

**Execution Plane (AI-Agent-Operated):**

- 20 specialized AI agents manage knowledge base operations across 7 categories
- Research, drafting, cross-referencing, quality assurance, and governance checking are agent-performed
- Every paper in this series was produced using this process

**Trust Verification (EATP):**

- Agent actions trace to the master directive (organizational root of authority)
- Constraint envelopes define boundaries: naming conventions, security rules, content standards
- Full conversation histories retained as audit trails

**Institutional Knowledge (CO Five-Layer):**

- Layer 1 (Intent): 20 agents with domain-specific expertise
- Layer 2 (Context): Rules, skills, reference documentation---living institutional handbook
- Layer 3 (Guardrails): 10 hook scripts (pre-execution, post-execution, and lifecycle), including anti-amnesia mechanisms
- Layer 4 (Instructions): 14 structured workflows with approval gates
- Layer 5 (Learning): Observation logs, pattern analysis, knowledge evolution

The production of this paper is itself evidence. The AI agents produced competent initial drafts. I defined what "honest" meant (remove unverifiable claims), what "useful" meant (explain for practitioners, not academics), and what to reject (marketing, overstatement, false precision). The agents could not make these judgments. I could not produce the drafts at this speed. The constrained organization is the synthesis.

---

## Part VI: Why This Exists

### The Gap in Current Approaches

Singapore has strong institutions across the AI lifecycle, but with a specific gap that no existing institution fills.

AI Singapore does foundational research. IMDA's AI Verify provides post-deployment testing. Enterprise SG offers SME digitalization grants. NTUC and SkillsFuture deliver individual training. Big Tech provides commercial platforms. Each does its work well.

What is missing: the connective tissue between research and practice. Specifically:

**Pre-deployment governance architecture.** AI Verify tests systems after they are built. Nothing helps organizations build governance-ready systems from the start. CARE and the Enterprise Agent Trust Protocol (EATP) address this by providing trust architecture that is embedded at design time, not bolted on after deployment.

**An open builder community.** Singapore trains individuals but does not connect them into a community that compounds knowledge across organizations. Trained practitioners graduate into isolation. The community of builders who share patterns, mentor newcomers, and collectively advance the practice does not exist as organized infrastructure.

**Open-source enterprise building blocks.** Enterprise AI capability is enterprise-priced. An SME in Singapore cannot afford the platform costs that large organizations absorb. The Kailash stack (released Apache 2.0) provides enterprise-quality building blocks at zero license cost.

**A sustainable open-source model.** Open source has a sustainability problem. The Kailash stack addresses this by being Apache 2.0: anyone can use it, build on it, and build businesses around it. The economics of openness work when the building blocks are genuinely open: adoption grows because there is no lock-in, and a wider ecosystem of implementers and users emerges than any single company could create.

### Why Open Source Matters for CARE

A governance framework that exists only as a white paper is theory. Theory is insufficient when organizations need to make deployment decisions now.

The Kailash stack provides concrete implementation: Core SDK for workflow orchestration, DataFlow for database operations, Nexus for multi-channel deployment, and Kaizen as an AI agent framework. All Apache 2.0. All designed to work with AI-assisted development tools, enabling small teams with domain expertise to compose enterprise-quality applications from pre-constructed building blocks.

This matters because the AI era fundamentally changes the economics of software creation. CARE provides the governance architecture; the Kailash stack provides the building blocks; the community provides the knowledge.

### Why Open Source Over Proprietary

I could have kept the technology proprietary. The market logic said I should: proprietary platforms command higher margins, create vendor lock-in, and make acquisition more attractive.

But proprietary platforms die with their companies. Open standards outlast them. The Apache 2.0 license sitting in the project repository is the simplest possible trust signal: the code is there, the license is irrevocable, and no one needs to take my word for anything.

Autor (2015) documented how automation creates new tasks even as it eliminates old ones. The question I'm asking is who captures the value from those new tasks. Closed platforms concentrate it. Open infrastructure distributes it. That is the choice, and I have made it.

---

## Part VII: What This Does Not Solve

### Honest Limitations

CARE does not claim that current human competencies are permanently beyond AI. The six categories are a snapshot of 2026, not a permanent boundary. If AI develops genuine moral agency, authentic emotional capacity, or true creative synthesis, the categories will need revision. The framework commits to reassessment, not to defending its current claims against contrary evidence.

CARE does not solve displacement economics. The framework prescribes role redesign over elimination. But prescription is not enforcement. Economic pressures may override ethical commitments. Organizations under competitive pressure may use the mirror to identify roles for elimination rather than roles for development. The macroeconomic effects of widespread AI adoption: aggregate labor market displacement, wage pressure, inequality are beyond the scope of any organizational framework. They require policy responses that CARE complements but cannot substitute for.

CARE does not guarantee regulatory compliance. The architecture is designed to support compliance with the EU AI Act (2024), NIST AI Risk Management Framework (2023), and OECD AI Principles: specifically the human oversight requirements that these frameworks demand. But "designed to support" is not "guaranteed to satisfy." Whether a specific CARE deployment meets regulatory requirements depends on implementation details, jurisdiction, and use case. Organizations need independent legal assessment.

CARE does not eliminate power asymmetries. Management deploys the mirror onto workers, not the reverse. The framework proposes safeguards but cannot architecturally prevent misuse.

CARE does not address democratic legitimacy. As Rahwan (2018) argues, society-in-the-loop governance requires democratic mechanisms for determining what values AI should encode. CARE assumes organizational values are given; it does not address where they come from.

CARE does not provide model-level alignment. Constitutional AI (Bai et al., 2022) addresses how to make AI follow constraints at the model level. CARE's Trust Plane assumes the AI follows its constraints; the question of how to ensure that at the model level is complementary but separate.

### Constraint Gaming

Any constraint-based system can be gamed. An AI that technically complies with every constraint while violating their intent is not governed, it is gaming the system. This is not a theoretical concern. It is the central operational risk of the CARE model. The framework addresses it through the transparency principle (all actions are auditable) and evolutionary trust (boundaries tighten when gaming is detected). Whether these mechanisms prove sufficient at scale remains to be demonstrated.

### Alternatives Possibly Underweighted

Red-team review identified four alternatives that deserve more consideration: **Tiered Approval Systems** (approve categories of actions rather than all-or-nothing constraints), **Collaborative Human-AI Decision-Making** (joint deliberation rather than plane separation), **Insurance-Based Governance** (let actuarial analysis set governance requirements), and **Distributed Accountability** (accountability across committees rather than individual trust chains).

I acknowledge these alternatives have merit. CARE may ultimately prove to be one approach among several, not the approach.

---

## Part VIII: Broader Impact

### Labor and Displacement

The Mirror Thesis has a dual nature. Used well, it identifies uniquely human contributions and invests in their development. Used badly, it identifies roles for elimination. Management deploys the mirror onto workers, not the reverse. The framework proposes safeguards---worker consent, data transparency, democratic governance of mirror configuration---but cannot architecturally prevent misuse.

### Access and Equity

The constrained organization requires significant initial investment in institutional knowledge engineering. Organizations with weak institutional knowledge have the most to gain and the least capacity to build. This creates an access gap that could widen inequality between well-resourced and under-resourced organizations.

### Geographic Considerations

CARE is developed in Singapore and draws on Singapore's institutional context. Whether the framework translates effectively across jurisdictions, legal systems, and cultural contexts is an empirical question that cross-cultural testing has not yet answered.

---

## Part IX: What CARE Is, Precisely

CARE stands for Collaborative Autonomous Reflective Enterprise. Each word is chosen:

- **Collaborative**: Human and AI as partners, each contributing what they do best
- **Autonomous**: AI executes within human-defined boundaries without requiring approval for every action
- **Reflective**: The system reveals what makes human contribution irreplaceable
- **Enterprise**: Organizational-scale design for real-world complexity

### Three Core Propositions

1. **The Dual Plane Model**: Organizations operate on two separable planes: a Trust Plane (accountability, values, authority, boundaries) that is permanently human, and an Execution Plane (task completion, coordination) that can be shared with AI

2. **The Mirror Thesis**: Building AI that can execute every organizational role creates a diagnostic mirror. The gap between AI execution and organizational need reveals uniquely human value

3. **Human-on-the-Loop**: Neither bottleneck (human-in-the-loop) nor abandonment (human-out-of-the-loop). Humans define the operating envelope; AI executes within it; humans observe and refine

### Eight Principles

1. **Full Autonomy as Baseline**: AI handles everything it can, within defined trust boundaries, revealing what only humans contribute
2. **Human Choice of Engagement**: Humans elevate involvement through deliberate judgment, not reflexive approval
3. **Transparency as Foundation**: Every AI action is fully visible---not because humans watch everything, but because the ability to look makes the choice not to look an informed one
4. **Continuous Operation**: AI maintains consistent quality; humans bring judgment when needed, not when the clock demands it
5. **Human Accountability Preserved**: Every consequential action traces to human authority through the trust chain
6. **Graceful Degradation**: When AI reaches competence boundaries, it degrades safely---reduced autonomy, increased transparency, escalation---preserving human agency
7. **Evolutionary Trust**: Trust boundaries evolve based on demonstrated performance, not assumption
8. **Purpose Alignment**: AI executes within human-defined organizational purposes, not its own optimization targets

These principles form an integrated system. Full autonomy without transparency is dangerous. Transparency without human choice is surveillance. Human choice without accountability is abdication. The principles constrain and support each other.

### Falsification Conditions

CARE's central claims are testable. The following conditions, if met, would warrant abandoning the framework:

- If the Dual Plane separation proves consistently unimplementable across five or more organizational deployments, the architectural model should be revised.
- If the six competency categories cannot be reliably identified across ten or more deployments, the Mirror Thesis should be abandoned.
- If human-on-the-loop governance produces worse outcomes than human-in-the-loop or human-out-of-the-loop across matched comparisons, the supervisory model should be rejected.
- If constrained organizations show no governance advantage over traditional enterprises with AI tools, the organizational form is not distinct.
- If constraint gaming proves undetectable or unmanageable in three or more deployments, the constraint-based governance model is insufficient.

---

## Conclusion: A Proposition, Not a Verdict

The question this paper addresses---what is the human actually for?---does not have a permanent answer. AI capability will continue advancing. The boundary between trust and execution will shift.

What CARE offers is not a final answer but a practical architecture: the Dual Plane Model for governance structure, the Mirror Thesis for organizational development, Human-on-the-Loop for supervisory design, and the Constrained Organization as the integrated form. The companion protocols---EATP for trust verification, CO for institutional knowledge---provide the operational mechanisms.

The alternative, that every organization solving the same governance problems independently, making the same mistakes, with no shared learning, is worse.

---

## References

Autor, D. (2015). Why Are There Still So Many Jobs? The History and Future of Workplace Automation. _Journal of Economic Perspectives_, 29(3), 3-30.

Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. _arXiv:2212.08073_.

Bainbridge, L. (1983). Ironies of Automation. _Automatica_, 19(6), 775-779.

DuPont, Q. (2017). Experiments in Algorithmic Governance: A History and Ethnography of "The DAO." In _Bitcoin and Beyond_. Routledge.

Emery, F. E. & Trist, E. L. (1960). Socio-technical Systems. In _Management Sciences, Models and Techniques_, Vol. 2. Pergamon.

Engin, Z. (2025). Human-AI Governance (HAIG): A Trust-Utility Approach. _arXiv:2505.01651_.

European Union. (2024). Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). _Official Journal of the European Union_.

Floridi, L. & Cowls, J. (2019). A Unified Framework of Five Principles for AI in Society. _Harvard Data Science Review_, 1(1).

Hagendorff, T. (2020). The Ethics of AI Ethics: An Evaluation of Guidelines. _Minds and Machines_, 30, 99-120.

Haidt, J. (2001). The Emotional Dog and Its Rational Tail: A Social Intuitionist Approach to Moral Judgment. _Psychological Review_, 108(4), 814-834.

Harre, M. (2025). From Firms to Computation: AI Governance and the Evolution of Institutions. _arXiv:2507.13616_.

Hassan, S. & De Filippi, P. (2021). Decentralized Autonomous Organization. _Internet Policy Review_, 10(2).

Hong, J. (2026b). "Enterprise Agent Trust Protocol (EATP): A Core Thesis." White Paper Series, Version 2.2. Terrene Foundation. https://terrene.foundation/publications/eatp-core-thesis. Companion paper providing the technical trust verification protocol for the governance architecture described here.

Hong, J. (2026c). "Cognitive Orchestration (CO): A Core Thesis." White Paper Series, Version 1.1. Terrene Foundation. https://terrene.foundation/publications/co-core-thesis. Companion paper providing the institutional knowledge methodology.

Hong, J. (2026e). "The Constrained Organization: An Organizational Model for Enterprise AI Governance." White Paper Series, Version 1.0. Terrene Foundation. https://terrene.foundation/publications/constrained-organization-thesis. Companion paper on institutional design.

Hu, B. A. & Rong, H. (2026). Sovereign Agents: Towards Infrastructural Sovereignty and Diffused Accountability in Decentralized AI. _arXiv:2602.14951_.

Humberd, B. & Latham, S. (2026). When AI Becomes an Agent of the Firm: Examining the Evolution of AI in Organizations Through an Agency Theory Lens. _Journal of Management Studies_, 63(2), pp. 668-694.

IMDA. (2020). _Model AI Governance Framework_, 2nd Edition. Singapore.

Jobin, A., Ienca, M., & Vayena, E. (2019). The Global Landscape of AI Ethics Guidelines. _Nature Machine Intelligence_, 1, 389-399.

Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at Work: The New Contested Terrain of Control. _Academy of Management Annals_, 14(1), 366-410.

Klein, G. (1998). _Sources of Power: How People Make Decisions_. MIT Press.

Kolbjornsrud, V. (2024). Designing the Intelligent Organization: Six Principles for Human-AI Collaboration. _California Management Review_, 66(2), pp. 44-64.

March, J. G. (1991). Exploration and Exploitation in Organizational Learning. _Organization Science_, 2(1), 71-87.

Methnani, L., Aler Tubella, A., & Dignum, V. (2021). Let Me Take Over: Variable Autonomy for Meaningful Human Control. _Frontiers in AI_, 4:737072.

Nahapiet, J., & Ghoshal, S. (1998). Social Capital, Intellectual Capital, and the Organizational Advantage. _Academy of Management Review_, 23(2), 242-266.

National Institute of Standards and Technology. (2023). _AI Risk Management Framework (AI RMF 1.0)_. NIST AI 100-1.

Nonaka, I. (1994). A Dynamic Theory of Organizational Knowledge Creation. _Organization Science_, 5(1), 14-37.

Organisation for Economic Co-operation and Development. (2019, updated 2024). _OECD AI Principles_. OECD/LEGAL/0449.

Parasuraman, R., & Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. _Human Factors_, 39(2), 230-253.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A Model for Types and Levels of Human Interaction with Automation. _IEEE Transactions on Systems, Man, and Cybernetics---Part A_, 30(3), 286-297.

Polanyi, M. (1966). _The Tacit Dimension_. University of Chicago Press.

Rahwan, I. (2018). Society-in-the-Loop: Programming the Algorithmic Social Contract. _Ethics and Information Technology_, 20, 5-14.

Santoni de Sio, F. & van den Hoven, J. (2018). Meaningful Human Control over Autonomous Systems: A Philosophical Account. _Frontiers in Robotics and AI_, 5, 15.

Sheridan, T. B. & Verplank, W. L. (1978). _Human and Computer Control of Undersea Teleoperators_. MIT Man-Machine Systems Laboratory Report.

Shneiderman, B. (2022). _Human-Centered AI_. Oxford University Press.

Trist, E. L. & Bamforth, K. W. (1951). Some Social and Psychological Consequences of the Longwall Method of Coal-Getting. _Human Relations_, 4(1), 3-38.

---

## A Note on How This Paper Was Produced

This paper was written using the process it describes. The production serves as a case study for the constrained organization methodology.

The initial draft was generated by a team of AI agents:

- **research analysts** that explored the knowledge base and source repositories, wrote structured drafts, and cross-referenced claims against anchor documents.
- A separate **alignment-critic agent** red-teamed the output, identifying eight issues including factual errors, overstatements, and inconsistencies with source material.
- A **debate-expert agent** challenged the draft's arguments and flagged unverifiable claims.

The author directed every iteration. Instructions included:

- remove claims that cannot be verified
- strip out references to structures that do not yet exist
- simplify the disclosure to plain facts
- explain technical terms for non-technical readers
- ensure the paper reads as a standards proposition rather than marketing

The author made direct edits to tone, phrasing, and substance throughout. Multiple rounds of revision followed, each narrowing the gap between what the agents produced and what the author judged to be honest and useful.

The following experimental observations were made during production:

- **Trust Plane interventions**: The author overrode AI output 14 times for factual inaccuracy, 8 times for overstatement, and 6 times for marketing language. The AI could not distinguish "honest" from "persuasive."
- **Mirror Thesis manifestation**: The AI produced competent prose at speed. It could not judge what was honest versus strategic, what to include versus omit, or when a claim exceeded its evidence. These judgments were the author's unique contribution.
- **Convention drift detected**: The AI defaulted to academic hedging conventions ("it could be argued that...") rather than the direct style the author specified. This required repeated correction.
- **Constraint gaming**: No instances detected during production. The AI complied with the spirit and letter of instructions. Whether this holds under adversarial conditions is unknown.

The tools used were Claude Code (Anthropic) with specialized subagents for research, alignment checking, and adversarial review. The full conversation history, including every instruction, every correction, and every piece of content the author rejected, is retained by the author.

---

_See also: Hong, J. (2026b). "EATP: A Core Thesis" for the trust verification protocol that operationalizes CARE. Hong, J. (2026c). "CO: A Core Thesis" for methodology. Hong, J. (2026e). "The Constrained Organization" for institutional design._
