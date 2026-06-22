# PACT: A Core Thesis

**Principled Architecture for Constrained Trust**

_Why Organizational Architecture Is the Missing Layer for Governed AI at Scale_

**Author**: Dr. Jack Hong, Singapore Management University

**Status**: Ratified Terrene Foundation standard (v1.0). Promoted from Working Architecture on 2026-06-21; see Section 16 for the promotion record.

**Version**: 1.0 | June 2026 (promoted from 0.1-WA, March 2026)

**License**: CC BY 4.0

---

## Abstract

Enterprise AI governance has philosophy, trust protocols, and knowledge methodology. It lacks the organizational architecture that makes governed AI tractable when hundreds of agents operate across multi-level hierarchies. This paper presents PACT, a specification for structuring accountable delegation in any organized group deploying autonomous agents.

I contribute four mechanisms. The Accountability Grammar constrains organizational modeling to three node types (Department, Team, Role) with the invariant that every container has a named human accountable for it. Recursive envelope delegation enables supervisors to define operating boundaries for direct reports only; envelopes compose through intersection and can only tighten through delegation chains. A knowledge clearance framework separates information access from organizational rank, adapted from Singapore Government classification. Positional addressing gives every entity a unique, traversable address encoding both containment and accountability.

These mechanisms were extracted from implementations across enterprise (a production enterprise agent platform deployment), human resources (Arbor, open source), and regulatory compliance (financial services designed for MAS infrastructure). The formalization is a design contribution; the underlying patterns are observable in military command, government administration, hospital governance, and financial regulation. I position PACT against recent AI agent delegation frameworks (Kolt, 2025; South et al., 2025; Tomasev et al., 2026) as addressing organizational architecture rather than delegation mechanics or authentication protocols.

---

## Disclosure

I developed PACT and the implementations from which it was extracted. The patterns originated during construction of a production enterprise agent platform and were validated against Arbor (an open-source HRIS platform), the PACT implementation (kailash-pact as the governance engine primitive, and the PACT Platform as the human judgment surface; collectively 133+ source modules, 4,191+ tests, Apache 2.0), and regulatory compliance architectures designed for financial services.

**Provenance and Independence**: The architectural patterns in PACT were extracted from a production enterprise deployment. The PACT specification is independent of any commercial implementation; it is CC BY 4.0. The Terrene Foundation, which publishes this specification, is a sovereign, independent entity with no structural relationship to any commercial entity. The Foundation owns all open-source IP (fully transferred, irrevocable). The constitution prevents open-washing, rent-seeking, and self-interest by any party, including the Founder.

**Implementation**: PACT is implemented in two layers, reflecting the ecosystem architecture:

- **kailash-pact** (Layer 1 primitive): The governance engine. GovernanceEngine, D/T/R addressing, constraint envelope propagation, verification gradient, and PACT for MCP middleware. Deterministic; no LLM required. Available as `pip install kailash-pact` (v0.12.0) from the Kailash Python SDK monorepo (github.com/terrene-foundation/kailash-py). The trust infrastructure is integrated into kailash-py v2.28.1 (`kailash.trust` namespace), whose MCP governance server enforces the verification gradient at runtime: an `eatp_verify` tool returns the four-level verdict (auto-approved / flagged / held / blocked), and held actions route through a hold queue for human approval.
- **PACT Platform** (Layer 3 entrypoint): The human judgment surface. Web dashboard (Next.js), mobile app (Flutter), and REST API. Org structure editor, constraint envelope configuration, approval queues for HELD actions, audit trail viewer, knowledge clearance management, shadow mode for simulation. Available at github.com/terrene-foundation/pact.

PACT for MCP provides governance middleware for MCP-compatible agents, enabling PACT envelope enforcement and EATP record generation within MCP tool-use sessions. The depth of enforcement is surface-dependent --- governance-grade interposition on Claude Code today, and narrower, mutation-level coverage with documented limits on other CLIs such as Codex and Gemini --- so naming a surface is not a claim of uniform coverage. It is a sub-module of kailash-pact, not a separate package.

I am the designer, builder, and evaluator. This dual role is a methodological limitation. This paper was written with AI assistance using Cognitive Orchestration for Research (COR). I directed all structural decisions, approved every paragraph, and can defend the work independently. Deliberation records are available on request. The universality claim rests on structural analysis of cross-domain governance patterns, not on empirical deployment in military, healthcare, or government contexts. Patents PCT/SG2024/050503 and P251088SG are pending. The PACT specification is CC BY 4.0; reference implementations are Apache 2.0 with automatic Section 3 patent grant. Implementing the specification independently does not require a patent license; the patents cover specific implementation mechanisms, not the architectural patterns themselves.

---

## 1. Introduction

A CFO delegates financial authority to a Head of Treasury, who delegates to a Cash Manager, who delegates to a Treasury Analyst. The analyst's AI agent processes payment reconciliations. When a payment error occurs, the accountability question cascades: Was the analyst authorized to process this amount? Did the Cash Manager's delegation exceed what the Head of Treasury granted?

In traditional organizations, these questions are answered by reading job descriptions, checking approval matrices, and interviewing managers. The answers are informal, inconsistent, and retrospective. When AI agents execute at machine speed across organizational boundaries, informal accountability becomes a structural failure.

The problem is not that organizations lack governance philosophy (Hong, 2026a), trust verification (Hong, 2026b), or knowledge methodology (Hong, 2026c). The problem is architectural: **how does a 500-person organization with agents at every role make envelope definition, knowledge access, and accountability tractable?**

Jobin, Ienca, and Vayena (2019) surveyed 84 AI ethics guidelines globally and found convergence on principles but divergence on implementation. Hagendorff (2020) identified a "deep gap" between ethical principles and operational practice. The EU AI Act (European Parliament, 2024) mandates human oversight for high-risk AI systems (Article 14) but specifies the legal requirement, not the organizational architecture. The NIST AI Risk Management Framework (NIST, 2023) provides a process model deliberately agnostic about governance structure. Shneiderman (2022) proposed high automation and high human control simultaneously but operationalized this through interface design rather than organizational architecture.

I address this implementation gap. The gap is not in principles; it is in the organizational structure that makes principles enforceable when AI agents act at scale.

This paper makes four contributions:

1. **The Accountability Grammar**: a three-node organizational model (D/T/R) with a constraint that forces every container to have a named human accountable for it. The result is structurally verifiable delegation chains.
2. **Recursive envelope delegation**: a three-layer composition architecture (Role/Task/Effective envelopes) with a monotonic tightening invariant ensuring downstream authority never exceeds upstream delegation.
3. **Knowledge clearance independent of seniority**: a five-level classification framework where information access follows need-to-know, not organizational rank.
4. **Positional addressing**: a deterministic addressing scheme encoding both organizational containment and accountability chains.

---

## 2. Background and Related Work

### 2.1 Organizational Design Theory

Why does organizational structure exist? The answer from sixty years of organizational theory converges on a single insight: structure compensates for the limits of human cognition. Simon (1947) established bounded rationality; March and Simon (1958) showed that organizational routines distribute decisions across structural positions because no individual can process all relevant information. Structure channels decision-making. PACT's operating envelopes formalize this channeling for AI agents: the envelope defines what the agent processes; everything outside it escalates to the human whose bounded rationality is better suited to the exception.

But what kind of structure? Weber (1947) analyzed bureaucratic hierarchy as authority flowing through defined positions. Perrow (1967) argued that organizational structure should match its technology. AI agents are a technology shift; hierarchical structures designed for human workers do not automatically provide the accountability architecture needed for autonomous agents. Galbraith (1973) deepened this with the information-processing view: organizations manage information through four strategies (rules/programs, hierarchy, targets/goals, and lateral relations). PACT addresses hierarchy (the D/T/R grammar and monotonic tightening) and lateral relations (cross-department bridges). The other two strategies (rules/programs and targets/goals) are addressed by CO's knowledge layers (Hong, 2026c); PACT is independently implementable without them, but organizations adopting both gain coverage across all four strategies.

What determines the right structural form? Mintzberg (1979) identified five configurations; Burns and Stalker (1961) drew the line between mechanistic structures (formalized, hierarchical, predictable) and organic structures (flexible, adaptive, informal). I place PACT on the mechanistic side deliberately. Governed AI at scale requires the traceability that mechanistic structures provide; organic structures sacrifice exactly the property PACT exists to enforce. This limits PACT's applicability to Mintzberg's Machine Bureaucracy and Divisionalized Form; it does not model Adhocracy well.

How do organizations balance specialization with coordination? Lawrence and Lorsch (1967) demonstrated that effective organizations balance differentiation (specialization into distinct units) with integration (coordination across them). The D/T/R grammar enforces differentiation through containment boundaries; bridges provide integration. Thompson (1967) analyzed boundary-spanning activities for managing interdependence across units; PACT's bridges formalize this concept with scoped, auditable channels. Williamson (1985) provided the transaction cost rationale: hierarchy is efficient when transactions are complex, recurring, and involve high asset specificity. Enterprise AI agent operations typically have this profile.

The sociotechnical systems tradition (Trist & Bamforth, 1951; Cherns, 1976) established that organizations are joint human-technical systems; you cannot optimize one subsystem independently of the other. PACT addresses the technical subsystem (formal structure, delegation mechanics, access control); the social subsystem (organizational culture, resistance to hierarchy, trust between humans) is outside scope. I acknowledge this limitation: a PACT implementation that ignores the social system will fail regardless of its architectural soundness.

Two theories from organizational economics are particularly relevant. Fama and Jensen (1983) showed that separating decision management (initiation and implementation) from decision control (ratification and monitoring) limits the power of individual agents to expropriate residual claimants. PACT's grammar encodes this: containers scope decision domains; roles provide the named control function. And incomplete contract theory (Hart, 1995; Hart & Moore, 1990) demonstrated that residual control rights determine who decides when contracts cannot anticipate every contingency. I model the operating envelope as a formalization of specified delegation boundaries, where residual authority (anything outside the envelope) reverts to the delegator. The analogy is structural rather than exact: Hart's residual rights concern unspecified contingencies; PACT's envelope explicitly specifies boundaries and treats everything outside as requiring escalation.

### 2.2 AI Governance

AI governance has converged on principles while diverging on implementation. Jobin et al. (2019) surveyed 84 AI ethics guidelines and found agreement on transparency, fairness, non-maleficence, responsibility, and privacy, but no agreement on how to operationalize them within organizations. Floridi et al. (2018) proposed the AI4People framework with five principles (beneficence, non-maleficence, autonomy, justice, explicability); Floridi and Cowls (2019) confirmed cross-framework convergence while acknowledging the gap between principles and practice.

Hagendorff (2020) analyzed this gap in detail, examining 22 guidelines and finding minimal practical impact. I read his analysis as revealing three persistent problems: (1) guidelines are addressed to developers rather than organizations, leaving institutional governance unspecified; (2) guidelines conflate technical and ethical concerns without distinguishing which require architectural solutions and which require cultural change; (3) most guidelines lack enforcement mechanisms ("Ethics has no enforcement mechanisms reaching beyond voluntary and non-binding cooperation," as Hagendorff puts it). PACT addresses the first and third of these. The D/T/R grammar and envelope architecture are organizational, not developer-facing. The monotonic tightening invariant and verification gradient are enforcement mechanisms, not advisory principles. Hagendorff's second gap (distinguishing technical from ethical) is outside PACT's scope; it is a framing problem, not an architecture problem.

The EU AI Act (European Parliament, 2024) represents the strongest regulatory attempt to require human oversight. Article 14 specifies that high-risk AI systems must include human oversight measures enabling users to "correctly interpret the high-risk AI system's output" and to "decide not to use the high-risk AI system, or to disregard, override or reverse the output." PACT's verification gradient operationalizes Article 14: the four outcome categories (auto-approved, flagged, held, blocked) provide the graduated override mechanisms the regulation requires, and the envelope architecture ensures that every autonomous action traces to the human authority who authorized it.

The NIST AI Risk Management Framework (NIST, 2023) defines a Govern function that "cultivates and implements a culture of risk management," but is deliberately agnostic about governance structure. Shneiderman (2022) proposed high automation and high human control simultaneously. PACT provides the organizational architecture that makes this combination tractable: high automation within envelopes, high human control at envelope boundaries.

The levels-of-automation literature provides the theoretical foundation for PACT's verification gradient. Sheridan and Verplank (1978) defined ten levels from full human control to full automation. Parasuraman, Sheridan, and Wickens (2000) extended this to four information-processing stages. Endsley and Kiris (1995) demonstrated the "out-of-the-loop" performance problem: situation awareness degrades as automation increases. PACT's gradient is an operationalization of levels-of-automation theory for organizational delegation: the four outcome categories (auto-approved, flagged, held, blocked) calibrate human involvement at the organizational level rather than the individual task level. The held zone specifically addresses Endsley's concern: it engages the human at the boundary where their judgment is needed, preserving situation awareness for the decisions that matter.

Bainbridge (1983) documented the ironies of automation: the more automated a system, the more critical (and degraded) the remaining human skills. PACT's design attempts to mitigate this irony: by engaging humans specifically at envelope boundaries (the held zone), rather than at every action (rubber-stamping) or no actions (skill atrophy), the architecture aims to keep human judgment exercised on genuinely challenging decisions.

### 2.3 AI Agent Delegation and Organizational Design

How should organizations govern AI agents? The question has generated substantial scholarly output since 2024, with principal-agent framings, organizational design proposals, and regulatory frameworks emerging in parallel. Kolt (2025) used principal-agent theory to characterize AI agent governance problems: information asymmetry, discretionary authority, and loyalty conflicts. He argued that conventional agency solutions (incentive design, monitoring, enforcement) may not work for agents that make uninterpretable decisions at unprecedented speed. Kolt identifies the problem; PACT provides one architectural response.

Humberd and Latham (2026) argued in the _Journal of Management Studies_ that AI's integration into firm decision-making parallels the emergence of the professional manager that prompted agency theory; as AI evolves from tool to agent of the firm, monitoring and control mechanisms must evolve with it. Jarrahi and Ritala (2025) proposed a principal-agent perspective on AI agents in the _California Management Review_, arguing this offers a more actionable framing than treating agents as autonomous entities. PACT's recursive envelope delegation is precisely a principal-agent mechanism: the envelope formalizes the delegation relationship these authors describe.

On organizational design specifically, Kolbjornsrud (2024) presented six principles for human-AI collaboration (addition, relevance, substitution, diversity, collaboration, explanation) and won the _California Management Review_ Best Article Award. Vantrappen (2025) extended organizational design thinking to "fluid organizations" where humans and AI agents cohabit. Vantrappen's argument is for fluidity; mine is for structure. This is a productive tension. Governed AI at scale requires the traceability that structured delegation provides; Vantrappen's fluidity sacrifices exactly the property PACT exists to enforce. Both approaches have a place; PACT is for organizations that prioritize accountability over adaptability.

Two recent technical papers address delegation mechanisms directly. South, Marro, Hardjono, Mahari, Whitney, Greenwood, Chan, and Pentland (2025) proposed AD/MIT, a framework for authenticated, authorized, and auditable delegation of AI agents, presented at ICML 2025. AD/MIT extends OAuth 2.0 with agent-specific credentials. Tomasev, Franklin, and Osindero (2026) from Google DeepMind proposed a framework for intelligent AI delegation that, as I read it, models delegation as a sequence of decisions involving task allocation, authority transfer, and trust mechanisms. Both operate at the delegation mechanics layer; neither addresses organizational structure. AD/MIT solves the authentication problem (who authorized this agent?); PACT solves the organizational architecture problem (how does delegation compose through hierarchy?). Tomasev et al. focus on dynamic delegation adaptation; PACT focuses on structural composition with monotonic tightening. These are complementary layers: AD/MIT or similar protocols could authenticate PACT's delegation records, and Tomasev et al.'s adaptive mechanisms could operate within PACT's structural constraints.

Singapore's Infocomm Media Development Authority published what it describes as the first national governance framework specifically for agentic AI (IMDA, 2026), specifying four dimensions: assessing and bounding risks upfront, making humans meaningfully accountable through significant checkpoints, implementing technical controls throughout the agent lifecycle, and enabling end-user responsibility through transparency. PACT operationalizes IMDA's second dimension (meaningful human accountability through checkpoints) through the verification gradient, and the third (technical controls) through envelope enforcement and knowledge clearance.

### 2.4 Organizational Modeling Notations

Existing notations model organizational structure. ArchiMate (The Open Group, 2019) has Business Actors, Business Roles, and Organizational Units. BPMN (OMG, 2014) uses pools and lanes. LDAP directories model Organization, OrganizationalUnit, and Person.

PACT is not a modeling notation. Modeling notations describe structure; PACT constrains and governs it. The distinction:

| Property                           | ArchiMate / UML / BPMN                | PACT                                                    |
| ---------------------------------- | ------------------------------------- | ------------------------------------------------------- |
| Accountability constraint          | Descriptive (can model, not enforced) | Enforced (every container must have a named person)     |
| Monotonic tightening               | Not modeled (permissions additive)    | Enforced (authority can only narrow through delegation) |
| Clearance independent of hierarchy | Limited (access follows role)         | Enforced (clearance follows need-to-know)               |
| Cryptographic backing              | No                                    | Yes (every governance action creates an EATP record)    |

An enterprise architect can model a PACT-conformant structure in ArchiMate. They cannot enforce the accountability constraint, monotonic tightening, or clearance independence using ArchiMate alone.

### 2.5 Access Control

Role-Based Access Control (Sandhu, Coyne, Feinstein, & Youman, 1996) governs what systems a user can access. RBAC is additive (permissions accumulate) and binary (permitted/denied). Attribute-Based Access Control (ABAC; Hu, Ferraiolo, Kuhn, Schnitzer, Sandlin, Miller, & Scarfone, 2014) moved beyond RBAC by evaluating policies against contextual attributes, and Next-Generation Access Control (NGAC; INCITS, 2020) supports policy composition across organizational boundaries.

PACT shares ABAC's context-awareness and NGAC's compositional character. Where PACT differs from both is in its organizational semantics. ABAC evaluates attributes against policies; it does not model the delegation chain through which those policies were authorized. NGAC composes policies but does not enforce monotonic tightening (a child policy can be more permissive than its parent). PACT envelopes are compositional, monotonically tightening, and cryptographically traceable through the delegation chain via EATP records. The contribution is not the access control mechanism per se; it is the organizational delegation architecture that gives access control decisions their governance meaning.

### 2.6 Enterprise GRC and Zero Trust

Deployed enterprise governance systems already enforce segregation of duties, approval workflows, and audit trails at scale. SAP GRC manages access risk analysis and remediation. Microsoft Entra provides identity governance with access reviews and entitlement management. These systems govern human access to enterprise applications. What they do not address is AI agent delegation: how authority composes through agent-to-agent delegation chains, how operating envelopes tighten monotonically through hierarchy, how knowledge clearance is independent of organizational rank, or how containment boundaries enforce information barriers architecturally.

PACT is not a replacement for enterprise IAM or GRC. It operates at a different layer: organizational delegation architecture for AI agents, not identity-based access control for human users. An organization deploying PACT would still use its IAM system for human authentication and its GRC system for SOD analysis. PACT governs what happens after the human defines the agent's authority.

NIST SP 800-207 (Rose, Borchert, Mitchell, & Connelly, 2020) defines Zero Trust Architecture: "never trust, always verify" with per-request access decisions. PACT's default-deny containment boundaries implement Zero Trust for organizational knowledge: no agent has implicit access to any knowledge outside its own D/T container, regardless of its role's seniority. Every cross-boundary access requires explicit authorization (bridge or cross-containment policy). This is Zero Trust applied to organizational structure, not just network perimeters.

### 2.7 Military and Government Classification

Military and intelligence organizations have separated clearance from rank for decades. PACT's Knowledge Clearance Framework uses the five classification levels defined in EATP's constraint envelope schema (PUBLIC through TOP SECRET) for enterprise and regulatory contexts where this principle applies but has never been architecturally encoded for AI agent governance.

### 2.8 Financial Services Regulation

The Securities and Futures Act (Singapore, 2001) and MAS Notice SFA 04-N21 (MAS, 2023) require capital markets intermediaries to maintain information barriers between functions that could give rise to conflicts of interest. SFA 04-N21 specifies segregation of work premises, restriction of access to confidential or price-sensitive information on a need-to-know basis, and separation of roles involving corporate finance advice from other activities. Industry practice adds physical separation, restricted communications, staff training, trading monitoring, and watch/restricted list management. PACT addresses the structural component (electronic access restriction through organizational containment boundaries) while leaving physical, procedural, and training requirements to complementary controls. I am explicit: PACT enforces one component of a multi-component regulatory requirement; it does not replace the full compliance architecture.

### 2.9 Relationship to CARE, EATP, and CO

PACT extends the Terrene Foundation's existing standards at a different architectural layer. CARE v2.1 (Hong, 2026a) provides the philosophical foundation for Human-on-the-Loop governance. EATP v2.2 (Hong, 2026b) provides cryptographic trust verification, including the five constraint dimensions (Financial, Operational, Temporal, Data Access, Communication) and the verification gradient with four outcome categories (auto-approved, flagged, held, blocked) that PACT uses without redefinition. CO v1.1 (Hong, 2026c) provides the knowledge methodology for structuring work within organizational structures; COC (Hong, 2026d) demonstrates the methodology in software development contexts.

I do not redefine EATP's constraint dimensions or verification gradient. PACT contributes the organizational architecture for how those dimensions are configured, delegated, and composed across hierarchical levels.

---

## 3. Research Methodology

This paper follows a design science research approach (Hevner, March, Park, & Ram, 2004; Peffers, Tuunanen, Rothenberger, & Chatterjee, 2007). Using the contribution typology of Gregor and Hevner (2013), the primary contribution is a **Level 1 design artifact**: the PACT specification as a situated implementation. The underlying design hypothesis is testable: organizations that adopt D/T/R grammar with monotonic envelope tightening will achieve shorter mean-time-to-accountability-resolution for AI agent actions than organizations using flat RBAC-only governance. Validating this hypothesis empirically would elevate the contribution to Level 2 (nascent design theory); I do not make that claim here.

The artifact was developed iteratively across four implementations: a production enterprise agent platform (605 Python modules), the PACT implementation (split into kailash-pact as the governance engine primitive and the PACT Platform as the human judgment surface; collectively 133+ Python modules, 4,191+ tests, open source under Apache 2.0), Arbor (HRIS platform, 227 Python modules, open source), and regulatory compliance architectures designed for financial services. Patterns that recurred across implementations were extracted and formalized. The kailash-pact primitive includes the core governance module (addressing, envelopes, clearance, access control, compilation) with three-level monotonic tightening. The PACT Platform provides the human-facing dashboard, approval queues, and audit interface. Both are validated against a dog-food deployment of the Terrene Foundation's own organizational structure.

**Evaluation**: I evaluate the artifact through structural analysis and scenario-based illustration (Hevner et al.'s descriptive evaluation method). I analyze whether the D/T/R grammar, envelope composition, and clearance framework can model organizational structures across domains (Sections 7-8). I acknowledge that descriptive evaluation is the weakest form in Hevner et al.'s (2004) hierarchy. Analytical evaluation (formal proof of monotonic tightening properties), expert evaluation (organizational design practitioners assessing the grammar), and empirical evaluation (deployment measurement) are future work. The falsification conditions (Section 14) define what would constitute negative evaluation outcomes.

The knowledge contribution is at Gregor and Hevner's (2013) Level 1: a situated implementation supported by informed argument and single-author testing. Promotion to Level 2 (nascent design theory) requires empirical validation by independent adopters.

---

## 4. The Accountability Grammar

### 4.1 Three Node Types

I model organizations using three node types:

**D (Department)**: A persistent knowledge container. The Finance Department exists independently of who leads it. Organizational memory accumulates here.

**T (Team)**: A fluid knowledge container. A project team, task force, or working group. More fluid than D; often purpose-built and temporary.

**R (Role)**: A person position. The accountability anchor. The position persists even when vacant; the occupant changes.

### 4.2 The Core Constraint

A containment node (D or T) MUST be immediately followed by exactly one R before any further structure can attach.

Valid: `D-R`, `D-R-R`, `D-R-D-R`, `D-R-T-R`
Invalid: `D-D`, `D-T`, `T-T` (no accountable person between containers)

This constraint encodes a governance principle from Fama and Jensen (1983): decision management requires a named decision controller. In Lawrence and Lorsch's (1967) terms, every act of differentiation (creating a new D or T) requires an immediate act of integration (assigning accountability to a person). Containers scope decisions; they do not make them.

In BNF:

```
organization ::= BOD ( unit )*
unit         ::= container head body
container    ::= "D" | "T"
head         ::= "R"                    /* mandatory */
body         ::= ( R | unit )*
```

BOD denotes the Board of Directors or equivalent apex governance body. When a D or T is created without an R, the system auto-creates a vacant head role. Vacant roles satisfy the constraint but cannot execute.

### 4.3 Positional Addressing

Every node receives a globally unique address encoding containment and accountability:

```
D1-R1                          CEO
D1-R1-D1-R1                    CFO
D1-R1-D1-R1-D1-R1              Head of Treasury
D1-R1-D1-R1-D1-R1-T1-R1       Cash Manager
D1-R1-D1-R1-D1-R1-T1-R1-R2    Treasury Analyst
```

Addresses are globally unique, deterministically computed, and support prefix-containment queries. Reading left to right traces the accountability chain from root to leaf.

### 4.4 Cross-Containment Bridges

The D/T/R grammar enforces containment boundaries; bridges provide controlled crossings. A bridge is a standing or ad-hoc coordination channel between two roles in different D or T containers. Bridges address Galbraith's (1973) lateral relations strategy and Thompson's (1967) boundary-spanning activities.

A bridge has five properties: (1) it connects two named roles (not containers; accountability must be traceable to persons on both sides); (2) it specifies a scope (what data, what operations, what classification level may cross the boundary); (3) it requires bilateral establishment (both roles must agree); (4) it requires approval from the lowest common ancestor in the D/T/R tree, or from a designated compliance role, to prevent collusion that circumvents information barriers; (5) it creates EATP records making the cross-boundary relationship auditable.

EATP's Delegation Record is unilateral (A delegates to B). Bridges are bilateral. I map this as two cross-referencing Delegation Records (A grants B scoped access; B grants A scoped access), each referencing the other's record ID. This creates an atomicity concern: what if A's record is created but B's is not? The implementation pattern is transactional: both records are created atomically or neither is. If the EATP store does not support transactions across records, a BilateralDelegation pattern (a wrapper that creates both records and rolls back on partial failure) is required. This is an implementation constraint, not a specification change to EATP; the underlying Delegation Records remain standard EATP elements.

Bridges do not override containment boundaries; they create scoped exceptions. A compliance-to-advisory bridge permits the CCO to read advisory RESTRICTED data for compliance review; it does not grant blanket access to all advisory knowledge. The bridge's scope is itself subject to monotonic tightening: a bridge cannot grant access broader than either party's own envelope permits.

---

## 5. Recursive Envelope Delegation

### 5.1 The Tractability Problem

CARE says "humans define the operating envelope." Which humans, for which agents? Galbraith (1973) would recognize this as an information-processing problem: the governance information required to configure envelopes for over 100 supervisory positions (the exact number depends on hierarchy depth and shape; in a four-level tree with span of five, levels 0-3 contain roughly 156 non-leaf positions) exceeds any central team's processing capacity.

The solution is recursive delegation: each supervisor defines envelopes for direct reports only. This aligns envelope-setting authority with organizational authority and distributes governance burden to the people closest to each context. It implements Galbraith's hierarchical strategy: each level processes the governance information relevant to its scope.

### 5.2 Three-Layer Architecture

I decompose the operating envelope into three layers:

**Role Envelope (standing)**: A supervisor defines the standing boundary for a direct report. Defined once; applies to all tasks.

**Task Envelope (ephemeral)**: For a specific task, the supervisor may optionally narrow the Role Envelope. Expires when the task completes.

**Effective Envelope (computed)**: The intersection of all ancestor envelopes from organizational root to current position. Never stored; always computed. This is the binding boundary.

Each layer uses EATP's five constraint dimensions without modification.

### 5.3 Monotonic Tightening

No envelope at any level can be wider than any ancestor envelope. Authority can only tighten through delegation.

Formally: for any child envelope E_child under parent envelope E_parent, for every dimension d: E_child.d is at most E_parent.d.

Enforced at write time. A wider envelope is rejected with the violating dimension identified. This implements the principle that delegated authority cannot exceed the delegator's authority (Fama & Jensen, 1983; Hart & Moore, 1990).

The intersection operation is defined per dimension, following XACML's (OASIS, 2013) principle that policy combining algorithms must be formally specified:

| Dimension     | Intersection                                                        | Example                                                           |
| ------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Financial     | min() of numeric limits                                             | min($500K, $100K) = $100K                                         |
| Operational   | set intersection of allowed actions; set union of blocked actions   | allowed: {A,B,C} and {A,B} = {A,B}                                |
| Temporal      | overlap of operating windows; union of blackout periods             | Mon-Fri 07:00-20:00 and Mon-Fri 09:00-18:00 = Mon-Fri 09:00-18:00 |
| Data Access   | min() of classification ceiling; set intersection of allowed scopes | min(CONFIDENTIAL, RESTRICTED) = RESTRICTED                        |
| Communication | set intersection of allowed recipients and channels                 | {internal, banking} and {internal} = {internal}                   |

Each operation guarantees that the result is at most as permissive as either input. This is a deny-overrides combining algorithm in XACML terms: wherever two envelopes disagree, the more restrictive value applies. Absent dimensions are treated as maximally permissive (the parent imposes no constraint on that dimension). When composed allowed and blocked sets overlap for Operational actions, the blocked set takes precedence (deny-overrides).

### 5.4 Gradient Composition

Each supervisor configures gradient thresholds for their direct reports only. The gradient does not compose across levels. The Effective Envelope (Section 5.2) already reflects all ancestor constraints; the immediate supervisor's gradient determines how close to the Effective Envelope boundary triggers each zone.

If the CEO allows $500K and the CFO allows $100K for the Head of Treasury, the Effective Envelope financial limit is $100K. The CFO's gradient determines whether $80K is auto-approved or flagged for the Head of Treasury. The CEO's gradient is irrelevant because the CEO's $500K limit is not the binding constraint at that level.

A risk follows from this design: a supervisor who sets auto-approve thresholds near the Effective Envelope boundary effectively delegates full authority without oversight. This is gradient dereliction, a variant of envelope dereliction (Section 12.9). Detection requires monitoring the ratio of auto-approved to held actions per supervisor; prevention requires gradient policies set by the supervisor's own supervisor, creating a recursive oversight structure that mirrors the envelope delegation itself.

### 5.5 Vacancy Handling

When a role becomes vacant (the occupant leaves and no replacement is assigned), the D/T/R grammar remains valid (the vacant R node satisfies the structural constraint) but governance is temporarily degraded. Three rules apply:

1. The parent role must designate an acting occupant within a configurable deadline (default: 24 hours).
2. Until an acting role is designated, the vacant role's direct reports operate under the more restrictive of their own Role Envelope or the parent's envelope for the vacant role.
3. If no acting role is designated within the deadline, all downstream agents are suspended (all actions held) with escalation to the next ancestor with an occupant.

Rule 3 is deliberately conservative. An organization that cannot fill a vacancy in 24 hours has a governance gap that should be surfaced, not papered over.

### 5.6 Per-Dimension Gradient Configuration

I extend EATP's verification gradient with per-dimension, per-role configuration. The supervisor sets gradient thresholds within each Role Envelope:

```
Head of Treasury's envelope for Cash Manager:
  Financial: auto-approved up to $20,000
             flagged $20,001 to $50,000
             held above $50,001
             blocked above $100,000
```

This operationalizes the levels-of-automation tradition (Sheridan & Verplank, 1978; Parasuraman et al., 2000) at the organizational level: each supervisor calibrates the automation level for each constraint dimension of each direct report's agent.

### 5.7 EATP Record Mapping

Every PACT governance action creates a corresponding EATP record. This mapping is normative; implementations claiming PACT conformance must produce these records.

| PACT Action                                  | EATP Record Type                                                  |
| -------------------------------------------- | ----------------------------------------------------------------- |
| Organization created (BOD established)       | Genesis Record                                                    |
| Role Envelope defined or modified            | Delegation Record + Constraint Envelope                           |
| Task Envelope created                        | Delegation Record + Constraint Envelope (with expiry)             |
| Clearance granted                            | Capability Attestation                                            |
| Bridge established                           | Two cross-referencing Delegation Records (bilateral)              |
| Action verified (any gradient zone)          | Audit Anchor (captures effective envelope at verification time)   |
| Information barrier enforced (access denied) | Audit Anchor (subtype: barrier_enforced)                          |
| Emergency bypass activated                   | Audit Anchor (subtype: emergency_bypass)                          |
| Envelope modified                            | Audit Anchor (subtype: envelope_modified) + new Delegation Record |

The Audit Anchor created at verification time captures the effective envelope as computed at that moment. This enables point-in-time audit queries without storing effective envelopes permanently: the Audit Anchor records what the effective envelope WAS, not what it IS now.

PACT requires EATP Conformant level at minimum (all five elements, all four operations, full verification gradient, cascade revocation, and reasoning trace support). EATP Complete is recommended for production deployments (all five trust postures, all five confidentiality levels, both StrictEnforcer and ShadowEnforcer, VerificationBundle export, and reasoning traces for governance decisions). See the EATP thesis (Hong, 2026b) for full conformance definitions.

---

## 6. Knowledge Clearance

### 6.1 The Seniority Fallacy

Traditional access control ties information access to organizational rank. This conflates authority (position in the decision chain) with clearance (need to know). A Legal Secretary processing M&A documents needs high clearance for that compartment despite low authority. A Sales VP may need no clearance above baseline despite high authority.

March and Simon (1958) recognized that organizational structure shapes information flows; Simon (1947) recognized that bounded rationality limits what any individual can process. I extend both insights to AI agents: when agents access knowledge bases on behalf of roles, encoding the seniority fallacy means agents access everything their role's rank permits, regardless of operational need.

### 6.2 Five Classification Levels

I adopt five classification levels consistent with EATP's confidentiality classification for reasoning traces (Hong, 2026b), applied here to organizational knowledge governance:

| Level | Name         | Enterprise Meaning                        | Pre-Clearance                       |
| ----- | ------------ | ----------------------------------------- | ----------------------------------- |
| C0    | PUBLIC       | Routine operations, published information | None                                |
| C1    | RESTRICTED   | Commercial data, personnel records        | Cross-containment policy sufficient |
| C2    | CONFIDENTIAL | Strategic plans, board materials          | Role-level clearance                |
| C3    | SECRET       | Legal privilege, regulatory investigation | Individual clearance + NDA          |
| C4    | TOP SECRET   | Existential risk, crisis plans            | Board clearance + vetting           |

Clearance is granted independently of rank. Compartments provide need-to-know isolation at SECRET and TOP SECRET.

### 6.3 Posture-Gated Effective Clearance

The five trust postures defined in EATP (Hong, 2026b) gate the maximum effective clearance an agent can exercise:

Effective clearance = min(role.max_clearance, posture_ceiling[agent.posture])

A high-clearance role with a low-trust agent accesses only what the posture permits. Trust in the agent must be earned before it can exercise the role's clearance.

---

## 7. Worked Example: Financial Services Regulatory

### 7.1 Structure

Consider a financial institution subject to MAS regulation:

```
BOD (Board of Directors)
D1 (Executive Office)
  D1-R1 (CEO)
    D1-R1-D1 (Compliance Division)
      D1-R1-D1-R1 (Chief Compliance Officer)
        D1-R1-D1-R1-T1 (AML/CFT Team)
          D1-R1-D1-R1-T1-R1 (AML Officer)
    D1-R1-D2 (Advisory Division)
      D1-R1-D2-R1 (Head of Advisory)
        D1-R1-D2-R1-T1 (Client Advisory Team)
          D1-R1-D2-R1-T1-R1 (Senior Advisor)
    D1-R1-D3 (Trading Division)
      D1-R1-D3-R1 (Head of Trading)
        D1-R1-D3-R1-T1 (Equities Desk)
          D1-R1-D3-R1-T1-R1 (Senior Trader)
```

### 7.2 Information Barriers

MAS regulations require information barriers between Advisory and Trading functions. PACT addresses the structural dimension: Advisory (D1-R1-D2) and Trading (D1-R1-D3) are separate D containers with no cross-containment knowledge sharing policy between them. An Advisory Analyst's agent cannot access Trading's market positions because the containment boundary blocks it architecturally.

The CCO (D1-R1-D1-R1) holds standing bridges to both divisions for compliance monitoring, scoped to compliance review only.

I am explicit about scope: PACT addresses structural electronic access restriction, one component of a multi-component information barrier program. Physical separation, staff training, personal account dealing monitoring, wall-crossing procedures, and watch/restricted list management are complementary controls that PACT does not replace.

### 7.3 Clearance Independence in Practice

The AML Officer (mid-level authority) holds SECRET clearance for compartment `aml-investigations` because the function requires access to Suspicious Activity Reports. The Head of Trading (senior authority) does not hold this clearance. Rank does not determine access; operational need does.

### 7.4 Verification Gradient

```
CCO's envelope for AML Officer:
  Financial: no financial authority
  Operational: STR preparation autonomous;
               STR filing requires CCO approval;
               regulatory notification to MAS requires CCO
  Data Access: SECRET (aml-investigations compartment)
  Communication: external to MAS held for CCO awareness

CEO's envelope for Head of Trading:
  Financial: trading within regulatory position limits
  Operational: execution within approved instruments
  Data Access: CONFIDENTIAL (no investigation access)
  Communication: regulatory bodies blocked (all via compliance)
```

---

## 8. Worked Example: CFO Office Task Cascade

A Q3 board presentation task cascades from CEO through CFO to Treasury and Financial Planning & Analysis (FP&A) agents. In a prototype demonstration using an enterprise agent platform (not a production deployment), three human touch points occurred over six days of autonomous execution. The CEO approved the decomposition plan. The Head of Treasury made a boundary judgment about counterparty data inclusion; the gradient held this action because the data scope exceeded the task envelope. The CEO reviewed the final output. Fourteen EATP records formed the audit trail.

Of 47 actions executed, 46 were auto-approved within envelopes and 1 was held at the data access boundary. The three human touch points (plan approval, data scope judgment, output review) engaged human judgment at the moments where it was irreplaceable. This is what Human-on-the-Loop looks like operationally: not absence, but targeted engagement at envelope boundaries where bounded rationality (Simon, 1947) makes human judgment the binding constraint.

---

## 9. Emergency Bypass

Legitimate emergencies require temporary envelope expansion. I provide tiered bypass with hard constraints:

| Tier | Duration      | Approval              | Scope                           |
| ---- | ------------- | --------------------- | ------------------------------- |
| 1    | Up to 4 hours | Immediate supervisor  | Up to supervisor's own envelope |
| 2    | 4-24 hours    | Two levels up         | Up to that envelope             |
| 3    | 24-72 hours   | C-Suite or equivalent | Up to C-Suite envelope          |
| 4    | Over 72 hours | Not emergency         | Not permitted via bypass        |

Bypass cannot widen beyond the approver's own envelope. Auto-expiry is hard-enforced. Post-incident review is mandatory within 7 days. Rate limiting prevents bypass from becoming a governance workaround.

---

## 10. The Architectural Inversion

Traditional software engineering builds applications first and bolts governance on afterward: design domain modules, build each module, add permissions (RBAC), add approval workflows, add audit logging, add compliance checks, add information barriers. The governance model is separate from the application architecture. Every new feature is a new surface where someone might forget the permission check, the audit log, the compliance gate.

PACT inverts this. The organizational structure IS the application architecture.

When you define Advisory (D1-R1-D2) and Trading (D1-R1-D3) as separate D containers with no cross-containment policy between them, you have simultaneously defined the module boundary, the data access model, the API contract (data crosses only through a bridge with scoped permissions), the audit trail (any attempt to cross is logged automatically), and the compliance evidence (the information barrier is enforced by construction, not by policy).

| Traditional Pattern                       | PACT-Native Equivalent                                |
| ----------------------------------------- | ----------------------------------------------------- |
| Microservice boundaries                   | D/T containment boundaries                            |
| Inter-service APIs                        | Bridges (scoped, audited, bilateral)                  |
| RBAC (role to permission to resource)     | Containment + clearance + envelope (structural)       |
| Approval workflows (coded step-by-step)   | Verification gradient (auto-surfaces held actions)    |
| Rate limiting middleware                  | Operational dimension of the operating envelope       |
| Budget controls                           | Financial dimension of the operating envelope         |
| Audit logging (sprinkled throughout code) | EATP records by construction                          |
| Data classification labels                | Knowledge clearance framework (enforced, not labeled) |
| Information barriers (policy, hoped-for)  | Containment boundaries (architectural, enforced)      |

Developers build three things: domain logic (what agents actually do; pure computation, no permission checks), agent capabilities (tools scoped to each role's function), and governance configuration (the D/T/R structure, envelopes, clearances, bridges). They do not build permission systems, approval workflow engines, audit logging infrastructure, data access control layers, rate limiting middleware, or budget tracking systems. Those are all handled by the organizational architecture.

This inversion has a cost: the governance structure must be defined before the application can function. Traditional engineering can defer governance; PACT-native engineering cannot. For organizations that prioritize accountability, this is the right trade-off. For organizations that prioritize speed of iteration, it may not be.

---

## 11. Universality

The patterns in PACT appear across domains with formal governance:

**Military**: Divisions (D) commanded by generals (R); Rules of Engagement are envelopes; security classifications are clearance; the engagement authorization chain is the gradient. **Government**: Ministries (D) led by ministers (R); Singapore's IM classification maps directly. **Healthcare**: Departments (D) led by chairs (R); treatment protocols are envelopes; patient data tiers are clearance. **Financial services**: Compliance, advisory, and trading divisions with information barriers enforced by containment boundaries.

PACT maps most naturally to Mintzberg's (1979) Machine Bureaucracy and Divisionalized Form. It does not model Adhocracy well; Burns and Stalker (1961) would place PACT on the mechanistic side. Informal organizations, egalitarian collectives, and single-person operations may not benefit. The specification is most valuable when organizational complexity justifies governance overhead.

I am careful about the epistemological status of this claim. The patterns were observed in existing governance structures and formalized as a design artifact. The formalization is prescriptive (it constrains organizational modeling choices). The observation that similar patterns recur across domains is descriptive. I do not claim to have discovered universal laws of organization; I claim to have formalized recurring patterns into a specification that makes them computationally enforceable for AI agent governance.

---

## 12. Honest Limitations

### 12.1 Constraint Theater

Organizations can configure PACT to maximize autonomy and minimize human engagement, creating governance without substance. If envelope boundaries are so broad that nothing is ever held, humans are absent. A poorly configured system is worse than no system: it creates false confidence. Initial deployments should target at least 10% of agent actions generating held events, as a calibration check.

### 12.2 Hierarchical Assumption

The grammar assumes hierarchy. Burns and Stalker (1961) would classify PACT as mechanistic. Organizations using Holacracy or sociocracy must map accountability anchors to R nodes (lead links to R; circles to T). This mapping is possible but may distort the governance model. PACT does not claim to be right for organizations that reject accountability hierarchy, nor for Mintzberg's Adhocracy configuration.

### 12.3 Deep Hierarchy Degeneration

In a 10-level hierarchy, monotonic tightening may shrink the effective envelope to near-zero. I specify degenerate envelope detection but cannot prevent excessively deep hierarchies. Practical guidance: if the effective envelope at any level drops below 20% of the role's functional minimum on any dimension, the Organization Builder should flag it.

### 12.4 Envelope Configuration Burden

In a 500-person organization with an average span of control of five, approximately 125 supervisory positions each require five-dimensional envelope configuration (the exact number depends on hierarchy depth and shape; in a four-level tree with span of five, levels 0-3 contain roughly 156 non-leaf positions). Defaults, templates, and incremental deployment help, but the burden is real and has not been empirically measured. A prototype configuration study would strengthen this specification.

### 12.5 Single-Author Provenance

All implementations were built by one person. The universality claim is structural analysis, not empirical deployment. Until independent implementations validate PACT in military, healthcare, and government contexts, universality remains a design hypothesis.

### 12.6 No Formal Verification

The monotonic tightening invariant, access algorithm, and addressing computation are argued informally and tested in implementations. Formal verification would strengthen the specification.

### 12.7 Regulatory Scope

The MAS information barrier mapping addresses structural electronic access restriction only, one component of a multi-component regulatory program. Physical separation, training, personal trading monitoring, wall-crossing procedures, and watch list management are outside PACT's scope.

### 12.8 Surveillance and Dual-Use

PACT proposes audit trails covering every action, delegation, and knowledge access event. The same architecture that enables accountability enables surveillance. An employer deploying PACT could monitor every action of every employee's AI agent, creating a granular surveillance apparatus under the banner of governance.

This dual-use risk is inherent in any accountability architecture; it is not unique to PACT. Mitigations include: access controls on the audit data itself (who can query the PACT graph is itself a clearance question), purpose limitation policies, data minimization in audit records (logging the boundary decision, not the full action content), and employee data protection regulations (PDPA in Singapore, GDPR in the EU). PACT's clearance framework can be applied reflexively: the audit data is itself classified, and access to it requires clearance. In jurisdictions with strong labor protections (EU under GDPR, Singapore under PDPA), data protection regulations constrain employer use of PACT audit data. In jurisdictions without such protections (notably the US, which lacks federal employee privacy law), the same architecture enables granular employee monitoring without legal constraint. I acknowledge that architectural mitigations do not prevent organizational misuse; they only constrain it.

### 12.9 Adversarial Threats Not Analyzed

Tomasev et al. (2026) identify 16 attack vectors for AI delegation systems. I have not conducted equivalent adversarial analysis for PACT. I acknowledge five threats that target PACT's configuration layer, where the specification is most vulnerable. Tomasev et al.'s authentication, cryptographic, and protocol-level vectors are addressed by EATP (Hong, 2026b) rather than PACT.

(1) **Envelope dereliction**: A supervisor sets envelopes as broad as their own authority permits, eliminating governance substance while satisfying the monotonic tightening invariant. PACT detects this only through governance dashboards that surface "pass-through" envelopes; it does not prevent it architecturally.

(2) **Compromised agent within envelope**: A prompt-injected or jailbroken agent operating within its envelope is invisible to PACT. PACT governs boundaries, not behavior. Runtime behavioral monitoring is a complementary requirement that PACT does not provide.

(3) **Bridge collusion**: Two role holders establish a bridge that creates a combined capability neither was intended to have, bypassing information barriers. Bridge creation should require approval from a common ancestor or designated compliance role; the current specification requires only bilateral agreement.

(4) **Posture gaming**: The supervisor who benefits from higher agent autonomy also controls posture advancement, creating a conflict of interest. Posture advancement should involve an independent assessor.

(5) **TOCTOU in envelope computation**: The organizational structure may change between envelope computation and action execution. PACT mitigates this through post-execution audit comparison but does not prevent the window.

A complete threat model is future work. I note that PACT's structural invariants (the grammar constraint, monotonic tightening, positional addressing) are resistant to adversarial pressure because they are enforced at write time, not at runtime. The threats above target the configuration layer, not the structural layer.

### 12.10 Evaluation Weakness

The evaluation in this paper is descriptive (scenario-based illustration). I have not conducted analytical evaluation (formal proof), expert evaluation (practitioner assessment), or empirical evaluation (deployment measurement). This is the weakest acceptable form of design science evaluation (Hevner et al., 2004). Stronger evaluation is future work.

---

## 13. Broader Impact

PACT's accountability architecture has implications beyond its intended use in enterprise AI governance.

**Positive**: Organizations deploying autonomous AI agents gain structurally enforceable accountability chains, graduated human oversight, and need-to-know information governance. This addresses the implementation gap that Hagendorff (2020) and Jobin et al. (2019) identified. For regulators, PACT's envelope and gradient mechanisms operationalize the human oversight requirements of the EU AI Act Article 14 and provide auditable evidence of compliance.

**Negative**: The same mechanisms enable granular workplace surveillance (Section 12.8). PACT trades organizational flexibility for accountability; the cost is that it encodes hierarchy as a prerequisite for governance. Organizations that adopt PACT cannot easily evolve toward flatter governance models without rebuilding their D/T/R structures. Holacracy (Robertson, 2015) and sociocracy explicitly reject the named-person accountability model that PACT requires; these governance forms cannot adopt PACT without distorting their core principles.

The clearance framework creates new forms of information inequality. Those with high clearance hold structural advantages over those without, regardless of organizational position. In contexts where information asymmetry already creates power imbalances (employer-employee, regulator-regulated), PACT's classification system amplifies the asymmetry by making it architecturally enforced rather than merely procedural.

**Equity considerations**: PACT assumes that hierarchical accountability is beneficial. In cultures with high power distance (Hofstede, 1980), the grammar may reinforce existing authority patterns without question. In cultures with low power distance, it may feel imposed rather than enabling. The specification should not be adopted as a universal best practice; it is a governance architecture for organizations that have already chosen hierarchical accountability as their governance model.

---

## 14. Falsification Conditions

1. **Grammar inadequacy**: A worked counterexample showing an organizational form (enterprise, government, military, healthcare) that the D/T/R grammar cannot model while preserving governance-relevant relationships (every accountability question answerable by traversing the PACT graph) would falsify the universality claim.

2. **Degenerate envelopes**: If organizations with 6-8 levels of hierarchy consistently produce effective envelopes where more than 50% of roles have at least one dimension below 20% of functional minimum, the composition model is impractical for standard organizational depth.

3. **Clearance rejection**: If adopters consistently override clearance-seniority independence (reinstating rank-based access within 12 months of deployment), that design hypothesis is wrong.

4. **Configuration cost**: If configuration cost consistently outweighs governance value for organizations of 50-5000 people, the architecture is too expensive. This condition cannot currently be operationalized without deployed systems and comparison baselines; I state it as a future evaluation criterion.

5. **Regulatory insufficiency**: If regulators (MAS, FINRA, FCA) reject containment-based information barriers as insufficient even as one component of a multi-component compliance program, the financial services application fails.

---

## 15. Relationship to the Constrained Organization

The Constrained Organization (Hong, 2026e) integrates CARE, EATP, and CO with five properties. PACT provides the architectural specification for how those properties compose at organizational scale. Rather than adding a sixth independent property, I frame PACT as the architectural detail that answers the scale question Properties 1 (architectural separation), 2 (verifiable trust lineage), and 4 (graduated autonomy) presuppose: how do these properties remain tractable when hundreds of agents operate across multi-level hierarchies?

The D/T/R grammar is the structural expression of the Trust Plane (Property 1). Recursive envelope delegation is how graduated autonomy (Property 4) composes through hierarchy. Knowledge clearance is how structured institutional knowledge (Property 3) is governed for access. Property 5 (Compounding knowledge) is addressed by CO's Layer 5 learning pipeline (Hong, 2026c), not by PACT; organizational architecture provides the structural boundaries within which knowledge compounds, but the compounding mechanism itself is CO's contribution. PACT does not add a new property; it makes Properties 1-4 implementable at scale.

---

## 16. Standard Status and Promotion Record

PACT was published in March 2026 as a Working Architecture (v0.1-WA) under a deliberate defer: the Foundation had just been incorporated, and standardizing from a single implementation before external validation is a known anti-pattern. On 2026-06-21 the Foundation promoted PACT to a ratified standard (v1.0), peer to CARE, EATP, and CO. The Foundation's ratified standards are now four: CARE (philosophy), EATP (protocol), CO (methodology), and PACT (organizational architecture). "The Trinity" is retained as the historical name for the original three.

The promotion criteria defined at publication, and their disposition at promotion:

1. **Multi-implementation validation** (at least two implementations, one open-source, one commercial): _met_ — an open-source reference implementation (kailash-py / kailash-pact) and a separate production commercial deployment.
2. **Adopter feedback** (structured feedback from operating deployments): _substantially met / in progress_ — the production deployment supplies sustained operational validation; broader multi-organization feedback continues to accumulate. Not treated as blocking.
3. **Foundation standards published** (CARE, EATP, CO published): _met_ for publication; external academic peer review of the Trinity remains in progress and is not treated as blocking.
4. **Specification boundary map** (PACT, CARE, EATP, CO boundaries): _met_ — the boundary is specified in Section 15 and across the published suite.

The promotion is a Foundation-authority determination that the accumulated evidence — a production commercial deployment, the open reference implementations, and multiple adversarial validation rounds — is sufficient. It does not assert that every criterion was independently and exhaustively cleared; criteria 2 and 3 remain in active progress and are not blocking. This section supersedes ADR-003 Decision 1; see terrene journal 0034 for the full decision record.

---

## References

Bainbridge, L. (1983). Ironies of automation. _Automatica_, 19(6), 775-779.

Burns, T., & Stalker, G. M. (1961). _The Management of Innovation_. Tavistock Publications.

Cherns, A. (1976). The principles of sociotechnical design. _Human Relations_, 29(8), 783-792.

Endsley, M. R., & Kiris, E. O. (1995). The out-of-the-loop performance problem and level of control in automation. _Human Factors_, 37(2), 381-394.

European Parliament. (2024). Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act). _Official Journal of the European Union_.

Fama, E. F., & Jensen, M. C. (1983). Separation of ownership and control. _Journal of Law and Economics_, 26(2), 301-325.

Floridi, L., & Cowls, J. (2019). A unified framework of five principles for AI in society. _Harvard Data Science Review_, 1(1).

Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Chazerand, P., Dignum, V., ... & Vayena, E. (2018). AI4People: An ethical framework for a good AI society. _Minds and Machines_, 28, 689-707.

Galbraith, J. R. (1973). _Designing Complex Organizations_. Addison-Wesley.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. _MIS Quarterly_, 37(2), 337-355.

Hagendorff, T. (2020). The ethics of AI ethics: An evaluation of guidelines. _Minds and Machines_, 30, 99-120.

Hart, O. (1995). _Firms, Contracts, and Financial Structure_. Oxford University Press.

Hart, O., & Moore, J. (1990). Property rights and the nature of the firm. _Journal of Political Economy_, 98(6), 1119-1158.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. _MIS Quarterly_, 28(1), 75-105.

Hofstede, G. (1980). _Culture's Consequences: International Differences in Work-Related Values_. Sage Publications.

Hong, J. (2026). Constraint Theater: Governance Without Wealth Effects. Submitted to _American Economic Review_. Theoretical foundation; PACT implements the recursive application of the formal model across organizational hierarchies.

Hong, J. (2026a). CARE: A Core Thesis. _Terrene Foundation_. https://github.com/terrene-foundation/publications/blob/main/CARE-Core-Thesis.pdf

Hong, J. (2026b). EATP: A Core Thesis. _Terrene Foundation_. https://github.com/terrene-foundation/publications/blob/main/EATP-Core-Thesis.pdf

Hong, J. (2026c). CO: A Core Thesis. _Terrene Foundation_. https://github.com/terrene-foundation/publications/blob/main/CO-Core-Thesis.pdf

Hong, J. (2026d). COC: A Core Thesis. _Terrene Foundation_. https://github.com/terrene-foundation/publications/blob/main/COC-Core-Thesis.pdf

Hong, J. (2026e). The Constrained Organization. _Terrene Foundation_. https://github.com/terrene-foundation/publications/blob/main/Constrained-Organization-Thesis.pdf

Hu, V. C., Ferraiolo, D., Kuhn, R., Schnitzer, A., Sandlin, K., Miller, R., & Scarfone, K. (2014). _Guide to Attribute Based Access Control (ABAC) Definition and Considerations_ (NIST SP 800-162). National Institute of Standards and Technology.

Humberd, B. K., & Latham, S. F. (2026). When AI becomes an agent of the firm: Examining the evolution of AI in organizations through an agency theory lens. _Journal of Management Studies_, 63(2), 668-694. DOI: 10.1111/joms.13274

IMDA. (2026). _Model AI Governance Framework for Agentic AI_. Infocomm Media Development Authority, Government of Singapore.

Jarrahi, M. H., & Ritala, P. (2025). Rethinking AI agents: A principal-agent perspective. _California Management Review_, 67(4).

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. _Nature Machine Intelligence_, 1(9), 389-399.

Kolbjornsrud, V. (2024). Designing the intelligent organization: Six principles for human-AI collaboration. _California Management Review_, 66(2), 44-64. DOI: 10.1177/00081256231211020

Kolt, N. (2025). Governing AI agents. _Notre Dame Law Review_, 101 (forthcoming). arXiv:2501.07913.

Lawrence, P. R., & Lorsch, J. W. (1967). Differentiation and integration in complex organizations. _Administrative Science Quarterly_, 12(1), 1-47.

March, J. G., & Simon, H. A. (1958). _Organizations_. Wiley.

MAS. (2023). _Notice on Business Conduct Requirements for Corporate Finance Advisers_ [SFA 04-N21]. Monetary Authority of Singapore.

Mintzberg, H. (1979). _The Structuring of Organizations_. Prentice-Hall.

INCITS. (2020). _Next Generation Access Control (NGAC)_ (INCITS 565-2020). InterNational Committee for Information Technology Standards.

NIST. (2023). _Artificial Intelligence Risk Management Framework (AI RMF 1.0)_. National Institute of Standards and Technology.

OASIS. (2013). _eXtensible Access Control Markup Language (XACML) Version 3.0_. OASIS Standard.

OMG. (2014). _Business Process Model and Notation (BPMN) Version 2.0.2_. Object Management Group.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. _IEEE Transactions on Systems, Man, and Cybernetics_, 30(3), 286-297.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. _Journal of Management Information Systems_, 24(3), 45-77.

Perrow, C. (1967). A framework for the comparative analysis of organizations. _American Sociological Review_, 32(2), 194-208.

Robertson, B. J. (2015). _Holacracy: The New Management System for a Rapidly Changing World_. Henry Holt and Company.

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). _Zero Trust Architecture_ (NIST SP 800-207). National Institute of Standards and Technology.

Sandhu, R. S., Coyne, E. J., Feinstein, H. L., & Youman, C. E. (1996). Role-based access control models. _IEEE Computer_, 29(2), 38-47.

Sheridan, T. B., & Verplank, W. L. (1978). _Human and computer control of undersea teleoperators_. MIT Man-Machine Systems Laboratory.

Shneiderman, B. (2022). _Human-Centered AI_. Oxford University Press.

Simon, H. A. (1947). _Administrative Behavior_. Macmillan.

Singapore. (2001). _Securities and Futures Act_ (Cap. 289). Government of Singapore.

South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Greenwood, D., Chan, A., & Pentland, A. (2025). Authenticated delegation and authorized AI agents (AD/MIT). In _Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)_. arXiv:2501.09674.

The Open Group. (2019). _ArchiMate 3.1 Specification_. The Open Group.

Thompson, J. D. (1967). _Organizations in Action_. McGraw-Hill.

Tomasev, N., Franklin, M., & Osindero, S. (2026). Intelligent AI delegation. arXiv:2602.11865.

Trist, E. L., & Bamforth, K. W. (1951). Some social and psychological consequences of the longwall method of coal-getting. _Human Relations_, 4(1), 3-38.

Vantrappen, H. (2025). Designing a fluid organization of humans and AI agents. _California Management Review_.

Weber, M. (1947). _The Theory of Social and Economic Organization_ (A. M. Henderson & T. Parsons, Trans.). Oxford University Press. (Original work published 1922)

Williamson, O. E. (1985). _The Economic Institutions of Capitalism_. Free Press.

---

## Version History

| Version | Date       | Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1     | 2026-03-21 | Initial working draft.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0.2     | 2026-03-21 | Added methodology, contribution statement, organizational theory grounding, comparison table, first person, removed uncited references, scaled MAS claims.                                                                                                                                                                                                                                                                                                              |
| 0.3     | 2026-03-21 | Added AI governance literature, levels-of-automation literature, additional org theory (March & Simon, Lawrence & Lorsch, Burns & Stalker, Perrow), Gregor & Hevner contribution typology, Broader Impact section, surveillance/dual-use limitation. Fixed cross-references, attribution, terminology.                                                                                                                                                                  |
| 0.4     | 2026-03-21 | Restructured Section 2.1 into argument threads. Deepened Hagendorff engagement. Downgraded design theory to testable hypothesis. Sharpened Broader Impact. Added surveillance jurisdictional asymmetry. Fixed MAS reference. Added COC citation, AI assistance disclosure.                                                                                                                                                                                              |
| 0.5     | 2026-03-21 | Added bridge specification (Section 4.4). Fixed Robertson, MAS, references ordering, BOD, spec-level terminology.                                                                                                                                                                                                                                                                                                                                                       |
| 0.6     | 2026-03-21 | Aligned labels with EATP (PUBLIC/RESTRICTED). Added ABAC, NGAC, sociotechnical tradition, fixed Gregor & Hevner levels, Endsley, MAS citation, supervisor math. 43 refs.                                                                                                                                                                                                                                                                                                |
| 0.7     | 2026-03-21 | Added Section 2.3 (AI Agent Delegation): Kolt (2025), Humberd & Latham (2026), Jarrahi & Ritala (2025), Kolbjornsrud (2024), Vantrappen (2025), South et al. AD/MIT (ICML 2025), Tomasev et al. DeepMind (2026), IMDA agentic AI framework (2026). Positioned PACT against competitors. Removed incorrect SFA 04-N11 reference. 51 references.                                                                                                                          |
| 0.8     | 2026-03-21 | Cross-thesis coherence audit: EATP Conformant description now complete (reasoning traces included), classification level attribution corrected, Property 5 acknowledged as CO's domain. Section 10 (Architectural Inversion) added. Enterprise GRC positioning (SAP GRC, Microsoft Entra, Zero Trust). 55 references. Conditional accept (Round 7).                                                                                                                     |
| 0.1-WA  | 2026-03-21 | Repackaged as Working Architecture. Added provenance disclosure, Foundation independence statement, PACT reference implementation stats (133 modules, 41K LOC, 4,191 tests). Added Section 16 (promotion criteria). Shadow Agent Planning (analysis spec Part 6) earmarked for CO methodology.                                                                                                                                                                          |
| 1.0     | 2026-06-21 | Promoted from Working Architecture to a ratified Terrene Foundation standard, peer to CARE/EATP/CO, by founder determination that accumulated maturity evidence (production commercial deployment + open reference implementations + adversarial validation) is sufficient. Title "A Working Architecture" → "A Core Thesis"; citation key Hong (2026f) retained. Section 16 reframed as the promotion record. Supersedes ADR-003 Decision 1; see terrene journal 0034. |

---

_This paper is Hong (2026f), a Core Thesis derived from the theoretical foundation in Hong, J. (2026). "Constraint Theater: Governance Without Wealth Effects." PACT implements the recursive application of the formal model across organizational hierarchies (see Remark on Recursive Application). See also: Hong, J. (2026a). "CARE: A Core Thesis" for governance philosophy. Hong, J. (2026b). "EATP: A Core Thesis" for trust verification. Hong, J. (2026c). "CO: A Core Thesis" for methodology. Hong, J. (2026d). "COC: A Core Thesis" for development methodology. Hong, J. (2026e). "The Constrained Organization" for institutional design._
