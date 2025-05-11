from app.domain.rag_engine import RAGEngine
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np

class RAGService:
    def __init__(self):
        self._docs = self._load_documents("app/data/knowledge_base.txt")
        self._embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self._generator = pipeline("text-generation", model="distilgpt2")
        self._index = self._build_index(self._docs)
        self._engine = RAGEngine(self._embedder, self._generator, self._index, self._docs)

    def _load_documents(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    def _build_index(self, docs):
        embeddings = self._embedder.encode(docs)
        index = faiss.IndexFlatL2(384)
        index.add(np.array(embeddings))
        return index

    def answer(self, question: str) -> str:
        return self._engine.query(question)
