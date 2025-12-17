# Plan Command

Create an implementation plan based on an existing specification.

## Usage
After creating a specification, use this command to plan the implementation approach.

## Process

1. **Review Specification**
   - Read the spec.md thoroughly
   - Understand all requirements
   - Note dependencies

2. **Break Down Into Phases**
   - Identify logical implementation phases
   - Order by dependency (what must come first)
   - Estimate complexity per phase

3. **Plan Structure**
   ```
   specs/[feature]/plan.md
   
   ## Overview
   ## Prerequisites
   ## Phase 1: [Name]
   - Goals
   - Tasks
   - Verification
   ## Phase 2: [Name]
   ...
   ## Testing Strategy
   ## Deployment Plan
   ## Rollback Plan
   ```

4. **Consider**
   - **Dependencies**: What exists? What needs building?
   - **Risks**: What could go wrong?
   - **Testing**: How to verify each phase?
   - **Rollback**: How to undo if needed?

## Template Location
See `.specify/templates/plan-template.md`

## Next Steps
1. Get plan reviewed/approved
2. Run `sp.tasks` to create detailed task list
3. Run `sp.implement` to start execution
