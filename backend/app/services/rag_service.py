import json
import os

import torch
from app.domain.rag_engine import RAGEngine
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from transformers import pipeline
from huggingface_hub import login



def _load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


class RAGService:
    def __init__(self):
        self._docs = self._load_documents(["app/data/chunks_glosario_mtg.json", "app/data/chunks_reglas_mtg.json"])
        self._embedder = None
        self._index = None
        self._generator = None
        self._engine = None

    def load_model(self):
        if not torch.cuda.is_available():
            print("❌ No se detectó GPU. Instala torch con soporte CUDA y asegúrate de que el contenedor la ve.")
            raise RuntimeError(
                "❌ No se detectó GPU. Instala torch con soporte CUDA y asegúrate de que el contenedor la ve.")

        self._embedder = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")
        self._index = self._build_index(self._docs)
        login("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")

        pipe = pipeline(
            "text-generation",
            model="meta-llama/Llama-2-7B-instruct",
            torch_dtype=torch.bfloat16,
            device_map="auto",
            temperature=0.1,
            do_sample=True,
            repetition_penalty=1.1,
            return_full_text=False,
            max_new_tokens=500,
        )
        self._generator = HuggingFacePipeline(pipeline=pipe)
        self._engine = RAGEngine(self._embedder, self._generator, self._index, self._docs)

    def _load_documents(self, paths):
        glossary_doc = [
            Document(
                page_content=item["Definicion"],
                metadata={
                    "source": item["Termino"],
                    "tipo": "glosario"
                }
            )
            for item in _load_json(paths[0])
        ]
        rules_doc = [
            Document(page_content=item["Texto"],
                     metadata={
                         "source": item["Regla"],
                         "tipo": "regla"
                     }
                     )
            for item in _load_json(paths[1])
        ]
        return rules_doc + glossary_doc

    def _build_index(self, docs):
        return FAISS.from_documents(docs, self._embedder)

    def answer(self, question: str) -> str:
        return self._engine.query(question)


service = RAGService()
