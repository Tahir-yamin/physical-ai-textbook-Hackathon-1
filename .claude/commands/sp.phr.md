# PHR Command

Create a Post-Implementation Historical Record documenting what was built and lessons learned.

## Usage
After completing implementation, document the journey for future reference.

## Process

1. **Document What Was Built**
   - Feature overview
   - What works now
   - How it was implemented

2. **Record Decisions**
   - Why certain approaches were chosen
   - Alternatives considered
   - Trade-offs made

3. **Capture Lessons**
   - What went well
   - What was challenging
   - What would you do differently

4. **PHR Structure**
   ```
   history/prompts/[feature-number]-[feature-name]/
   └── PHR-[number]-[feature-name].md
   
   ## Summary
   ## Implementation Details
   ## Key Decisions
   ## Challenges & Solutions
   ## Lessons Learned
   ## Future Improvements
   ```

5. **Include**
   - Screenshots/demos if applicable
   - Code snippets of key parts
   - Performance metrics
   - Links to related docs

## Template Location
See `.specify/templates/phr-template.prompt.md`

## Value
PHRs help future developers understand:
- Why things are the way they are
- What to avoid
- How to extend the feature
- Context for maintenance

## Next Steps
1. Archive prompt history
2. Update constitution if needed
3. Share learnings with team
