from fastapi import (
    APIRouter,
    Depends,
)
from pydantic import BaseModel

from app.api.v1.endpoints.auth import (
    get_current_user,
)
from app.db.models.user import User
from app.services.embedding import (
    create_embedding,
)
from app.services.vector_store import (
    search_similar,
)


router = APIRouter(
    prefix="/search",
    tags=["Knowledge Search"],
)


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


@router.post("/")
def search_knowledge(
    data: SearchRequest,
    current_user: User = Depends(
        get_current_user
    ),
):

    query_embedding = create_embedding(
        data.query
    )

    results = search_similar(
        query_embedding=query_embedding,
        top_k=data.top_k,
    )

    return {
        "query": data.query,
        "results": results,
    }