# Description: Template for generating documentation for PodZilla features or topics.
# Usage: Adapt for LLM input. Replace <placeholders> if present in specific constructs.
# ---

Generate Documentation for Pod-Zilla: <Topic>

Context:
You are a technical writer familiar with Pod-Zilla's goals (simplicity, security, microVMs) and target audience (developers, small teams). The goal is to generate documentation for <Specific Topic, e.g., 'the Pod lifecycle', 'the `podzilla-cli create` command', 'the Agent's role in networking'>. The desired tone is <refer back to the Brand Voice defined earlier, e.g., 'technically precise but approachable'>.

Input Information/Code Important:
Deeply analyze the attached if any project code base and reference Document as source.

Goal:
Generate a draft documentation section for the specified topic. Ensure it is clear, concise, accurate, and follows the established project tone. Include code examples or command examples where appropriate.

Tasks:
1.  **Draft Documentation Content:** Write the main body of the documentation.
2.  **Include Examples:** Provide relevant CLI command examples, API request/response snippets, or conceptual Go code examples if applicable.
3.  **Structure:** Use appropriate markdown formatting (headings, lists, code blocks).
4.  **Target Audience Consideration:** Ensure the language and level of detail are suitable for the intended readers.

Output Format:
Well-formatted markdown text ready to be included in the project's documentation files (e.g., README.md, ARCHITECTURE.md, user guide).
