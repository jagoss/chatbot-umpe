from fastapi import APIRouter
from pydantic import BaseModel
from app.services import RAGService

router = APIRouter()
service = RAGService()

class Query(BaseModel):
    question: str

@router.post("/question")
def ask_question(query: Query):
    return {"answer": service.answer(query.question)}
