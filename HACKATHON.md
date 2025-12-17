# Hackathon Submission: Physical AI & Humanoid Robotics Textbook

## 🏆 Panaversity Hackathon I: Physical AI & Humanoid Robotics

### Project Overview
An AI-powered, bilingual (English/Urdu) textbook platform for teaching Physical AI and Humanoid Robotics, featuring an integrated RAG chatbot for interactive learning.

---

## ✅ Core Features (100 Points)

### 1. Comprehensive Textbook Content ✅
- **4 Complete Modules**:
  - Module 1: The Robotic Nervous System (ROS 2)
  - Module 2: The Digital Twin (Gazebo & Unity)
  - Module 3: The AI-Robot Brain (NVIDIA Isaac™)
  - Module 4: Vision-Language-Action (VLA)
- **21 Bilingual Pages** (English/Urdu)
- **MDX Format** with interactive components

### 2. RAG Chatbot Integration ✅
- **FastAPI Backend** with Qdrant vector database
- **Context-Aware Responses** using OpenRouter LLM
- **Text Selection Feature** - Select any text and ask questions
- **Session Management** with PostgreSQL (Neon)
- **Streaming Responses** for real-time UX

### 3. User Authentication ✅
- **Sign Up/Sign In** functionality
- **User Profiles** with hardware/software background
- **Protected Routes** - Authentication required for docs
- **Session Persistence** via localStorage

### 4. Modern UI/UX ✅
- **Docusaurus 3.x** framework
- **Dark Mode Support**
- **Responsive Design**
- **Beautiful Animations** (particle background, smooth transitions)
- **Chat Widget** with floating interface

---

## 🌟 Bonus Features (200 Points)

### Bilingual Support (50 pts) ✅
- **English ↔ Urdu** language switching
- **Client-Side i18n** (react-i18next)
- **RTL Support** for Urdu
- **Gulzar Font** for authentic Urdu typography
- **No URL Routing** - seamless switching

### Advanced Chat Features (50 pts) ✅
- **Context Injection** (user profile, page context, conversation history)
- **Text Selection Queries** - Select and ask
- **Chat History** persistence
- **Markdown Rendering** in responses
- **Code Syntax Highlighting**

### User Experience (50 pts) ✅
- **Particle Background** animation
- **Smooth Transitions** and hover effects
- **Loading States** and error handling
- **Accessibility** features
- **SEO Optimization**

### Technical Excellence (50 pts) ✅
- **TypeScript** for type safety
- **Component Architecture** (reusable, modular)
- **API Integration** (OpenRouter, Qdrant, Neon)
- **Error Handling** and validation
- **Performance Optimization**

---

## 🚀 Live Demo

- **Website**: [Demo Video Placeholder - To be uploaded]
- **Repository**: https://github.com/tahir-yamin/physical-ai-textbook
- **GitHub Pages**: [To be deployed]

---

## 📊 Technical Stack

### Frontend
- **Framework**: Docusaurus 3.x
- **Language**: TypeScript/React
- **Styling**: CSS Modules
- **i18n**: react-i18next
- **State Management**: React Hooks

### Backend
- **Framework**: FastAPI (Python)
- **Vector DB**: Qdrant
- **Database**: PostgreSQL (Neon)
- **LLM**: OpenRouter (multiple models)
- **Embeddings**: text-embedding-3-small

### Deployment
- **Frontend**: GitHub Pages
- **Backend**: [To be configured]

---

## 📁 Project Structure

```
physical-ai-textbook/
├── textbook/                 # Frontend (Docusaurus)
│   ├── docs/                # MDX content (21 pages)
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── theme/           # Custom theme
│   │   └── i18n/            # i18n configuration
│   └── backend/             # FastAPI server
│       ├── main.py          # Server entry point
│       ├── embeddings.py    # Document embedding
│       └── requirements.txt
├── docs/                    # Project documentation
│   ├── architecture/        # Architecture docs
│   ├── development/         # Development guides
│   ├── deployment/          # Deployment guides
│   └── project-details/     # Lessons learned
├── guides/                  # User guides
├── specs/                   # Specifications
└── .SP/                     # Spec-Kit Plus artifacts
```

---

## 🎯 Hackathon Achievements

| Category | Points | Status |
|----------|--------|--------|
| Core Features | 100 | ✅ Complete |
| Bilingual Support | 50 | ✅ Complete |
| Advanced Chat | 50 | ✅ Complete |
| User Experience | 50 | ✅ Complete |
| Technical Excellence | 50 | ✅ Complete |
| **Total** | **300** | **✅ 100%** |

---

## 🔧 Setup & Installation

See [README.md](./README.md) for detailed setup instructions.

Quick start:
```bash
# Frontend
cd textbook
npm install
npm start

# Backend
cd textbook/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python embeddings.py
python main.py
```

---

## 📝 Documentation

- [README.md](./README.md) - Project overview
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Contribution guidelines
- [CHANGELOG.md](./CHANGELOG.md) - Version history
- [CITATION.md](./CITATION.md) - Citation information
- [docs/](./docs/) - Comprehensive documentation

---

## 🙏 Acknowledgments

- **Panaversity** for organizing the hackathon
- **Docusaurus** team for the excellent framework
- **OpenRouter** for LLM API access
- **Qdrant** for vector database
- **Neon** for PostgreSQL hosting

---

**Built with ❤️ for the Physical AI & Humanoid Robotics community**
