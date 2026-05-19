# Document RAG System

A full-stack Retrieval-Augmented Generation (RAG) system for intelligent document querying using FastAPI, Qdrant, SentenceTransformers, Groq LLMs, Streamlit, Docker, and Inngest.

---

## Features

- PDF upload and ingestion
- Semantic vector search
- AI-powered question answering
- Context-aware retrieval
- Streamlit frontend
- FastAPI backend
- Qdrant vector database
- Groq LLM integration
- Inngest async workflows
- Dockerized deployment

---

## Tech Stack

- FastAPI
- Streamlit
- Qdrant
- SentenceTransformers
- Groq API
- Inngest
- Docker
- Python

---

## Architecture

```text
PDF
 ↓
Chunking
 ↓
Embeddings
 ↓
Qdrant Vector DB
 ↓
Semantic Retrieval
 ↓
Groq LLM
 ↓
Final Answer

Installation
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/document-rag-system.git
cd document-rag-system
2. Create Virtual Environment
python -m venv .venv

Activate environment:

Windows
.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
Running Qdrant

Run Qdrant using Docker:

docker run -p 6333:6333 qdrant/qdrant
Running FastAPI Backend
uvicorn main:app --reload

Backend runs on:

http://127.0.0.1:8000
Running Streamlit Frontend
streamlit run app.py

Frontend runs on:

http://localhost:8501
Running Inngest Dev Server
npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
Dockerization

Build Docker image:

docker build -t document-rag-system .

Run container:

docker run -p 8000:8000 -p 8501:8501 --env-file .env document-rag-system
API Endpoints
Query Documents
POST /query

Example request:

{
  "question": "What is this document about?",
  "top_k": 5
}
Future Improvements
Hybrid search
Reranking
Source citations
Multi-document support
Authentication
Chat memory
Cloud deployment
Author

Anirudh Gupta
