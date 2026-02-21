# Context-Engine: LLM Token & File Optimizer

A specialized toolkit to solve the "Context Window Overflow" problem. This repo transforms massive `.md` roadmaps and documentation into lean, digestible modules for AI agents like Claude Code and Gemini.

## Features
- **Header-Based Chunking**: Split giant files into logical sections.
- **Context Mapping**: Generate an index so the AI can "request" specific files.
- **Token Estimation**: Pre-flight check to prevent "Limit Exceeded" errors.

## Why this exists
When managing complex enterprise roadmaps, uploading a single large file causes AI focus loss. This toolkit implements a **Tiered Context Architecture**—only feed the AI what it needs for the current task.
