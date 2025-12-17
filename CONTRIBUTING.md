# Contributing to Physical AI & Humanoid Robotics Textbook

Thank you for your interest in contributing to this project! This textbook is designed to help students learn about Physical AI and Humanoid Robotics through an interactive, AI-powered platform.

## How to Contribute

### Reporting Issues
- Use the GitHub Issues tab to report bugs or suggest features
- Provide clear descriptions and steps to reproduce issues
- Include screenshots or error messages when applicable

### Content Contributions
- **Textbook Content**: Improve existing modules or suggest new topics
- **Translations**: Help improve Urdu translations or add new languages
- **Documentation**: Enhance guides, tutorials, or API documentation

### Code Contributions

1. **Fork the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/physical-ai-textbook.git
   cd physical-ai-textbook
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow existing code style
   - Test your changes locally
   - Update documentation as needed

4. **Test Thoroughly**
   ```bash
   cd textbook
   npm install
   npm start  # Test frontend
   npm run build  # Verify build works
   
   cd backend
   python main.py  # Test backend
   ```

5. **Commit and Push**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Provide clear description of changes
   - Reference any related issues
   - Wait for review and address feedback

## Development Guidelines

### Code Style
- **Frontend**: Follow React and TypeScript best practices
- **Backend**: Follow PEP 8 for Python code
- **MDX Content**: Use consistent formatting and structure

### Commit Messages
Follow conventional commits format:
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test additions or changes
- `chore:` Maintenance tasks

### Testing Requirements
- Test all new features locally
- Ensure no breaking changes
- Verify bilingual content works (EN/UR)
- Test RAG chatbot functionality

## Questions?

Feel free to open an issue for questions or discussions about contributions.

Thank you for helping make this educational resource better! 🚀
