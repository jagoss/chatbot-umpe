# RAG Chatbot with Streamlit + FastAPI

This project implements a chatbot based on the RAG (Retrieval-Augmented Generation) architecture, composed of:

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Embeddings:** SentenceTransformers (`all-MiniLM-L6-v2`)
- **Vector Store:** FAISS
- **Generation:** Generic LLM model (`distilgpt2`)

---

## 📁 Project Structure

```
chatbot_project/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── core/
│   │   ├── domain/
│   │   │   └── rag_engine.py
│   │   ├── services/
│   │   │   └── rag_service.py
│   │   ├── data/
│   │   │   └── knowledge_base.txt
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── run_chatbot.sh
└── README.md
```

---

## 🚀 Installation and Execution

### Prerequisites

- Docker
- Docker Compose

### Quick Start

Run the provided shell script to automatically build and launch the backend and frontend containers:

```bash
./run_chatbot.sh
```

This script will:

1. Build the backend image and start it on port `8000`.
2. Build the frontend image and start it on port `8501`.
3. Automatically link both containers so the frontend can access the backend.

Then, access the UI at: [http://localhost:8501](http://localhost:8501)

Alternatively, you can run the containers manually:

```bash
# Backend
docker build -t rag-backend ./backend
docker run -d -p 8000:8000 rag-backend

# Frontend (after backend is up)
docker build -t rag-frontend ./frontend
docker run -d -p 8501:8501 --link rag-backend rag-frontend
```

---

## 📄 Technical Details

- **Backend** exposes `POST /ask` endpoint which receives a user question and returns a generated answer.
- **RAGEngine** handles embeddings and context retrieval via FAISS.
- **LLM** uses `distilgpt2` via `transformers.pipeline`.

---

## 📊 Architecture Diagram

See [`architecture_diagram.puml`](architecture_diagram.puml)

---

## 🧠 Knowledge Base

Located at `backend/app/data/knowledge_base.txt`. You can replace it with any domain-relevant content.

---

## 🛠️ Dependencies

Installed automatically via Docker. For manual setup:

```bash
cd backend
pip install -r requirements.txt
```

---

## ✍️ Credits

Final project - Master UM - Language Models Workshop.
