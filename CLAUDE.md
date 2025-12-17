# CLAUDE.md - AI-Assisted Development Guide

## Overview
This project uses Spec-Kit methodology for AI-assisted development with Claude. All commands and templates are located in `.claude/` and `.specify/` directories.

## Spec-Kit Commands

Access via `.claude/commands/`:

- **sp.specify** - Create feature specifications
- **sp.clarify** - Clarify unclear requirements
- **sp.plan** - Create implementation plans
- **sp.tasks** - Break down into actionable tasks
- **sp.implement** - Guide implementation
- **sp.phr** - Document post-implementation
- **sp.adr** - Record architectural decisions
- **sp.checklist** - Manage requirement checklists
- **sp.analyze** - Analyze code and specs
- **sp.constitution** - View/update project principles
- **sp.git.commit_pr** - Git workflow guidance

## Development Workflow

### 1. Specification Phase
```bash
# Create spec
sp.specify

# Clarify requirements
sp.clarify

# Review and approve spec
```

### 2. Planning Phase
```bash
# Create implementation plan
sp.plan

# Break into tasks
sp.tasks

# Review and approve plan
```

### 3. Implementation Phase
```bash
# Implement feature
sp.implement

# Track progress in tasks.md
# Update checklist as you go
```

### 4. Documentation Phase
```bash
# Create PHR
sp.phr

# Update ADRs if needed
sp.adr
```

## Directory Structure

```
.claude/                    # Claude commands
  commands/                 # Spec-Kit commands
  settings.local.json       # Project settings

.specify/                   # Spec-Kit artifacts
  docs/                     # Documentation
  memory/                   # Constitution, context
  templates/                # File templates
  
history/                    # Prompt history
  prompts/                  # Organized by feature
  
specs/                      # Feature specifications
  [feature-number]-[name]/
    spec.md
    plan.md
    tasks.md
    checklists/
    
```

## Templates

All templates in `.specify/templates/`:
- `spec-template.md` - Feature specification
- `plan-template.md` - Implementation plan
- `tasks-template.md` - Task breakdown
- `phr-template.prompt.md` - Post-implementation record
- `adr-template.md` - Architecture decision record
- `checklist-template.md` - Requirements checklist

## Best Practices

1. **Always start with specification**
2. **Clarify before implementing**
3. **Break down into small tasks**
4. **Document decisions**
5. **Create PHR after completion**

## Constitution

Project principles and guidelines are in `.specify/memory/constitution.md`.  
Review before making major decisions.

## Git Workflow

Follow conventional commits:
```
feat(auth): add password reset
fix(chat): resolve message ordering
docs(readme): update installation steps
```

See `sp.git.commit_pr` for full guidance.

## Questions?

Refer to:
- `.claude/commands/` for command details
- `.specify/docs/` for methodology docs  
- `history/prompts/` for past implementation examples
