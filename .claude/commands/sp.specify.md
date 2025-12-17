# Specify Command

Create a detailed specification document for a feature or component.

## Usage
When you need to create a new specification, this command guides you through the process of documenting requirements, architecture, and implementation details.

## Process

1. **Understand the Feature**
   - What problem does this solve?
   - Who are the users?
   - What are the key requirements?

2. **Create Specification Structure**
   ```
   specs/[feature-number]-[feature-name]/
   ├── spec.md              # Main specification
   ├── checklists/
   │   └── requirements.md  # Requirements checklist
   ├── plan.md              # Implementation plan
   ├── tasks.md             # Task breakdown
   ├── research.md          # Research and decisions
   └── quickstart.md        # Quick reference
   ```

3. **Document Components**
   - **Goals**: What will this achieve?
   - **Non-Goals**: What is out of scope?
   - **Requirements**: Functional and non-functional
   - **Architecture**: High-level design
   - **API/Interfaces**: Contracts and schemas
   - **Dependencies**: What does this rely on?
   - **Testing**: How will we verify it works?

4. **Review Criteria**
   - Is it clear and unambiguous?
   - Are all requirements captured?
   - Can someone implement from this?
   - Are edge cases considered?

## Template Location
See `.specify/templates/spec-template.md` for the full template.

## Next Steps
After specification:
1. Run `sp.clarify` if anything is unclear
2. Run `sp.plan` to create implementation plan
3. Run `sp.tasks` to break down into tasks
