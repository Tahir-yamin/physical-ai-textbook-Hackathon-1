# Contributing to Physical AI Textbook

Thank you for your interest in contributing to the Physical AI & Humanoid Robotics Textbook! This guide will help you get started.

## Ways to Contribute

### 1. Content Development
- Improve existing course modules
- Add examples and exercises
- Create new learning materials
- Fix typos and improve clarity

### 2. Translation
- Translate content from English to Urdu
- Review and improve existing Urdu translations
- Help with other language translations
- See [Translation Guide](translation-guide.md) for details

### 3. Technical Improvements
- Fix bugs and issues
- Improve performance
- Enhance user experience
- Add new features

### 4. Documentation
- Improve setup guides
- Write tutorials
- Document best practices
- Update architecture docs

## Getting Started

### Prerequisites
- Node.js 18+ (for frontend)
- Python 3.10+ (for backend)
- Git for version control
- A text editor (VS Code recommended)

### Setup Development Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/physical-ai-textbook.git
   cd physical-ai-textbook
   ```

2. **Setup Frontend**
   ```bash
   cd textbook
   npm install
   npm start
   ```

3. **Setup Backend**
   ```bash
   cd textbook/backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python main.py
   ```

## Development Workflow

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 2. Make Changes
- Write clear, concise code
- Follow existing code style
- Add comments where helpful
- Test your changes locally

### 3. Test Your Changes
- Run frontend: `npm start` in `/textbook`
- Run backend: `python main.py` in `/textbook/backend`
- Test authentication flow
- Test language switching
- Verify chat functionality

### 4. Commit Your Changes
```bash
git add .
git commit -m "Description of your changes"
```

Use clear commit messages:
- `feat: Add new feature`
- `fix: Fix bug description`
- `docs: Update documentation`
- `style: Format code`
- `refactor: Refactor code`

### 5. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear description of changes
- Why the changes are needed
- How you tested the changes

## Code Style Guidelines

### JavaScript/TypeScript
- Use TypeScript for new code
- Follow existing naming conventions
- Use meaningful variable names
- Add JSDoc comments for functions

### Python
- Follow PEP 8 style guide
- Use type hints
- Write docstrings for functions/classes
- Keep functions focused and small

### Markdown
- Use clear headers
- Include code examples
- Add links where relevant
- Keep line length reasonable

## Testing

Before submitting:
- [ ] Frontend loads without errors
- [ ] Backend starts successfully
- [ ] Authentication works
- [ ] Language switching works
- [ ] Chat functionality works
- [ ] No console errors

## Reporting Issues

Found a bug? Please create an issue with:
- Clear description
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots if applicable

## Questions?

- Check existing documentation in `/docs`
- Review the guides in `/guides`
- Look at similar implementations in the codebase
- Ask in project discussions

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

Thank you for contributing! 🎉
