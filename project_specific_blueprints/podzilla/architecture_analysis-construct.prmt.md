# Description: Template for analyzing architectural options for PodZilla features.
# Usage: Adapt for LLM input. Replace <placeholders> if present in specific constructs.
# ---

Analyze Architectural Options for Pod-Zilla <Feature Name>

Context:

You are the lead architect for Pod-Zilla, a lightweight microVM orchestrator in Go. We need to design the architecture for the <Feature Name> subsystem (e.g., "Pod Scheduling", "Inter-Pod Networking", "Volume Management"). The core goals are <list core goals like simplicity, security, performance, scalability as relevant>. Pod-Zilla currently uses <mention key existing components like microVM tech, state store type, API style>.

Goal:
Analyze and compare <Number, e.g., 2-3> distinct architectural approaches for implementing <Feature Name>. Provide a detailed breakdown of each approach, including its pros, cons, complexity, dependencies, and suitability for Pod-Zilla's specific context (lightweight, secure, microVM-based). Recommend the most pragmatic approach for the initial implementation, considering the current single-developer status, but also future scalability.

Tasks:
1.  **Approach 1 Description:** Detail the core mechanics, components involved, data flow.
2.  **Approach 1 Pros & Cons:** List specific advantages and disadvantages (technical, operational).
3.  **Approach 2 Description:** Detail the core mechanics, components involved, data flow.
4.  **Approach 2 Pros & Cons:** List specific advantages and disadvantages.
5.  **(Optional) Approach 3...**
6.  **Comparison Summary:** A table or bullet points directly comparing key aspects (e.g., complexity, performance potential, security implications, implementation effort).
7.  **Recommendation:** Justify the suggested approach for the initial phase of Pod-Zilla.

Output Format:
Structured analysis with clear headings for each approach, pros/cons, comparison, and recommendation. Focus on technical details relevant to Go implementation and microVM orchestration.
