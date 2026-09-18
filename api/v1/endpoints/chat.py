from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field

from app.llm.groq_client import groq_client


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


class ChatRequest(BaseModel):
    question: str
    top_k: int = Field(default=3, ge=1, le=10)


class ChatResponse(BaseModel):
    answer: str


@router.post("/", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    token: str = Depends(oauth2_scheme),
):
    answer = groq_client.generate_response(
        question=request.question,
        context="",
    )

    return {
        "answer": answer
    }