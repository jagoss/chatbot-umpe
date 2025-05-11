
class RAGEngine:
    def __init__(self, embedder, generator, index, documents):
        self._embedder = embedder
        self._generator = generator
        self._index = index
        self._docs = documents

    def query(self, question: str) -> str:
        # Obtener embedding de la pregunta
        q_embedding = self._embedder.encode([question])

        # Buscar el contexto más relevante
        D, I = self._index.search(q_embedding, k=1)
        context = self._docs[I[0][0]]

        # Armar prompt para el modelo generador
        prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"

        # Generar respuesta con el modelo LLM
        result = self._generator(prompt, max_length=100, do_sample=True)

        # Limpiar salida
        return result[0]["generated_text"].split("Answer:")[-1].strip()
