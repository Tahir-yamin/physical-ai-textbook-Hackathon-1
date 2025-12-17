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
   - ROS 2 fundamentals and architecture
   - Nodes, topics, services, and actions
   - Python integration with rclpy
   - URDF for robot description

2. **Module 2: The Digital Twin (Gazebo & Unity)**
   - Physics simulation with Gazebo
   - High-fidelity visualization with Unity
   - Sensor simulation (LiDAR, cameras, IMU)

3. **Module 3: The AI-Robot Brain (NVIDIA Isaac™)**
   - Isaac Sim for photorealistic simulation
   - Hardware-accelerated perception
   - Nav2 path planning

4. **Module 4: Vision-Language-Action (VLA)**
   - Voice control with OpenAI Whisper
   - LLM-based task planning
   - Multimodal robot control

## 🚀 Setup Instructions

### Prerequisites

- Node.js 20+
- Python 3.10+
- Accounts for:
  - [Qdrant Cloud](https://cloud.qdrant.io/) (Free tier)
  - [Neon Database](https://neon.tech/) (Free tier)
  - [OpenRouter](https://openrouter.ai/) (For LLM access)
  - GitHub (For deployment)

### Frontend Setup (Docusaurus)

```bash
cd textbook
npm install
npm start  # Run locally at http://localhost:3000
```

### Backend Setup (RAG Chatbot)

```bash
cd textbook/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your API keys and database URLs

# Initialize database and embed documents
python database.py  # Creates database tables
python embeddings.py  # Embeds textbook content into Qdrant

# Run backend server
python main.py  # Runs on http://localhost:8000
```

### Environment Variables

Create `backend/.env` with:

```env
# OpenRouter API
OPENAI_API_KEY=your_openrouter_api_key
OPENAI_BASE_URL=https://openrouter.ai/api/v1

# Qdrant Vector Database
QDRANT_URL=your_qdrant_cluster_url
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_COLLECTION_NAME=physical_ai_textbook

# Neon Postgres Database
DATABASE_URL=postgresql://user:password@host/database

# LLM Configuration
LLM_MODEL=openai/gpt-3.5-turbo
EMBEDDING_MODEL=text-embedding-3-small
```

## 📦 Deployment

### Deploy to GitHub Pages

1. Update `docusaurus.config.ts`:
   - Set `url` to `https://your-username.github.io`
   - Set `baseUrl` to `/your-repo-name/`
   - Set `organizationName` to your GitHub username
   - Set `projectName` to your repository name

2. Enable GitHub Pages:
   - Go to repository Settings → Pages
   - Source: GitHub Actions

3. Push to GitHub:
   ```bash
   git add .
   git commit -m "Deploy textbook"
   git push origin main
   ```

The GitHub Actions workflow will automatically build and deploy your site.

### Deploy Backend

Deploy the FastAPI backend to:
- **Railway**: Connect GitHub repo, set environment variables
- **Render**: Deploy as web service with environment variables
- **Fly.io**: Use `fly launch` and configure secrets

Update `CORS_ORIGINS` in backend `.env` to include your deployed frontend URL.

## 🤖 How to Use the Chatbot

1. **Ask General Questions**: "What is ROS 2?" or "How does VSLAM work?"
2. **Select Text**: Highlight any text from the textbook and ask specific questions about it
3. **Follow-up Questions**: The chatbot maintains conversation context
4. **View Sources**: Each response shows which book sections were used

## 🏗️ Architecture

```
Frontend (Docusaurus + React)
    ↓ HTTP
Backend (FastAPI)
    ↓
RAG Engine
    ├─→ Qdrant (Vector Search)
    ├─→ OpenAI/OpenRouter (LLM)
    └─→ Neon Postgres (Sessions/History)
```

## 📊 Hackathon Scoring

- ✅ Core Requirements (100 points):
  - AI/Spec-driven book creation with Docusaurus
  - Deployed to GitHub Pages
  - RAG chatbot with OpenAI ChatKit SDK equivalent
  - FastAPI backend with Neon and Qdrant
  - Text-selection based queries

- 🎁 Bonus Features (up to 200 points):
  - Authentication with better-auth
  - Content personalization
  - Urdu translation
  - Claude Code Subagents/Skills

## 🛠️ Tech Stack

- **Frontend**: Docusaurus, React, TypeScript
- **Backend**: FastAPI, Python
- **Vector DB**: Qdrant Cloud
- **Database**: Neon Serverless Postgres
- **LLMs**: OpenRouter (GPT-3.5, GPT-4)
- **Embeddings**: OpenAI text-embedding-3-small
- **Deployment**: GitHub Pages, Railway/Render

## 📝 License

This project is created for the Panaversity Hackathon I.

## 🙏 Acknowledgments

- Course content based on Panaversity's Physical AI & Humanoid Robotics curriculum
- Built with guidance from the reference materials and lesson learned documents

---

**Created for Hackathon I: Physical AI & Humanoid Robotics Textbook**  
Submission Deadline: November 30, 2025
