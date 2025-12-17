# Tasks Command

Break down the implementation plan into specific, actionable tasks.

## Usage
After creating a plan, use this to generate detailed task lists.

## Process

1. **Review Plan**
   - Read plan.md for the feature
   - Understand each phase

2. **Create Task List**
   ```
   specs/[feature]/tasks.md
   
   ## Phase 1: [Name]
   - [ ] Task 1: Description
     - Acceptance criteria
     - Estimated time
   - [ ] Task 2: Description
   ...
   ```

3. **Task Guidelines**
   - **Specific**: Clear what needs to be done
   - **Measurable**: Clear completion criteria
   - **Achievable**: Can be done in reasonable time
   - **Relevant**: Contributes to phase goal
   - **Time-bound**: Has an estimate

4. **Task Format**
   ```markdown
   - [ ] Create UserService class
     - AC: Class has methods for CRUD operations
     - AC: All methods have unit tests
     - AC: Errors are properly handled
     - Est: 2 hours
   ```

## Template Location
See `.specify/templates/tasks-template.md`

## Next Steps
1. Review tasks with team
2. Assign priorities
3. Use `sp.implement` to start executing
