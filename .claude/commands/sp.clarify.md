# Clarify Command

Clarify requirements or specifications before implementation.

## Usage
When a specification is unclear or incomplete, use this to ask questions and refine understanding.

## Process

1. **Review Specification**
   - Read spec.md carefully
   - Note ambiguities
   - Identify gaps

2. **Types of Clarifications**
   - **Requirements**: What exactly should it do?
   - **Scope**: What's included/excluded?
   - **Edge Cases**: How to handle unusual situations?
   - **Dependencies**: What does it need?
   - **Performance**: How fast/scalable?
   - **Security**: What protections needed?

3. **Document Questions**
   ```
   specs/[feature]/clarifications.md
   
   ## Questions
   1. Q: Should we support offline mode?
      A: Yes, with 7-day cache
   
   2. Q: Max file upload size?
      A: 10MB for now, 100MB in v2
   ```

4. **Update Specification**
   - Incorporate answers into spec.md
   - Remove ambiguities
   - Add missing details

## Best Practices
- Ask specific questions
- Provide context for each question
- Suggest possible answers
- Document decisions clearly

## Next Steps
1. Get answers from stakeholders
2. Update spec.md with clarifications
3. Run `sp.plan` with clear requirements
