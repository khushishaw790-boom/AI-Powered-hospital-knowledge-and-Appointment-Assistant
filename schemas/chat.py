from fastapi import (
    APIRouter,
    Depends,
)

from app.api.v1.endpoints.auth import (
    get_current_user,
)
from app.db.models.user import User
from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)
from app.services.rag import ask_rag


router = APIRouter(
    prefix="/chat",
    tags=["AI Chatbot"],
)


@router.post(
    "/",
    response_model=ChatResponse,
)
def chat(
    data: ChatRequest,
    current_user: User = Depends(
        get_current_user
    ),
):

    result = ask_rag(
        question=data.question,
        top_k=data.top_k,
    )

    return result