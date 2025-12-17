# Git Commit & PR Command

Create proper git commits and pull requests following conventions.

## Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `perf`: Performance improvement
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples
```
feat(auth): add password reset functionality

- Create reset token generation
- Add email service integration
- Implement reset confirmation page

Closes #123
```

```
fix(chat): resolve message ordering issue

Messages were displaying in random order due to
missing timestamp sort. Added proper sorting by
createdAt timestamp.

Fixes #456
```

## Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Checklist
- [ ] Tests pass
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] No console errors

## Screenshots (if applicable)

## Related Issues
Closes #123
```

## Best Practices
1. Write clear, descriptive commits
2. Keep commits atomic (one logical change)
3. Reference issues in commits
4. Update CHANGELOG.md
5. Squash before merging if needed

## Next Steps
1. Stage changed files
2. Write commit message
3. Push to branch
4. Create pull request
5. Request review
