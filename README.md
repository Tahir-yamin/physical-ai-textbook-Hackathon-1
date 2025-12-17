# Physical AI & Humanoid Robotics Textbook

A comprehensive, AI-powered textbook for teaching Physical AI and Humanoid Robotics, featuring an integrated RAG chatbot for interactive learning.

## 🎯 Features

- ✅ **Comprehensive Course Content**: 4 modules covering ROS 2, Gazebo/Unity, NVIDIA Isaac, and Vision-Language-Action
- ✅ **RAG Chatbot**: AI-powered assistant that answers questions about the textbook content
- ✅ **Text-Selection Queries**: Select any text from the book and ask questions about it
- ✅ **Beautiful UI**: Modern, responsive design with dark mode support
- ✅ **Interactive**: Chat history, session management, and contextual responses

## 📚 Course Modules

1. **Module 1: The Robotic Nervous System (ROS 2)**
2. **Module 2: The Digital Twin (Gazebo & Unity)**
3. **Module 3: The AI-Robot Brain (NVIDIA Isaac™)**
4. **Module 4: Vision-Language-Action (VLA)**

## 🚀 Quick Start

### Frontend
```bash
cd textbook
npm install
npm start
```

### Backend
```bash
cd textbook/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Edit with your API keys
python embeddings.py  # Embed documents
python main.py  # Start server
```

## 📝 Full Documentation

See the complete setup guide in the textbook/README.md file.

## 🏆 Hackathon Submission

Created for **Panaversity Hackathon I: Physical AI & Humanoid Robotics**

**Core Features (100 pts)**: ✅ Complete
**Bonus Features**: Can be added based on requirements

---

Built with Docusaurus, FastAPI, Qdrant, Neon, and OpenRouter
