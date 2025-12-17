# Architecture Overview

This document provides a high-level overview of the Physical AI & Humanoid Robotics Textbook system architecture.

## System Components

```
┌─────────────────────────────────────────────────────────┐
│                    USER BROWSER                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │           Docusaurus Frontend (React)             │  │
│  │  • Course Content (Modules 1-4)                  │  │
│  │  • Authentication UI (Sign In/Sign Up)           │  │
│  │  • Language Switcher (English/Urdu)              │  │
│  │  • Chat Widget Interface                         │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                         │
                         │ HTTP/WebSocket
                         ▼
┌─────────────────────────────────────────────────────────┐
│              FastAPI Backend (Python)                    │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Authentication Endpoints                         │  │
│  │  • /auth/signin                                  │  │
│  │  • /auth/signup                                  │  │
│  │  • /auth/profile                                 │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  RAG Chatbot Endpoints                           │  │
│  │  • /chat                                         │  │
│  │  • /session/new                                  │  │
│  │  • /session/{id}/history                         │  │
│  │  • /translate                                    │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
          │                    │                    │
          ▼                    ▼                    ▼
┌──────────────────┐  ┌──────────────┐  ┌──────────────┐
│  Neon Postgres   │  │   Qdrant     │  │  OpenRouter  │
│   Database       │  │   Vector DB   │  │     LLM      │
│                  │  │               │  │              │
│ • User Profiles  │  │ • Embeddings │  │ • Chat       │
│ • Chat Sessions  │  │ • Similarity │  │ • Generation │
│ • Chat Messages  │  │   Search     │  │              │
└──────────────────┘  └──────────────┘  └──────────────┘
```

## Technology Stack

### Frontend
- **Framework**: Docusaurus 3.x (React-based)
- **Language**: TypeScript
- **Styling**: CSS Modules
- **i18n**: Docusaurus i18n (English & Urdu)
- **Build Tool**: Webpack (via Docusaurus)

### Backend
- **Framework**: FastAPI (Python 3.10+)
- **Database**: Neon Postgres (Serverless PostgreSQL)
- **Vector DB**: Qdrant Cloud
- **LLM**: OpenRouter API
- **ORM**: SQLAlchemy

### Infrastructure
- **Hosting**: TBD (GitHub Pages for frontend, cloud for backend)
- **CI/CD**: GitHub Actions
- **Environment**: .env files for configuration

## Data Flow

### Authentication Flow
1. User clicks "Sign In" or tries to access protected content
2. Frontend displays auth modal
3. User submits credentials
4. POST request to `/auth/signin` or `/auth/signup`
5. Backend validates and creates session
6. User data stored in localStorage
7. Frontend grants access to protected routes

### RAG Chatbot Flow
1. User sends message via chat widget
2. POST request to `/chat` endpoint
3. Backend retrieves relevant context from Qdrant
4. Context + query sent to OpenRouter LLM
5. LLM generates response
6. Response returned to frontend
7. Message history stored in database

### Translation Flow
1. User clicks language switcher
2. Docusaurus loads appropriate i18n bundle
3. Page re-renders with selected language
4. RTL layout applied for Urdu

## Security

- **Authentication**: Session-based with localStorage
- **Password Storage**: bcrypt hashing
- **CORS**: Configured for localhost (development)
- **API Keys**: Stored in .env files (not in repo)
- **Route Protection**: Conditional rendering based on auth state

## Scalability Considerations

- **Frontend**: Static site generation allows CDN caching
- **Backend**: Async FastAPI scales well
- **Database**: Neon Postgres serverless auto-scales
- **Vector DB**: Qdrant Cloud handles scaling
- **LLM**: OpenRouter manages model scaling

## Future Improvements

- [ ] Add Redis for session management
- [ ] Implement JWT tokens
- [ ] Add rate limiting
- [ ] Implement caching layer
- [ ] Add monitoring and logging
- [ ] Add end-to-end tests

---

See also:
- [Frontend Architecture](frontend.md)
- [Backend Architecture](backend.md)
