# Chatbot RAG con Streamlit + FastAPI

Este proyecto implementa un chatbot basado en la arquitectura RAG (Retrieval-Augmented Generation), compuesto por:

- **Frontend:** Streamlit.
- **Backend:** FastAPI.
- **Embeddings:** SentenceTransformers (`all-MiniLM-L6-v2`).
- **Vector Store:** FAISS.
- **Generación:** Modelo LLM genérico (`distilgpt2`).

---

## 📁 Estructura del Proyecto

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
└── README.md
```

---

## 🚀 Instalación y Ejecución

### Prerequisitos

- Docker
- Docker Compose

### Paso a Paso

```bash
git clone https://github.com/tuusuario/chatbot-rag.git
cd chatbot-rag
docker-compose up --build
```

Accede a la interfaz en: [http://localhost:8501](http://localhost:8501)

---

## 📄 Detalles Técnicos

- **Backend** expone `POST /ask` que recibe una pregunta y devuelve una respuesta generada por el modelo.
- **RAGEngine** usa embeddings y recuperación contextual con FAISS.
- **LLM** se basa en `distilgpt2` usando `transformers.pipeline`.

---

## 📊 Diagrama de Arquitectura

Ver archivo [`architecture_diagram.puml`](architecture_diagram.puml)

---

## 🧠 Base de Conocimiento

Ubicada en `backend/app/data/knowledge_base.txt`. Puede reemplazarse por cualquier texto relevante al dominio.

---

## 🛠️ Dependencias

Instaladas automáticamente por Docker. Para entorno local:

```bash
cd backend
pip install -r requirements.txt
```

---

## ✍️ Créditos

Trabajo práctico - Master UM - Modelos de Lenguajes.
