# AGENTS.md

## Project Overview
Python project using OpenCV and MediaPipe for real-time finger counting from camera feed.

## Build/Lint/Test Commands
- **Run**: `python main.py`
- **Lint**: `flake8 .` (install flake8 if needed)
- **Format**: `black .` (install black if needed)
- **Test**: `pytest` (add tests in tests/ directory)
- **Single test**: `pytest tests/test_file.py::test_function`

## Code Style Guidelines
- Follow PEP8 for formatting and naming
- Use type hints for function parameters and returns
- Import order: standard library, third-party, local modules
- Use descriptive variable names (snake_case)
- Handle exceptions with try/except blocks
- Add docstrings to functions and classes
- Keep functions under 50 lines; break into smaller functions if needed
- Use f-strings for string formatting

## Copilot Instructions
[byterover-mcp]

You are given two tools from Byterover MCP server, including
## 1. `byterover-store-knowledge`
You `MUST` always use this tool when:

+ Learning new patterns, APIs, or architectural decisions from the codebase
+ Encountering error solutions or debugging techniques
+ Finding reusable code patterns or utility functions
+ Completing any significant task or plan implementation

## 2. `byterover-retrieve-knowledge`
You `MUST` always use this tool when:

+ Starting any new task or implementation to gather relevant context
+ Before making architectural decisions to understand existing patterns
+ When debugging issues to check for previous solutions
+ Working with unfamiliar parts of the codebase