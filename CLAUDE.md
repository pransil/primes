# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an agentic programming workspace that uses Model-Driven Computation (MDC) rules to automate software development workflows. The repository contains structured rules for generating Product Requirements Documents (PRDs), breaking them down into task lists, and managing implementation workflows.

## Core Architecture

### MDC Rule System
- **`.mdc` files**: Contains structured rules with YAML frontmatter and markdown content
- **Rule Structure**: Each rule defines processes, outputs, and interaction models for specific development phases

### Workflow Components

1. **PRD Generation** (`create-prd.mdc`): Converts initial ideas into structured Product Requirements Documents
2. **Task Generation** (`generate-tasks.mdc`): Breaks PRDs into actionable developer task lists  
3. **Task Management** (`process-task-list.mdc`): Defines protocols for task execution and completion

### File Organization

- **`/tasks/`**: Target directory for generated PRDs and task lists
  - PRDs: `prd-[feature-name].md`
  - Task lists: `tasks-[prd-file-name].md`
- **`idea.md`**: Contains initial feature ideas/requirements input

## Development Workflows

### PRD Creation Process
1. Start with `idea.md` containing initial feature description
2. AI asks clarifying questions using letter/number options
3. Generate structured PRD with: Introduction, Goals, User Stories, Functional Requirements, Non-Goals, Success Metrics
4. Target audience: Junior developers

### Task List Generation Process  
1. Analyze existing PRD
2. Generate high-level parent tasks (~5 tasks)
3. Wait for user confirmation ("Go")
4. Break down into detailed sub-tasks
5. Identify relevant files and test files

### Task Implementation Protocol
- **One sub-task at a time**: Wait for user permission before proceeding
- **Completion sequence**: Mark sub-task complete → run full test suite → stage changes → commit with conventional format → mark parent task complete
- **Test command**: Use appropriate test runner (`pytest`, `npm test`, etc.)
- **Commit format**: Conventional commits with descriptive multi-line messages

## Key Rules

### Interaction Model
- Use option lists (letter/number) for user responses
- Explicit pause points requiring "Go" confirmation
- Progressive disclosure: high-level first, then details

### File Management
- Always update task lists after work
- Maintain "Relevant Files" section with descriptions
- Include both implementation and test files

### Quality Gates
- Run full test suite before any commits
- Clean up temporary files before committing
- Use conventional commit format with context references

## Target Audience

All generated documents and task lists assume **junior developers** as the primary audience, requiring explicit, unambiguous requirements without jargon.