# Checklist Command

Create or update requirements and verification checklists.

## Usage
Maintain checklists to track requirements and ensure nothing is missed.

## Types of Checklists

### 1. Requirements Checklist
```
specs/[feature]/checklists/requirements.md

## Functional Requirements
- [ ] FR-1: User can login with email/password
- [ ] FR-2: User can reset password
...

## Non-Functional Requirements
- [ ] NFR-1: Login responds within 2s
- [ ] NFR-2: Passwords hashed with bcrypt
...

## Security Requirements
## Performance Requirements
## Accessibility Requirements
```

### 2. Implementation Checklist
- [ ] Code written
- [ ] Tests written (80%+ coverage)
- [ ] Documentation updated
- [ ] Code reviewed
- [ ] Deployed to staging
- [ ] User acceptance testing
- [ ] Deployed to production

### 3. Pre-Deployment Checklist
- [ ] All tests passing
- [ ] No console errors
- [ ] Performance acceptable
- [ ] Security review done
- [ ] Backup plan ready
- [ ] Monitoring configured

## Template Location
See `.specify/templates/checklist-template.md`

## Best Practices
- Keep checklists up to date
- Check off as you complete
- Add new items as discovered
- Review before deployment

## Next Steps
1. Create feature checklist
2. Track progress regularly
3. Don't deploy until all checked
