# Description: Template for troubleshooting issues within the PodZilla system.
# Usage: Adapt for LLM input. Replace <placeholders> if present in specific constructs.
# ---

Troubleshoot Pod-Zilla Issue: 
<Brief Issue Summary>

Context: You are an expert diagnostician for distributed systems and Go applications, specifically familiar with Pod-Zilla's architecture (microVMs, Go components, state store, networking). I am encountering an issue: <Detailed description of the problem, e.g., 'Pods fail to get IP addresses on node X', 'API server crashes with panic X', 'MicroVM fails to start with error Y'>. This started happening after <mention recent changes, if any>.

Important:
Deeply analyze the attached if any project code base and reference Document as source.

Relevant Information:
*   Component(s) Involved: <e.g., API Server, Agent on Node X, Scheduler>
*   Error Message(s): `<Paste full error messages or logs>`
*   Observed Behavior: <What actually happens vs. what is expected>
*   Steps to Reproduce (if known): <List the steps>
*   Environment Details (if relevant): <OS version, Go version, microVM runner version>

Goal:
Help diagnose the potential root causes of this issue. Provide a structured list of possible causes, suggest specific diagnostic steps or commands to run (e.g., `kubectl` equivalent for Pod-Zilla, specific logs to check, network diagnostic tools), and propose potential fixes or areas to investigate further in the Go codebase.

Tasks:
1.  **Hypothesize Potential Causes:** List likely reasons for the observed issue, categorized (e.g., Networking, State Consistency, Configuration Error, Code Bug in Component X).
2.  **Suggest Diagnostic Steps:** Provide concrete commands or procedures to gather more information relevant to each hypothesis (e.g., "Check agent logs on Node X for CNI errors", "Verify etcd connectivity from the API server", "Inspect microVM console output").
3.  **Identify Code Investigation Areas:** Point to specific functions, modules, or logic within the Pod-Zilla codebase that might be related to the potential causes.
4.  **Propose Potential Solutions (if possible):** Based on likely causes, suggest potential fixes or configuration changes.

Output Format:
A structured troubleshooting guide with clear steps and explanations. Prioritize the most likely causes based on the provided information.
