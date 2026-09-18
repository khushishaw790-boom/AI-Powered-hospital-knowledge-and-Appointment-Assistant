from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(
    tags=["Documents"]
)


# =========================================================
# GET ALL DOCUMENTS
# =========================================================

@router.get(
    "/",
    summary="Get all documents",
    description="Returns all documents stored in the hospital knowledge base."
)
def get_documents():
    return {
        "documents": [
            {
                "id": 1,
                "filename": "hospital_information.pdf",
                "status": "indexed"
            },
            {
                "id": 2,
                "filename": "departments.pdf",
                "status": "indexed"
            }
        ]
    }


# =========================================================
# GET DOCUMENT BY ID
# =========================================================

@router.get(
    "/{document_id}",
    summary="Get document by ID",
    description="Returns information about a specific knowledge document."
)
def get_document(document_id: int):

    return {
        "id": document_id,
        "filename": "hospital_information.pdf",
        "status": "indexed"
    }


# =========================================================
# UPLOAD DOCUMENT
# =========================================================

@router.post(
    "/upload",
    summary="Upload document",
    description="Uploads a PDF, DOCX, TXT or Markdown document to the hospital knowledge base."
)
async def upload_document(
    file: UploadFile = File(...)
):

    allowed_extensions = [
        ".pdf",
        ".docx",
        ".txt",
        ".md"
    ]

    filename = file.filename or ""

    extension = ""

    if "." in filename:
        extension = "." + filename.split(".")[-1].lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX, TXT and Markdown files are allowed."
        )

    return {
        "message": "Document uploaded successfully",
        "filename": filename,
        "content_type": file.content_type,
        "status": "uploaded"
    }


# =========================================================
# DELETE DOCUMENT
# =========================================================

@router.delete(
    "/{document_id}",
    summary="Delete document",
    description="Deletes a document from the hospital knowledge base."
)
def delete_document(document_id: int):

    return {
        "message": "Document deleted successfully",
        "document_id": document_id
    }