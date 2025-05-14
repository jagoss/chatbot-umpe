# app/api/routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import service

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/question")
async def ask_question(query: Query):
    q = query.question.strip()
    if not q:
        raise HTTPException(400, "La pregunta no puede estar vacía")
    answer = service.answer(q)
    return {"answer": answer}
