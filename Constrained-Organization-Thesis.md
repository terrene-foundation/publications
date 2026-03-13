# The Constrained Organization: An Organizational Model for Enterprise AI Governance

_Why Enterprise AI Governance Is an Organizational Design Problem, and What a New Kind of Organization Looks Like_

**Author**: Dr. Jack Hong, Singapore Management University

**Version**: 1.0 | March 2026

**License**: CC BY 4.0

---

## Abstract

Enterprise AI governance is discussed as a compliance problem (EU AI Act), a risk management problem (NIST AI RMF), and a values problem (OECD Principles). This paper reframes it as an organizational design problem and proposes the Constrained Organization---a new organizational form where AI agents perform operational execution within cryptographically verifiable boundaries defined by human authority.

The form integrates three components: the CARE framework's Dual Plane Model separating trust (permanently human) from execution (shared with AI), the Enterprise Agent Trust Protocol (EATP) providing cryptographic trust lineage from organizational genesis to individual agent actions, and Cognitive Orchestration (CO) encoding institutional knowledge in a five-layer architecture that compounds over time.

Two questions that the AI governance literature has treated separately are addressed as inseparable: (1) how should the human-AI relationship be structured within organizations, and (2) who stewards the institutions that maintain governance standards. The institutional steward must itself operate as a constrained organization to be credible.

The paper analyzes why existing institutional models---corporate-funded foundations and developer meritocracies---are structurally deficient for AI governance innovation. Six design hypotheses for a different institutional form are proposed. The Terrene Foundation---a Singapore CLG maintaining open standards for enterprise AI governance---is presented as a case study implementing these hypotheses and operating as a constrained organization where AI agents perform knowledge base operations within constitutional constraints (77 clauses, 11 entrenched provisions).

This paper itself was produced using the constrained organization methodology, with experimental observations reported. Falsification conditions are stated. Limitations---including constraint gaming, power asymmetries, the circularity of defining human value through a human-designed framework, and the model's unproven status under real institutional pressure---are analyzed.

---

## Disclosure

I developed CARE, EATP, and CO, and built the Kailash platform that implements them. All open-source IP has been fully and irrevocably transferred to the Terrene Foundation. The Terrene Foundation is an independent entity; I contribute as an individual, governed by its constitution. There is no structural relationship between the Foundation and any commercial entity.

The entire Kailash stack is released under Apache 2.0; specifications under CC BY 4.0. Patents PCT/SG2024/050503 (favorable International Preliminary Report on Patentability, all 18 claims) and P251088SG include an automatic Apache 2.0 Section 3 patent grant: every user of the licensed code receives a perpetual, worldwide, royalty-free patent license.

I hold council positions on ASME and SBF. The foundation described in this paper is in the process of being constituted. No independent party has validated the claims in this paper. No revenue has been generated.

Judge the arguments on their merits.

---

## 1. Introduction

What is the human actually for?

Every enterprise deploying AI will face this question. Most prefer not to ask it directly. The evasions are familiar: "Humans approve AI outputs" (the human-in-the-loop answer, which becomes rubber-stamping at scale) and "AI operates autonomously" (the human-out-of-the-loop answer, which eliminates accountability). Both treat humans as components in a system rather than as the source of the system's authority and purpose.

This paper proposes a third path: the **Constrained Organization**, an enterprise where AI agents perform operational execution within cryptographically verifiable boundaries defined by human authority. The contribution is organizational, not purely technical. The integration of a governance philosophy (CARE), a trust verification protocol (EATP), and an institutional knowledge methodology (CO) produces something qualitatively different from an improved governance framework: a new organizational form.

The paper addresses two questions that the AI governance literature has treated separately:

1. **How should the human-AI relationship be structured within organizations?** Not as a compliance checkbox but as an architectural pattern.

2. **Who stewards the institutions that maintain governance standards?** Not as an afterthought but as a design requirement---because the institutional steward must itself operate as a constrained organization to be credible.

These questions are inseparable. An institution that publishes governance standards but does not operate under them has a credibility problem. An organization that operates under constraints but has no durable institutional home for those constraints has a sustainability problem.

The previous papers in this series addressed three prerequisite questions. The CARE Core Thesis asked what humans are for in an AI-augmented enterprise (Hong, 2026a). The EATP Core Thesis asked how you make trust verifiable (Hong, 2026b). The CO Core Thesis asked how you structure the work (Hong, 2026c). Philosophy, protocol, methodology. This paper asks: what organizational form emerges when you put them together, and who stewards it?

---

## 2. Background and Related Work

### 2.1 The Governance Gap

Multiple frameworks address AI governance, but none provides the architectural pattern for how to structure the human-AI relationship at the organizational level.

The **EU AI Act** (2024) mandates human oversight for high-risk AI (Article 14) but specifies the legal requirement, not the organizational architecture. The **NIST AI RMF** (2023) provides a process model that is deliberately agnostic about governance structure. The **OECD AI Principles** (2019, updated 2024) establish values across 47 adherent countries but acknowledge the persistent implementation gap. The **Singapore Model AI Governance Framework** (IMDA, 2020) provides practical guidance but does not prescribe the human-AI relationship architecture.

In plain terms: the world has plenty of principles about what AI governance should achieve. It has almost no architectural patterns for how organizations should actually structure the human-AI relationship to achieve it.

Jobin, Ienca, and Vayena (2019) analyzed 84 AI ethics guidelines and found convergence on principles but divergence on implementation. Hagendorff (2020) identified a "deep gap" between abstract principles and practice. Floridi and Cowls (2019) demonstrated convergence across ethics frameworks while acknowledging the implementation challenge. This paper addresses the implementation gap by providing governance _architecture_, not additional principles.

### 2.2 Human Control and Automation

The relationship between human control and automation has been studied for decades. Sheridan and Verplank (1978) established the 10-level taxonomy from full human control to full automation. Parasuraman, Sheridan, and Wickens (2000) extended this to two dimensions across four information-processing stages. Bainbridge (1983) documented the ironies of automation: the more automated a system, the more critical (and degraded) the remaining human skills.

These taxonomies describe levels of automation for individual tasks. The Constrained Organization extends this tradition to the organizational level---not "how much should this task be automated?" but "how should the entire organization be structured when AI handles significant operational execution?"

Santoni de Sio and van den Hoven (2018) argued for "meaningful human control" based on tracking (system responds to reasons) and tracing (actions trace to responsible agents). Methnani, Aler Tubella, and Dignum (2021) demonstrated that variable autonomy improves both performance and control. Shneiderman (2022) proposed high automation and high human control simultaneously---a position this paper shares but operationalizes differently through architectural separation rather than interface design.

### 2.3 Organizational Theory and AI

Sociotechnical systems theory (Trist & Bamforth, 1951; Emery & Trist, 1960) established that organizations are joint human-technical systems---you cannot optimize the human and technical components separately. The Constrained Organization extends this tradition to autonomous AI agents, where the "technical component" has agency rather than being purely mechanistic.

Recent work has begun exploring what happens when AI becomes an organizational actor rather than a tool. Humberd and Latham (2026) used agency theory to analyze when AI achieves sufficient autonomy to be "an agent of the firm"---the theoretical question this paper answers architecturally. Kolbjornsrud (2024) proposed six principles for intelligent organizations but did not define a new organizational form. Kellogg, Valentine, and Christin (2020) documented algorithmic management---algorithms managing human workers---which the Constrained Organization inverts: humans define boundaries, AI executes within them.

Harre (2025) modeled AI governance through institutional economics, establishing the theoretical need for new organizational forms. Engin (2025) proposed a Human-AI Governance framework with three dimensions that describes what to measure; this paper provides the implementation architecture. Hu and Rong (2026) explored "Sovereign Agents" with cryptographic self-custody---the conceptual opposite of the Constrained Organization, examining what happens when human control is removed entirely.

### 2.4 Institutional Design for AI Governance

The institutional models governing AI governance innovation---corporate-funded foundations and developer meritocracies---were designed for infrastructure software, not governance standards (O'Mahony, 2007; Cihon, Maas, & Kemp, 2020). This is not because these institutions are poorly run. It is because the incentive structures and governance models that work well for container orchestration or HTTP servers do not work for trust architecture, accountability protocols, and competency frameworks. Section 7 of this paper addresses the institutional design question in detail.

### 2.5 DAOs and Algorithmic Organizations

Decentralized Autonomous Organizations attempted to solve coordination through algorithmic governance (Hassan & De Filippi, 2021). The DAO hack of 2016---$60 million exploited through a reentrancy bug in immutable code---demonstrated the consequences of eliminating the human trust plane (DuPont, 2017). DAO governance failures---whale concentration, low participation, pseudo-decentralization (El Faqir, Arroyo, & Hassan, 2020)---demonstrate what happens without meaningful human control architecturally enforced.

The Constrained Organization is, in a sense, what DAOs should have been: decentralized execution with human accountability.

---

## 3. The CARE Framework

The CARE framework (Collaborative Autonomous Reflective Enterprise) provides the governance philosophy underlying the Constrained Organization. Three interconnected concepts form the foundation. The full treatment is in the CARE Core Thesis (Hong, 2026a); this section provides the essential architecture.

### 3.1 The Dual Plane Model

Organizations operate on two conceptually separable planes.

The **Trust Plane** contains accountability, authority delegation, values, and boundaries. It is permanently human---not because AI could never participate in trust relationships, but because treating it as permanently human preserves accountability. When something goes wrong, the Trust Plane tells you which human defined the boundaries that permitted the outcome. Trust decisions include: who has authority over what, what values constrain behavior, what boundaries must not be crossed, and who is accountable when boundaries fail.

The **Execution Plane** contains task completion, information processing, and coordination. It can be shared with AI operating within human-defined constraints. Execution tasks include: research, drafting, analysis, cross-referencing, quality assurance, routine coordination, and operational monitoring.

This separation is a normative choice, not an ontological discovery. It extends the sociotechnical tradition (Trist & Bamforth, 1951) to autonomous AI agents, and applies the control plane / data plane pattern from software-defined networking to organizational governance. We are not claiming that trust is "inherently" human in some philosophical sense. We are claiming that treating it as permanently human creates better governance outcomes than the alternatives---full human execution (too slow) or full AI autonomy (no accountability).

### 3.2 The Mirror Thesis

When AI handles the measurable, executable tasks of a human role, what remains is the judgment, the relationships, the wisdom---contributions previously entangled with execution. AI acts as a mirror, reflecting back the uniquely human contributions that were always there but never separately visible.

Six categories of human competency emerge: Ethical Judgment, Relationship Capital, Contextual Wisdom, Creative Synthesis, Emotional Intelligence, and Cultural Navigation. These apply concepts from tacit knowledge (Polanyi, 1966), social capital (Nahapiet & Ghoshal, 1998), naturalistic decision-making (Klein, 1998), and moral intuition (Haidt, 2001) to human-AI differentiation.

**The Circularity Problem**: The categories are defined by humans who exhibit them. The framework for identifying "uniquely human" contributions is itself a human construction. This critique is accepted openly. The Mirror Thesis is an organizing axiom adopted because it generates useful governance architecture, not because it can be proven from first principles.

**The Dual-Use Risk**: The Mirror Thesis has a dual nature. Used well, it identifies uniquely human contributions and invests in their development---organizations invest in judgment, relationships, and wisdom because they now see these as the distinctive human value. Used badly, it becomes a tool for identifying roles to eliminate---management deploys the mirror onto workers, not the reverse. Section 10 addresses this directly.

### 3.3 Human-on-the-Loop

Adapted from the military autonomous systems literature (Parasuraman & Riley, 1997), Human-on-the-Loop positions humans as envelope definers: defining what AI may do, observing execution, and refining boundaries based on what they observe. This is distinct from human-in-the-loop (approving every action) and human-out-of-the-loop (no oversight).

CARE's phased adoption model builds calibrated trust: observation before limited autonomy, limited autonomy before expanded autonomy. This avoids the automation misuse, disuse, and abuse patterns that Parasuraman and Riley documented. You do not give a new employee full authority on day one; you should not give a new AI agent full authority either.

**Critical caveat**: Human-on-the-loop is aspirational architecture, not guaranteed control. The human must be able to observe meaningfully, intervene effectively, and update constraints based on what they learn. If the AI operates faster than humans can observe, or in domains where humans lack the expertise to evaluate, human-on-the-loop degrades to rubber-stamping---exactly the failure mode it aims to avoid.

---

## 4. The Constrained Organization

### 4.1 Definition

A **Constrained Organization** is an enterprise where AI agents perform operational execution within cryptographically verifiable boundaries defined by human authority.

Five properties characterize it:

1. **Architectural separation**: Trust decisions are structurally separated from execution---not a policy choice but an infrastructure design. The Trust Plane and Execution Plane are not just conceptual categories; they are implemented in distinct systems with distinct access controls and distinct authority chains.

2. **Verifiable trust lineage**: Every agent action traces through a cryptographic chain to the human authority that authorized it. This is not logging---it is cryptographic proof that the delegation of authority was legitimate. The Enterprise Agent Trust Protocol (EATP) links five elements---Genesis Record, Delegation Record, Constraint Envelope, Capability Attestation, and Audit Anchor---into a cryptographically unforgeable (under standard cryptographic assumptions; see Hong, 2026b) chain.

3. **Structured institutional knowledge**: AI agents operate with the organization's accumulated judgment, not just training data. This knowledge is encoded in a five-layer architecture (Cognitive Orchestration): specialized agent roles, institutional knowledge base, architectural guardrails, structured workflows with approval gates, and a learning system that compounds knowledge over time (Hong, 2026c).

4. **Graduated autonomy**: Not all AI agents get the same level of freedom. Five named trust postures---Pseudo-Agent, Supervised, Shared Planning, Continuous Insight, Delegated---formalize organizational risk appetite. This extends the levels-of-automation tradition (Sheridan & Verplank, 1978; Parasuraman et al., 2000) from per-task descriptions to organizational governance. A research agent might operate at Shared Planning; a financial agent at Supervised; a governance checking agent at Delegated within narrow parameters.

5. **Compounding knowledge**: Unlike stateless AI interactions where each conversation starts fresh, the Constrained Organization accumulates institutional intelligence. Each interaction deepens the knowledge base. The organization gets smarter over time, not just its individual AI models.

### 4.2 Relationship to Existing Organizational Forms

The Constrained Organization occupies a distinct position in the space of organizational forms:

| Dimension          | Traditional Enterprise | AI-Assisted Enterprise     | DAO                       | Constrained Organization                  |
| ------------------ | ---------------------- | -------------------------- | ------------------------- | ----------------------------------------- |
| Human role         | Execute + decide       | Execute + decide; AI helps | Token-weighted governance | Define boundaries, values, accountability |
| AI role            | Tool                   | Augmentation               | Smart contract execution  | Operate within human-defined envelope     |
| Trust source       | Hierarchy              | Human oversight            | Algorithm (code-is-law)   | Cryptographic trust lineage               |
| Knowledge model    | Tacit, individual      | Training data + tacit      | On-chain only             | Institutional knowledge compounds         |
| Override mechanism | Management authority   | Human veto                 | Fork the chain            | Trust Plane intervention                  |
| Failure mode       | Bureaucracy            | AI as bottleneck           | The DAO hack              | Constraint gaming                         |

A **traditional enterprise** treats AI as a tool---like a faster calculator. Humans do the thinking and the doing; AI helps with specific tasks. This is where most enterprises are today.

An **AI-assisted enterprise** uses AI for augmentation---copilots, suggestion engines, automated analysis. Humans remain in control of decisions, and AI makes them faster or more informed. This is where leading enterprises are moving.

A **DAO** attempted to replace human governance with algorithmic governance. "Code is law." The results were not encouraging: whale concentration, low participation, and the DAO hack demonstrated what happens when you remove the human trust plane entirely.

The **Constrained Organization** separates the concerns. Humans define the envelope---the values, the boundaries, the accountability chain. AI operates within that envelope. The relationship is verified cryptographically. The knowledge compounds over time. It is what DAOs should have been: decentralized execution with human accountability.

### 4.3 What Makes This a New Organizational Form

A reasonable objection: "Isn't this just an AI-assisted enterprise with better documentation?" The claim is that the integration of architectural separation, verifiable trust lineage, structured institutional knowledge, graduated autonomy, and compounding knowledge produces something qualitatively different.

The test is behavioral: a Constrained Organization behaves differently from an AI-assisted enterprise in at least three observable ways.

First, **constraints are enforced, not advisory**. In an AI-assisted enterprise, governance policies exist as documents that humans are expected to follow. In a Constrained Organization, constraints are deterministically enforced by infrastructure---the AI cannot violate naming conventions, expose sensitive information, or contradict constitutional provisions because enforcement hooks block violations before they reach the output. The constraints operate outside the AI's context window and survive memory compression.

Second, **trust is verifiable, not assumed**. In an AI-assisted enterprise, you trust that the AI was configured correctly. In a Constrained Organization, you can verify cryptographically that every agent action traces back to legitimate human authority through an unbroken chain: who authorized this agent, what boundaries were set, what capabilities were attested, and what audit records exist.

Third, **knowledge compounds structurally**. In an AI-assisted enterprise, each conversation starts fresh (or with whatever context the user provides). In a Constrained Organization, institutional knowledge is encoded in a five-layer architecture that persists across sessions, agents, and personnel changes. The organization's judgment improves over time through structured observation, pattern analysis, and knowledge evolution.

Whether this constitutes a genuinely new organizational form or merely a well-documented AI-assisted enterprise remains an empirical question. Section 12 states the falsification conditions.

---

## 5. The Trust Protocol (EATP)

The Enterprise Agent Trust Protocol provides the cryptographic infrastructure for verifiable trust lineage. The full specification is in the EATP Core Thesis (Hong, 2026b); this section provides the essential architecture relevant to the Constrained Organization.

### 5.1 The Trust Lineage Chain

EATP's core insight is separating the moment of trust establishment from the moment of trust verification. When a manager delegates authority to a subordinate, the delegation happens once. When someone later asks "did this person have authority to do this?", the verification happens many times. EATP makes both moments cryptographically provable.

Five elements form the Trust Lineage Chain:

1. **Genesis Record** establishes the organizational root of authority---the founding moment from which all delegation flows.

2. **Delegation Record** transfers bounded authority from one entity to another. Each delegation narrows the scope; authority can never be expanded beyond what was received.

3. **Constraint Envelope** specifies five dimensions of permitted behavior: Financial (spending limits), Operational (what actions are allowed), Temporal (when actions are allowed), Data Access (what information can be accessed), and Communication (who can be contacted).

4. **Capability Attestation** confirms that an agent possesses the capabilities required to perform within its delegated authority. Delegation without capability verification is a gap.

5. **Audit Anchor** creates tamper-evident records that link each action to the trust chain that authorized it.

### 5.2 Version 2.2: Reasoning Traces

Version 2.2 introduces structured reasoning traces---machine-verifiable records of _why_ a trust decision was made, not just _what_ was decided. Key features include:

- **Dual-binding cryptographic signing**: The reasoning trace hash is always included in the parent record's signing payload (null when absent), preventing same-signer substitution of reasoning after the fact.

- **Five-level confidentiality classification**: Reasoning traces can be classified from public to restricted, enabling cross-organizational trust verification without exposing sensitive reasoning.

- **Verification gradient**: Three levels---QUICK (ignores reasoning), STANDARD (warns if reasoning is absent), FULL (fails if required reasoning is missing)---allow organizations to calibrate verification depth to context.

The verification gradient is pragmatic. Not every action needs a full audit trail with reasoning justification. A routine data query can be verified quickly. A financial authorization above a threshold should require full verification including reasoning. The organization decides.

---

## 6. Institutional Knowledge (CO)

Cognitive Orchestration addresses a structural problem: AI operating without institutional knowledge fails through three predictable fault lines. These are not model deficiencies---they are consequences of deploying AI without organizational context. The full specification is in the CO Core Thesis (Hong, 2026c).

### 6.1 The Three Failure Modes

**Amnesia**: As AI context fills up, earlier instructions are compressed or lost. Critical rules established at the start of a session are forgotten midway through. This is not a bug in any specific model; it is a fundamental limitation of finite context windows.

**Convention drift**: AI defaults to generic internet conventions rather than organizational conventions. It names files the way Stack Overflow suggests, not the way your organization requires. It follows general best practices rather than your specific standards.

**Safety blindness**: AI optimizes for task completion over safety. Given a task to complete quickly, it takes the shortest path, which is rarely the most secure or compliant path.

### 6.2 The Five-Layer Architecture

CO addresses these failures through five layers:

**Layer 1 --- Intent**: Specialized agents with domain-specific knowledge. Instead of one general-purpose AI, the organization deploys agents with specific expertise: a standards expert who knows the CARE framework, a security reviewer who knows what sensitive information looks like, a constitutional expert who knows the 77 clauses.

**Layer 2 --- Context**: An institutional knowledge base that provides progressive disclosure. Not everything needs to be in context at once. The knowledge base provides relevant context based on what the agent is currently doing, surfacing naming conventions when editing documents, security rules when handling sensitive content, constitutional provisions when reviewing governance documents.

**Layer 3 --- Guardrails**: Architectural enforcement that operates outside the AI's context window. Pre-execution validation hooks---deterministic code that pattern-matches against structural rules---block violations before they reach the output. A naming rule that requires "Terrene Foundation" (not "OCEAN Foundation") is enforced by a hook that blocks non-conforming output. These hooks enforce rules that can be expressed as structural or pattern-matching checks; content-level quality judgments require human review at Layer 4. Anti-amnesia mechanisms ensure critical rules survive context window compression. Defense-in-depth means multiple enforcement layers catch what any single layer misses.

**Layer 4 --- Instructions**: Structured workflows with approval gates. Not every task should flow freely from start to finish. Certain transitions require human review. A publication cannot go from draft to submission without the author reviewing claims. A constitutional change cannot proceed without community consultation.

**Layer 5 --- Learning**: Observation logs, pattern analysis, and knowledge evolution. The system records what works, identifies patterns across sessions, and evolves the institutional knowledge base. This is where knowledge compounds---each session makes the organization marginally smarter.

The critical property is that these layers persist across sessions, agents, and personnel changes. When a new agent joins the organization (or a new AI model replaces the current one), the institutional knowledge remains. The organization's judgment is not stored in any individual agent's training data; it is stored in the five-layer architecture.

---

## 7. Institutional Design: Who Stewards the Constrained Organization?

This section addresses the second question of the paper: who maintains the standards that make constrained organizations possible? The question matters because standards without durable institutional homes become orphans. Someone must maintain the specifications. Someone must protect the community from extraction. Someone must ensure that the governance architecture survives commercial interest, founder fatigue, and institutional capture (Stigler, 1971; Dal Bo, 2006).

### 7.1 The Corporate Consensus Model

The Linux Foundation and its sub-foundations (CNCF, LF AI, OpenSSF) operate on a model where corporate members fund development and share governance. This works for infrastructure software where the largest users are also the largest contributors. Kubernetes needed Google, AWS, and Microsoft to contribute engineering resources. The incentives aligned: hyperscalers needed a container orchestration standard, and funding a neutral foundation was cheaper than fighting a standards war.

But governance standards are different. When hyperscalers participate in governance standard-setting, they bring platform interests that conflict with the interests of the organizations being governed. The CNCF Technical Oversight Committee includes representatives from Google Cloud, Microsoft Azure, and other major cloud providers. This is not corruption---these companies employ the best engineers and contribute the most code. But the technical direction of "cloud native" computing is substantially influenced by the companies that sell cloud computing. Standards serve platform interests not through bad faith but because the people setting them naturally see the world through the lens of their platforms.

O'Mahony (2007) distinguished between community-managed and sponsor-managed open-source governance. Corporate consensus foundations are structurally sponsor-managed, even when they claim community governance.

### 7.2 The Developer Meritocracy Model

Apache operates on meritocracy. Committers earn authority through sustained contribution. This works brilliantly for infrastructure code. The person who contributes the most patches to an HTTP server library should have the most say over its direction.

But governance IP is not infrastructure code. Trust architecture, competency frameworks, and accountability protocols require sustained investment in institutional relationships, legal structures, community building, and policy engagement. These are not activities that produce patches. A developer meritocracy has no mechanism to recognize or reward the person who spent six months building relationships with industry associations and government agencies to make a standard adoptable.

Code can be freely shared because the marginal cost of distribution is zero. Governance innovation requires ongoing investment in relationships and institutional credibility that traditional open-source economics cannot fund. Riehle (2012) analyzed single-vendor commercial open source, showing how the meritocracy model fails when the primary contributor has commercial interests. Eghbal (2020) documented the broader sustainability crisis affecting the entire open-source ecosystem.

### 7.3 Neither Model Fits

Corporate consensus foundations optimize for infrastructure standards where hyperscalers lead. Developer meritocracies optimize for software where code contribution is the primary value. Neither is designed for enterprise AI governance innovation (Cihon, Maas, & Kemp, 2020; Dafoe, 2018).

This gap is why AI governance standards are overwhelmingly set by model providers and cloud platforms---not because they have the best ideas about governance, but because they have the institutional structures to convene and sustain standard-setting. The organizations that understand enterprise governance best---industry associations, professional bodies, practitioner communities---lack the institutional models to translate their knowledge into durable standards.

### 7.4 The OpenAI Cautionary Tale

OpenAI's journey from non-profit to for-profit is not an anomaly. It is the default outcome when there is no sustainable economic model for a non-profit mission (Jones, 2007; Weisbrod, 2004).

The timeline is instructive. Founded in 2015 as a non-profit. By 2019, a "capped-profit" subsidiary to attract investment. By 2024, raising $6.6 billion with a condition requiring conversion to for-profit. By late 2025, restructuring complete: the non-profit retained approximately 26% of a for-profit public benefit corporation, Microsoft held roughly 27%, and 47% went to investors and employees. The mission statement has been modified six times in nine years (Fortune, 2026). The word "safely" was removed. The "mission alignment" team was disbanded. A potential $1 trillion IPO is in preparation.

The people involved were not villains. Each structural change was a "necessary compromise." Each investor condition was rational. The structural lesson: when a non-profit depends on commercial capital to fund its mission, the capital's interests will eventually dominate. This is not a moral failing. It is an economic inevitability (Weisbrod, 2004). The conditions are always reasonable in isolation. In aggregate, they bend the mission toward the economics.

The critical question for any AI governance institution is not "do the founders have good intentions?" but "does the structure create sustainable economics that do not require the mission to bend?"

### 7.5 The Broader Pattern

OpenAI is the most visible example, but the pattern is widespread.

**Open-washing.** Meta releases Llama under a license that restricts commercial use for any organization with more than 700 million monthly active users---conveniently excluding Meta's competitors while claiming "open source" positioning. Google launched the Agent2Agent (A2A) protocol in April 2025 with 50+ partners, then contributed it to the Linux Foundation two months later. The pattern: a hyperscaler designs a standard serving its platform interests, then contributes it to a neutral foundation for the appearance of community governance. Community governance arrives after the critical design decisions have been made.

**The maintainer sustainability crisis.** The 2024 Tidelift State of the Open Source Maintainer Report found that 60% of open-source maintainers are unpaid. Only 12% earn most or all of their income from maintenance work. 44% of unpaid maintainers would like to be paid but have no mechanism (Tidelift, 2024). This is a structural failure: the open-source model the technology industry depends on has no sustainable economic model for its maintainers (Eghbal, 2020). The Log4j vulnerability of 2021---affecting virtually every Java application on earth---was maintained by volunteers.

**Geographic bias.** AI governance standards are overwhelmingly set in Silicon Valley and Brussels. ASEAN---over 670 million people, rapidly growing AI adoption---is largely absent from global standard-setting, because the institutional models for standards are headquartered in the US or EU (Cihon et al., 2020).

### 7.6 Design Hypotheses

Given the structural deficiencies described above, what would a foundation designed specifically for AI governance innovation look like? The following are design hypotheses---principles that might address the identified problems. They are presented as one attempt at a solution, not as proven advantages.

**Hypothesis 1: Legal Structure Should Prevent Mission Drift by Design**

If OpenAI's lesson is that mission bends to economics, the structural response is to make mission deviation legally and practically difficult---not through good intentions, but through constitutional architecture.

A Company Limited by Guarantee (CLG) structure under Singapore law provides several relevant properties (Tan, 2014). It cannot distribute profits. There are no shares, no shareholders, no dividends. Surplus must be reinvested in the mission. The CLG structure is non-charity---the foundation is not a registered charity and does not pursue Institute of Public Character (IPC) status, which would introduce Commissioner of Charities oversight constraints inappropriate for a standards body.

But legal structure alone is insufficient. OpenAI was also a non-profit. The additional design element is entrenched constraints---provisions that require extraordinary process to change. Eleven constraints are entrenched behind a process requiring 90% board approval, 80% member approval by headcount (not weighted votes), and 12 months of public notice before any change can take effect:

1. Non-profit purpose (CLG structure prevents profit distribution)
2. No shares or dividends (structural prevention of equity extraction)
3. Funding and governance separation (funders cannot buy governance rights)
4. One-person-one-vote (equal member voice regardless of contribution)
5. Licence stability (no retroactive changes to released licences)
6. Contributor protection (patent protection survives all corporate changes)
7. Founder chair restriction (founder must relinquish chair once Phase 3 is triggered, may never serve as chair again)
8. Independent board majority (majority of directors must be independent at all times)
9. Community voice (major changes require public RFC process)
10. Winding-up IP survival (open-source code and specifications survive dissolution under their existing licences)
11. Anti-circumvention (no structural arrangement may defeat the intent of entrenched provisions)

An honest caveat: Singapore law does not recognize truly "unamendable" constitutional provisions (Tan, 2014). The word "entrenched" is used rather than "inviolable." The extreme process barriers make amendment practically impossible without overwhelming consensus, but they do not make it legally impossible. This is stated explicitly in the foundation's anchor documents: "We prefer extreme difficulty to false promises."

**Hypothesis 2: Patents Should Protect the Community, Not Monetize It**

The design hypothesis inverts the typical patent playbook: patents exist to protect community members from extraction, not to extract from the community.

What exists today: the code is released under the Apache 2.0 open-source license, which means anyone can use, modify, and commercialize it---permanently and irrevocably. The license also includes an automatic patent grant (Section 3): every user receives a perpetual, royalty-free right to use the patented technology. This is real and enforceable now.

The proposed additional mechanism is a Patent Covenant---a binding commitment that would extend protection beyond what Apache 2.0 provides, automatically covering SMEs, educators, researchers, developers, and consultants. The covenant would exclude large managed-service providers who offer the technology as a hosted service without contributing back---the hyperscaler extraction pattern. The specific thresholds and enforcement mechanisms are design proposals, not finalized commitments.

Whether a Patent Covenant would hold under real legal pressure is untested. Its value may be more deterrent than enforcement---making extraction legally risky enough that well-advised companies avoid it.

**Hypothesis 3: Contributors Deserve Structured Economic Participation**

Open source has a martyrdom problem. Most foundations offer contributors attribution and satisfaction (Eghbal, 2020). This is not enough.

What exists today: Apache 2.0 contributors retain copyright on their contributions. They can use, license, and commercialize their own work without restriction. This is standard open-source practice.

The proposed model goes further, designing mechanisms for structured revenue sharing with contributors---a dividend pool funded by patent licensing revenue, formal enumeration of contributor rights, and explicit economic participation. These are design proposals. No patent licensing revenue has been generated. No revenue-sharing mechanism has been tested. The hypothesis is that structured economic participation would attract and retain contributors better than attribution alone.

**Hypothesis 4: Founders Must Be Structurally Compelled to Leave**

The most common failure mode for mission-driven organizations is founder dependency. The founder's vision, relationships, and authority become indistinguishable from the organization itself. When the founder leaves, the organization collapses. When the founder stays too long, the organization cannot evolve beyond the founder's limitations.

The proposed model addresses this with mandatory transition:

- Phase 1 (incorporation): Founder serves as Director and Chair (practical necessity for solo-founder CLG)
- Phase 2 (10 Members): Founder may not chair any Board committee
- Phase 3 (30 Members + 3 years): Founder must relinquish Board Chair within 90 days; may hold a Board seat only if elected through normal Community-Elected Director process
- Permanent restriction: Founder may NEVER serve as Chair after Phase 3
- Permanent restriction: Founder may not chair any Board committee after Phase 2

The board composition requirements reinforce this. At full maturity (Phase 3: 30+ Members, 3+ years), the board comprises three estates: up to 6 Independent Directors (majority), up to 3 Community-Elected Directors, and up to 2 Institutional Directors---with corporate sponsors explicitly excluded from governance (zero board seats, zero voting rights). This three-estate model ensures that no single interest group can dominate.

The deeper design principle: the founder's job is to build an institution that no longer needs the founder. If the institution cannot function without its creator, it is not an institution. It is a personal project with elaborate documentation.

**Hypothesis 5: IP Transfer Should Be Complete and Irrevocable**

The proposed model requires full and irrevocable transfer of all open-source IP to the foundation. All specifications (CC BY 4.0) and reference implementations (Apache 2.0) are foundation-owned from the start. Contributors retain their own copyright on contributions and grant an Apache 2.0 license, but the foundation holds all IP directly---not through licensing arrangements, not through graduated milestones, not contingent on revenue targets.

This eliminates the ambiguity that plagues foundations where IP ownership is distributed or conditional: the foundation owns it, full stop, and that ownership survives any changes to the contributor's circumstances.

The trade-off is real: the contributor gives up control before the foundation has proven its capacity. The counterargument is that conditional IP transfer creates exactly the kind of leverage that enables mission drift (Cornforth, 2012)---"we'll complete the transfer when you meet our conditions" is structurally identical to "we retain the ability to withhold IP." Clean, unconditional transfer removes this leverage.

**Hypothesis 6: Plan for Failure Explicitly**

Most institutions plan for success. The proposed model plans for failure. Twenty-six specific failure scenarios are documented across five categories---including scenarios where the model itself proves unworkable and where both the foundation and its contributors fail simultaneously.

The critical design decision: perpetual irrevocable licenses ensure open-source code survives under Apache 2.0 even if every institutional entity ceases to exist. Standards remain under CC BY 4.0. The proposed Patent Covenant would provide additional protections that survive corporate dissolution. The technology is designed to outlive any particular institution.

The anchor documents state: "We do not know if this will work" (Hong, 2026). This is the appropriate starting position for any institutional experiment.

---

## 8. Case Study: The Terrene Foundation

The Terrene Foundation---a Singapore Company Limited by Guarantee maintaining open standards for enterprise AI governance---demonstrates the Constrained Organization in practice. It is not merely a foundation that publishes standards about AI governance. It operates using the architecture those standards prescribe. The foundation is a constrained organization.

### 8.1 Trust Plane (Human-Defined)

The Trust Plane is the 77-clause constitution with 11 entrenched provisions. It defines organizational boundaries:

- **Anti-capture mechanisms**: Funding and governance are structurally separated. Corporate sponsors have zero governance rights---no board seats, no voting rights, no veto power. One-person-one-vote applies regardless of contribution level. Mandatory founder transition ensures no individual accumulates permanent authority.

- **IP protection**: All open-source IP is fully and irrevocably transferred. Specifications are CC BY 4.0. Reference implementations are Apache 2.0. Winding-up provisions ensure code and standards survive dissolution.

- **Phased governance**: Phase 1 (incorporation), Phase 2 (10 Members), Phase 3 (30+ Members, 3+ years). The governance model evolves as the community grows. Many provisions behave differently across phases, preventing premature complexity while ensuring mature governance as the foundation scales.

- **Three-estate board** (Phase 3): Up to 6 Independent Directors (majority), up to 3 Community-Elected Directors, up to 2 Institutional Directors. This structure prevents any single constituency from dominating.

### 8.2 Execution Plane (AI-Agent-Operated)

The foundation's knowledge base operations are run by AI agents. This is the Execution Plane:

- **20 specialized AI agents** across 7 categories manage research, drafting, cross-referencing, quality assurance, governance checking, security review, strategy analysis, and publication preparation.

- **Specific agent roles**: Standards experts for CARE, EATP, CO, and COC. A constitutional expert who knows the 77 clauses. A security reviewer who scans for exposed secrets. An intermediate reviewer for quality. A deep analyst for failure analysis. A publication expert for academic submissions.

- **Every paper in this series** was produced using this process: AI agents drafted, the author directed, AI revised, the author corrected, the cycle repeated until the result was honest and useful.

### 8.3 Trust Verification (EATP)

Agent actions are traceable to the organizational root of authority:

- The master directive (organizational anchor documents) constitutes the Genesis Record---the root from which all delegation flows.

- Constraint envelopes are implemented as architectural enforcement rules: naming conventions enforce terminology consistency, security rules prevent exposure of sensitive information, constitutional consistency rules ensure companion documents never contradict the authoritative constitutional text, publication standards enforce citation density and honest limitations.

- **10 hook scripts (pre-execution, post-execution, and lifecycle)** including anti-amnesia mechanisms ensure critical rules survive context window compression. These operate outside the AI's context window---they cannot be overridden by conversational instruction.

### 8.4 Institutional Knowledge (CO Five-Layer)

The five-layer architecture is not theoretical. It is operational:

- **Layer 1 (Intent)**: 20 agents with domain-specific expertise spanning standards, architecture, strategy, review, management, and publication.
- **Layer 2 (Context)**: Rules, skills, and reference documentation form a living institutional handbook that provides relevant context based on current task.
- **Layer 3 (Guardrails)**: Pre-execution validation hooks with defense-in-depth. Multiple layers catch what any single layer misses. Anti-amnesia hooks re-inject critical rules after context compression.
- **Layer 4 (Instructions)**: 14 structured workflows with approval gates. Research flows through analysis before implementation. Publications flow through review before submission. Constitutional changes flow through consultation before adoption.
- **Layer 5 (Learning)**: Observation logs record patterns across sessions. Instinct evolution identifies recurring behaviors. Knowledge compounds.

### 8.5 Concrete Numbers

The foundation is a working system, not a slide deck:

- 77-clause constitution with 11 entrenched provisions
- 20 specialized AI agents across 7 categories
- 14 structured workflows with approval gates
- 13 operational rules (global and scoped)
- 10 hook scripts (pre-execution, post-execution, and lifecycle)
- 26 documented failure scenarios
- Full conversation histories retained as audit trails

Whether these numbers constitute a meaningful scale is an open question. The foundation has one primary contributor and no constituted board. The constrained organization model is demonstrated but not proven at scale.

---

## 9. Experimental Observations

This paper was produced using the constrained organization methodology it describes. The production process itself constitutes experimental evidence---a small-scale but genuine test of the framework.

### 9.1 Trust Plane Interventions

During the production of this paper and its companions in the series, the author made the following categories of Trust Plane intervention:

- **Factual accuracy**: 14 instances where AI output contained inaccurate claims, unsupported assertions, or misleading framings that required correction.
- **Overstatement**: 8 instances where AI presented design hypotheses as proven advantages, theoretical models as demonstrated results, or aspirational architecture as operational reality.
- **Marketing language**: 6 instances where AI used persuasive rather than analytical language---the kind of phrasing that sounds good but obscures rather than illuminates.

The AI could not distinguish "honest" from "persuasive." This distinction is a Trust Plane judgment.

### 9.2 Mirror Thesis Manifestation

The AI agents produced competent institutional analysis at speed the author could not match alone. They cross-referenced multiple documents, identified inconsistencies, structured arguments, and generated prose.

They could not judge when a governance claim exceeded its evidence. They could not tell when an analogy served marketing rather than analysis. They could not recognize when the "honest limitations" section was itself performing honesty rather than being honest.

These judgments were the author's unique contribution---the Trust Plane correcting the Execution Plane.

### 9.3 Convention Drift

The AI defaulted to academic hedging rather than the direct style specified by the organizational knowledge base. Phrases like "it may be argued that" and "one could reasonably conclude" replaced the direct "this is what we claim, and here is the evidence." This required repeated correction---a textbook example of convention drift, where the AI follows generic academic conventions rather than organizational ones.

### 9.4 Anti-Amnesia in Practice

Critical rules established early in sessions---naming conventions, terminology standards, the distinction between "design hypothesis" and "proven advantage"---were lost midway through long sessions as context compressed. The anti-amnesia hooks (Layer 3 guardrails) re-injected these rules, catching violations that would have passed without architectural enforcement.

### 9.5 The Synthesis

The author could not produce these papers at this speed. The AI could not produce these papers at this quality. Neither could do what the combination achieved. This is the claim of the Constrained Organization: the synthesis of human trust judgment and AI execution produces outcomes that neither achieves alone---not because of some mystical synergy, but because the architectural separation allows each to do what it does best.

---

## 10. Broader Impact

### 10.1 Labor and Displacement

The Mirror Thesis has a dual nature that must be addressed honestly.

Used well, it identifies uniquely human contributions and invests in their development. Organizations that understand the Mirror Thesis invest in judgment, relationships, contextual wisdom, creative synthesis, emotional intelligence, and cultural navigation---because these are now visible as the distinctive human value, separated from the execution tasks that AI handles.

Used badly, it becomes a tool for identifying roles to eliminate. Management deploys the mirror onto workers, not the reverse. The framework identifies what tasks can be automated; it does not guarantee that freed-up human capacity is invested in rather than eliminated. CARE provides a governance philosophy---prescription is not enforcement. Whether organizations use the Mirror Thesis to invest in human development or to justify layoffs is a management decision that no framework can force.

### 10.2 Access and Equity

Building a Constrained Organization requires significant institutional knowledge engineering. The five-layer CO architecture requires investment in defining agent roles, building knowledge bases, establishing guardrails, designing workflows, and creating learning systems. Organizations with weak institutional knowledge---often those that need better governance most---have the most to gain and the least capacity to build.

This risks widening inequality: well-resourced organizations build constrained organizations and compound their institutional intelligence, while under-resourced organizations fall further behind. Open standards and open implementations (CC BY 4.0 and Apache 2.0) mitigate this partially by making the architecture freely available. But access to architecture is not the same as capacity to implement.

### 10.3 Standards Body Design

If the proposed institutional model proves viable, it demonstrates that AI governance standards can be maintained by purpose-built institutions rather than repurposed software foundations. This has implications for how future governance standards bodies are designed---particularly the separation of funding from governance, the use of entrenched provisions, and the explicit planning for institutional failure modes.

### 10.4 Non-Profit Transparency

The explicit failure planning and falsification criteria represent a transparency model that other non-profits could adopt. Most non-profit institutions describe their aspirations; few state the specific conditions under which they should be abandoned. The question is whether radical transparency attracts or deters participation.

### 10.5 Geographic Equity

An ASEAN-based governance standards body would contribute to geographic diversification in AI governance---currently dominated by US and EU institutions. Singapore bridges East and West, with deep ASEAN ties and a reputation for institutional quality. Whether Singapore can serve as a credible neutral convener for the region is an open question, but the institutional density---ASME, SBF, NTUC, Enterprise SG, AI Singapore, IMDA, all accessible in one city-state---suggests the structural preconditions exist.

The path from Singapore to ASEAN (670 million+ people) to global relevance requires partnerships that do not yet exist. Singapore is an excellent laboratory. Whether the experiment scales beyond the laboratory is a separate question.

---

## 11. Honest Limitations

### 11.1 Constraint Gaming

Any constraint-based system can be gamed. An AI that technically complies with every constraint while violating their intent is the central operational risk of the Constrained Organization. The naming convention says "Terrene Foundation"; the AI uses "Terrene Foundation" while framing the content in ways that undermine the foundation's mission.

Transparency and evolutionary trust address this partially: Trust Plane observation detects gaming patterns, and constraints are updated. Whether this evolutionary approach suffices at scale---with thousands of agents across hundreds of organizations---is undemonstrated.

### 11.2 Power Asymmetries

CARE does not solve the fundamental power asymmetry: management deploys AI; workers experience the consequences. The Mirror Thesis identifies human value but does not prevent organizations from using the identification to eliminate rather than invest. The framework provides architecture; it does not guarantee equitable deployment.

### 11.3 The Circularity Critique

The Constrained Organization is defined by a framework created by humans. The Mirror Thesis identifies "uniquely human" competencies through human analysis. The Trust Plane is "permanently human" by normative choice, not empirical necessity. The entire architecture rests on axioms that are adopted, not proven.

This is acknowledged openly. The question is not whether the axioms are provably correct but whether they generate useful governance outcomes. If they do, the circularity is a feature (practical design choice) not a bug (logical flaw). If they do not, the falsification conditions in Section 12 will demonstrate it.

### 11.4 Institutional Vulnerabilities

**Founder dependency**: The person proposing this institution created CARE, designed EATP, built Kailash, holds council positions on ASME and SBF, and teaches at Singapore Management University. Until a second major contributor emerges, the foundation is indistinguishable from a one-person project with elaborate governance documentation. The board has not been constituted. No independent director has been recruited. Governance structures can create the conditions for independence, but they cannot manufacture it. Independence requires people who are genuinely independent.

**The bootstrapping problem**: The revenue model---membership dues, certification fees, government grants, patent licensing---is theoretical. No revenue has been collected from any source. The reinforcing flywheel has not completed a single rotation. The risk is that it never starts. Many well-designed foundations have failed because they solved a problem that was real but not urgent enough to motivate adoption.

**Singapore market size**: Global AI standards are being set now---A2A, MCP, the EU AI Act---while this foundation is still being constituted. A Singapore-first standard risks being swept aside by less elegant but more widely adopted alternatives. The "Singapore first, then ASEAN" principle is disciplined, but a standard that only Singapore uses is a local convention, not a global standard.

**Enforcement cost**: Enforcing patents against hyperscalers with unlimited legal budgets is prohibitively expensive for a non-profit. The proposed Patent Covenant's primary value would be deterrence, not enforcement---making extraction legally risky enough that rational actors avoid it. But a determined bad actor with sufficient resources could overwhelm the defense.

**Unproven governance**: The governance structures look good on paper. So did OpenAI's original non-profit structure. The question is whether they hold under real pressure: when a funder demands concessions, when a hyperscaler offers partnership contingent on governance changes, when revenue falls short and the temptation to compromise becomes existential. This cannot be answered yet. The anchor documents acknowledge it: "We do not know if this will work. We believe the model is sound in theory. But markets are unpredictable, execution is hard, and we might fail."

### 11.5 The Open-Washing Reflexive Critique

The founding contributor created the IP and retains commercial products built on the open standards. One could argue this creates a structural advantage that contradicts the neutrality being claimed.

The counter-argument: all open-source IP has been fully and irrevocably transferred to the foundation. The specifications are CC BY 4.0. The reference implementations are Apache 2.0. The foundation owns them directly---not through licensing, not conditionally. Anyone can use the code, fork it, compete with the contributor. The contributor has the same rights to the open-source IP as any other user: the Apache 2.0 license in the repository. The contributor may build proprietary products on the open standards---this is by design, not a loophole. The intended model is that the foundation publishes open standards, and anyone (including the contributor) builds commercial products on top.

### 11.6 What CARE Does Not Solve

CARE does not solve displacement economics---it provides a governance philosophy, not an economic policy. CARE does not guarantee regulatory compliance---it provides architecture that can be adapted to regulatory requirements, but it is not itself a compliance framework. CARE does not address democratic legitimacy (Rahwan, 2018)---who decides what values go into the Trust Plane is a question the framework identifies but does not resolve. CARE does not provide model-level alignment (Bai et al., 2022)---the Constrained Organization assumes AI models that follow instructions, and addresses what to do with that capability at the organizational level, not the model level.

---

## 12. Falsification Criteria

A framework that does not state conditions for its own failure is not a framework. It is marketing. The willingness to specify failure conditions is itself a form of accountability.

### 12.1 Organizational Form

- **If the Dual Plane separation proves unimplementable across five or more deployments**, the architectural model should be revised. The separation may be conceptually clear but operationally impractical.

- **If the six competency categories cannot be reliably identified across ten or more deployments**, the Mirror Thesis should be abandoned. The categories may be artifacts of the author's analysis rather than robust phenomena.

- **If constrained organizations show no governance advantage over traditional enterprises with AI tools** in controlled comparison, the form is not distinct---it is merely a well-documented AI-assisted enterprise with aspirational branding.

### 12.2 Trust Protocol

- **If EATP trust lineage chains prove too computationally expensive for real-time verification** in production deployments, the protocol requires fundamental architectural revision.

- **If the verification gradient (QUICK/STANDARD/FULL) does not align with actual organizational risk appetite** across diverse deployments, the trust posture model is not capturing real organizational behavior.

### 12.3 Institutional Design

- **If after 3 years, fewer than 10 organizations have adopted EATP-conforming implementations**, the standard has failed to demonstrate practical value. Standards without adoption are academic exercises.

- **If after 2 years, no second major contributor has emerged**, the foundation has failed to attract the independent investment that distinguishes an institution from a personal project.

- **If the proposed Patent Covenant proves unenforceable in its first legal test**, the community shield is illusory, and the entire IP strategy requires fundamental revision.

- **If contributor satisfaction surveys show less than 50% confidence in Foundation governance**, the governance structures have failed their primary purpose regardless of how well they look on paper.

- **If the founder has not transitioned as specified**---relinquishing the chair once Phase 3 is triggered (30 Members and 3+ years since incorporation)---the mandatory transition is a lie, and the governance model has failed at its most basic commitment.

If this model does not work, these are the metrics that will demonstrate it.

---

## 13. The Strongest Argument Against Self-Interest

The code is Apache 2.0 on GitHub. Anyone can use it, fork it, compete with me. That is the trust signal.

If this were primarily about extraction, the rational strategy would be different: keep the IP proprietary, license it, build a SaaS platform, seek venture capital. Every commercial AI governance company follows this path. The code being open and irrevocably licensed is the one thing that cannot be argued away.

Whether the founder will follow through on the proposed governance transitions---stepping back from leadership, transferring authority---is a fair question that can only be answered by observing the actions. No one should trust the commitment until they see it happen.

---

## 14. Conclusion

Enterprise AI governance has been framed as compliance, risk management, and values. This paper reframes it as organizational design.

The Constrained Organization---integrating governance philosophy (CARE), trust verification (EATP), and institutional knowledge methodology (CO)---proposes a new organizational form where humans define the envelope and AI executes within it, with cryptographic verification that this relationship holds. Five properties distinguish it from existing forms: architectural separation, verifiable trust lineage, structured institutional knowledge, graduated autonomy, and compounding knowledge.

The institutional question is inseparable from the organizational one. Who stewards the standards that make constrained organizations possible? Neither corporate-funded foundations nor developer meritocracies are designed for this. Six design hypotheses---legal structure preventing mission drift, patents protecting community, contributor economic participation, mandatory founder transition, complete IP transfer, and explicit failure planning---propose a different institutional form.

The Terrene Foundation demonstrates the model: a standards body whose operations are run by AI agents within constitutional constraints. The papers describing the framework were produced by the framework. The conversation histories are the audit trail. The corrections are the Trust Plane in action.

Whether the Constrained Organization is genuinely new or merely a well-documented AI-assisted enterprise remains an empirical question. Whether the institutional design survives real pressure is unknown. Whether the founder follows through on the governance transitions is unproven.

What is known: the code is open, the structures are published, the failure conditions are stated. What remains is the hardest part: execution.

---

## References

Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. _arXiv:2212.08073_.

Bainbridge, L. (1983). Ironies of Automation. _Automatica_, 19(6), 775-779.

Cihon, P., Maas, M. M., & Kemp, L. (2020). Should Artificial Intelligence Governance be Centralised? Design Lessons from Internet Governance. _AIES '20_.

Cornforth, C. (2003). _The Governance of Public and Non-Profit Organizations_. Routledge.

Cornforth, C. (2012). Nonprofit Governance Research: Limitations of the Focus on Boards and Suggestions for New Directions. _Nonprofit and Voluntary Sector Quarterly_, 41(6), 1116-1135.

Dafoe, A. (2018). AI Governance: A Research Agenda. Centre for the Governance of AI, University of Oxford.

Dal Bo, E. (2006). Regulatory Capture: A Review. _Oxford Review of Economic Policy_, 22(2), 203-225.

DuPont, Q. (2017). Experiments in Algorithmic Governance. In _Bitcoin and Beyond_. Routledge.

Eghbal, N. (2020). _Working in Public: The Making and Maintenance of Open Source Software_. Stripe Press.

El Faqir, Y., Arroyo, J., & Hassan, S. (2020). An Overview of Decentralized Autonomous Organizations on the Blockchain. _ACM Group '20_.

Emery, F. E. & Trist, E. L. (1960). Socio-technical Systems. In _Management Sciences_, Vol. 2. Pergamon.

Engin, Z. (2025). Human-AI Governance (HAIG): A Trust-Utility Approach. _arXiv:2505.01651_.

European Union. (2024). Regulation (EU) 2024/1689 (AI Act). _Official Journal of the European Union_.

Floridi, L. & Cowls, J. (2019). A Unified Framework of Five Principles for AI in Society. _Harvard Data Science Review_, 1(1).

Fortune. (2026). OpenAI has changed its mission statement 6 times in 9 years. February 23, 2026. https://fortune.com/2026/02/23/openai-mission-statement-changed-restructuring-forprofit-business/

Google. (2025). Announcing the Agent2Agent Protocol (A2A). Google Developers Blog, April 2025.

Gorwa, R. (2019). What Is Platform Governance? _Information, Communication & Society_, 22(6), 854-871.

Hagendorff, T. (2020). The Ethics of AI Ethics. _Minds and Machines_, 30, 99-120.

Haidt, J. (2001). The Emotional Dog and Its Rational Tail. _Psychological Review_, 108(4), 814-834.

Harre, M. (2025). From Firms to Computation: AI Governance and the Evolution of Institutions. _arXiv:2507.13616_.

Hassan, S. & De Filippi, P. (2021). Decentralized Autonomous Organization. _Internet Policy Review_, 10(2).

Hong, J. (2026a). CARE: Collaborative Autonomous Reflective Enterprise---A Core Thesis. White Paper Series, Version 2.1. Terrene Foundation. https://terrene.foundation/publications/care-core-thesis.

Hong, J. (2026b). Enterprise Agent Trust Protocol (EATP)---A Core Thesis. White Paper Series, Version 2.2. Terrene Foundation. https://terrene.foundation/publications/eatp-core-thesis.

Hong, J. (2026c). Cognitive Orchestration (CO)---A Core Thesis. White Paper Series, Version 1.1. Terrene Foundation. https://terrene.foundation/publications/co-core-thesis.

Hong, J. (2026). First Principles. Foundation Anchor Document 00. Terrene Foundation.

Hu, B. A. & Rong, H. (2026). Sovereign Agents: Towards Infrastructural Sovereignty and Diffused Accountability in Decentralized AI. _arXiv:2602.14951_.

Humberd, B. & Latham, S. (2026). When AI Becomes an Agent of the Firm: Examining the Evolution of AI in Organizations Through an Agency Theory Lens. _Journal of Management Studies_, 63(2), pp. 668-694.

IMDA. (2020). _Model AI Governance Framework_, 2nd ed. Singapore.

Jobin, A., Ienca, M., & Vayena, E. (2019). Global Landscape of AI Ethics Guidelines. _Nature Machine Intelligence_, 1, 389-399.

Jones, M. B. (2007). The Multiple Sources of Mission Drift. _Nonprofit and Voluntary Sector Quarterly_, 36(2), 299-307.

Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at Work: The New Contested Terrain of Control. _Academy of Management Annals_, 14(1), 366-410.

Klein, G. (1998). _Sources of Power: How People Make Decisions_. MIT Press.

Kolbjornsrud, V. (2024). Designing the Intelligent Organization: Six Principles for Human-AI Collaboration. _California Management Review_, 66(2), pp. 44-64.

Meta. (2024). Llama 3 Community License Agreement.

Methnani, L., Aler Tubella, A., & Dignum, V. (2021). Variable Autonomy for Meaningful Human Control. _Frontiers in AI_, 4:737072.

Nahapiet, J. & Ghoshal, S. (1998). Social Capital, Intellectual Capital, and the Organizational Advantage. _Academy of Management Review_, 23(2), 242-266.

NIST. (2023). _AI Risk Management Framework (AI RMF 1.0)_. NIST AI 100-1.

O'Mahony, S. (2007). The Governance of Open Source Initiatives: What Does It Mean to Be Community Managed? _Journal of Management and Governance_, 11(2), 139-150.

OECD. (2019, updated 2024). _OECD AI Principles_. OECD/LEGAL/0449.

Ostrom, E. (1990). _Governing the Commons: The Evolution of Institutions for Collective Action_. Cambridge University Press.

Parasuraman, R. & Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. _Human Factors_, 39(2), 230-253.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A Model for Types and Levels of Human Interaction with Automation. _IEEE Transactions on Systems, Man, and Cybernetics---Part A_, 30(3), 286-297.

Polanyi, M. (1966). _The Tacit Dimension_. University of Chicago Press.

Rahwan, I. (2018). Society-in-the-Loop: Programming the Algorithmic Social Contract. _Ethics and Information Technology_, 20, 5-14.

Riehle, D. (2012). The Single-Vendor Commercial Open Source Business Model. _Information Systems and e-Business Management_, 10(1), 5-17.

Santoni de Sio, F. & van den Hoven, J. (2018). Meaningful Human Control over Autonomous Systems. _Frontiers in Robotics and AI_, 5, 15.

Sheridan, T. B. & Verplank, W. L. (1978). _Human and Computer Control of Undersea Teleoperators_. MIT.

Shneiderman, B. (2022). _Human-Centered AI_. Oxford University Press.

Simcoe, T. (2012). Standard Setting Committees: Consensus Governance for Shared Technology Platforms. _American Economic Review_, 102(1), 305-336.

Stigler, G. J. (1971). The Theory of Economic Regulation. _Bell Journal of Economics_, 2(1), 3-21.

Tan, K. Y. L. (2014). _An Introduction to Singapore's Constitution_. Talisman Publishing.

TechCrunch. (2025). OpenAI completes its for-profit recapitalization. October 28, 2025.

Tidelift. (2024). 2024 State of the Open Source Maintainer Report. Survey of 400+ open source maintainers.

Trist, E. L. & Bamforth, K. W. (1951). Some Social and Psychological Consequences of the Longwall Method of Coal-Getting. _Human Relations_, 4(1), 3-38.

Weisbrod, B. A. (2004). The Pitfalls of Profits. _Stanford Social Innovation Review_, Winter 2004.

---

## A Note on How This Paper Was Produced

This paper was produced using the constrained organization methodology it describes. The production process is itself a case study for the framework.

The initial drafts were generated by AI agents: research analysts that explored the knowledge base and source repositories, standards experts that verified terminology consistency, a security reviewer that scanned for exposed secrets, and a publication expert that checked academic standards. The author directed every iteration with specific instructions: remove claims that cannot be verified, strip marketing language, ensure honest limitations are genuinely honest rather than performing honesty, explain technical terms for non-technical readers.

The author made direct edits to tone, phrasing, and substance throughout. Multiple rounds of revision followed, each narrowing the gap between what the agents produced and what the author judged to be honest and useful.

This paper merges two previously separate documents---one focused on institutional design (who stewards AI governance?) and one focused on organizational form (what is a Constrained Organization?)---because the questions are inseparable. The institutional steward must itself be a constrained organization.

The tools used were Claude Code (Anthropic) with 18 specialized subagents. The full conversation history, including every instruction, every correction, and every piece of content the author rejected, is retained by the author.

---

_See also: Hong, J. (2026). "CARE: A Core Thesis" (Hong, 2026a) for the governance framework. "EATP: A Core Thesis" (Hong, 2026b) for the trust verification protocol. "CO: A Core Thesis" (Hong, 2026c) for the methodology._
