from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.api.v1.endpoints.auth import (
    get_current_user,
)
from app.db.models.user import User
from app.db.session import get_db
from app.services.indexing import (
    index_document,
)


router = APIRouter(
    prefix="/index",
    tags=["Knowledge Indexing"],
)


@router.post(
    "/document/{document_id}"
)
def index_knowledge_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):

    if current_user.role not in {
        "admin",
        "staff",
    }:
        raise HTTPException(
            status_code=403,
            detail=(
                "Only admin or staff "
                "can index documents"
            ),
        )

    try:

        chunks = index_document(
            document_id=document_id,
            db=db,
        )

        return {
            "message": "Document indexed successfully",
            "document_id": document_id,
            "chunks_created": len(chunks),
        }

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error),
        )

    except Exception as error:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Indexing failed: {str(error)}",
        )