# Polymathic-Cognition-Constructs

This repository stores a curated collection of "Cognition Constructs" - advanced prompts and system instructions for AI interactions, covering various domains and use cases.

## Structure

The repository is organized hierarchically:

-   `meta_instructions/`: Prompts about prompting or generating complex outputs (like codebases).
-   `jailbreak_constructs/`: Prompts for testing AI response boundaries.
-   `project_specific_blueprints/`: Detailed prompt sequences for example projects (e.g., PodZilla, X-in-Go).
-   `technology_domains/`: Prompts related to specific technologies (Cloud, Go, IaC, DevOps, UI/UX).
-   `learning_methodologies/`: Templates for structured learning or expert emulation.

Within each directory:
-   A `.prmt.md` file often serves as an entry point, containing general or high-level prompts for that category.
-   Specific sub-topics or tools have dedicated `[topic]-construct.prmt.md` files.

Each file starts with a brief description for the file itself. Individual constructs within a file will also have their own descriptive headers.

## CLI Tool

A Python CLI tool (`generate_prompt_cli.py`) is provided at the root (currently a placeholder).
