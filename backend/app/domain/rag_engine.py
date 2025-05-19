from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


def _format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


class RAGEngine:
    def __init__(self, embedder, generator, index, documents):
        self._embedder = embedder
        self._generator = generator
        self._index = index
        self._docs = documents
        self._retriever = self._index.as_retriever(search_type="similarity",
                                                   search_kwargs={"k": 3})

    def query(self, question: str) -> str:
        prompt_template = """
        <|start_header_id|>user<|end_header_id|>
        Eres un asistente respondiendo cuestiones referidas al reglamento del juego de cartas Magic: The Gathering.
        Se te provee el reglamento completo con su glosario para responder una pregunta.
        Debes proveer una respuesta conversacional y en inglés.
        La respuesta siempre debe especificar los números de las secciones en que se basa.
        Si no sabes la respuesta porque no se encuentra en el reglamento del contexto dado responde con "No lo sé"
        No inventes la respuesta. No generes información que no se encuentre en el contexto dado.
        Siempre terminar el mensaje recomendando consultar con un juez si se encuentra en un torneo.
        Question: {question}
        Context: {context}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
        """

        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=prompt_template,
        )

        rag_chain = (
                {"context": self._retriever | _format_docs, "question": RunnablePassthrough()}
                | prompt
                | self._generator
                | StrOutputParser()
        )
        return rag_chain.invoke(question)
