<div align="center">

# 🚀 Document RAG System

### AI-Powered Document Question Answering using RAG

<img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi" />
<img src="https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge&logo=streamlit" />
<img src="https://img.shields.io/badge/Qdrant-VectorDB-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Groq-LLM-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker" />

</div>

---

# 📌 Overview

Document RAG System is a full-stack Retrieval-Augmented Generation (RAG) application that allows users to:

- 📄 Upload PDF documents
- 🔍 Perform semantic search
- 🤖 Ask AI-powered questions about documents
- ⚡ Get context-aware answers using LLMs

The system uses:
- **FastAPI** for backend APIs
- **Qdrant** as vector database
- **SentenceTransformers** for embeddings
- **Groq LLMs** for response generation
- **Streamlit** for frontend UI
- **Inngest** for async workflows
- **Docker** for containerization

---

# 🏗️ Architecture

```text
PDF Upload
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
Final Response
```

---

# ⚙️ Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/document-rag-system.git

cd document-rag-system
```

---

## 2️⃣ Add Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# 🐳 Run the Application

## Start Qdrant

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

## Build Docker Image

```bash
docker build -t document-rag-system .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 -p 8501:8501 --env-file .env document-rag-system
```

---

# ⚡ Run Inngest Dev Server

```bash
npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
```

---

# 🌐 Access the App

## Streamlit Frontend

```text
http://localhost:8501
```

## FastAPI Docs

```text
http://localhost:8000/docs
```

---

# ✨ Features

- 📄 PDF ingestion
- 🔍 Semantic vector search
- 🤖 AI-powered question answering
- ⚡ Context-aware retrieval
- 🧠 Vector embeddings
- 🐳 Dockerized deployment
- 🔄 Async ingestion workflows

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Backend APIs |
| Streamlit | Frontend UI |
| Qdrant | Vector Database |
| SentenceTransformers | Embeddings |
| Groq | LLM Inference |
| Inngest | Async Workflows |
| Docker | Containerization |

---

# 🚀 Future Improvements

- Hybrid Search
- Reranking
- Source Citations
- Multi-document Support
- Authentication
- Chat Memory
- Cloud Deployment

---

<div align="center">

## ⭐ If you liked the project, consider giving it a star!

</div>
