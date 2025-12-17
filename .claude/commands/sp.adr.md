# ADR Command

Create an Architecture Decision Record.

## Usage
Document important architectural or technical decisions.

## What Is An ADR?
A record of a key technical decision, including:
- What we decided
- Why we decided it
- Alternatives considered  
- Consequences

## When To Create ADR
- Choosing a framework/library
- Database selection
- API design approach
- Deployment strategy
- Major refactoring
- Security approach

## ADR Structure
```
specs/[feature]/adrs/
└── ADR-001-[decision-name].md

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
What is the issue we're facing?

## Decision
What we're doing about it.

## Consequences
What becomes easier/harder?

## Alternatives Considered
What else did we think about?
```

## Template Location
See `.specify/templates/adr-template.md`

## Example ADRs
- "Use PostgreSQL for user data"
- "Adopt React for UI framework"
- "Implement JWT for authentication"
- "Deploy on Vercel + Railway"

## Benefits
- Provides historical context
- Explains rationale
- Helps new team members
- Prevents repeated discussions

## Next Steps
1. Document decision
2. Share with team
3. Update relevant specs
