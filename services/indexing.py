from pathlib import Path
import json

import numpy as np
from sentence_transformers import SentenceTransformer


INDEX_DIR = Path("data/index")

EMBEDDINGS_FILE = INDEX_DIR / "embeddings.npy"
CHUNKS_FILE = INDEX_DIR / "chunks.json"

MODEL_NAME = "all-MiniLM-L6-v2"

_model = None


def get_model():
    """Load the embedding model only once."""

    global _model

    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)

    return _model


def create_embeddings(chunks: list[str]) -> np.ndarray:
    """Convert text chunks into embeddings."""

    if not chunks:
        return np.empty((0, 384))

    model = get_model()

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    return embeddings


def save_index(
    chunks: list[str],
    embeddings: np.ndarray
) -> None:
    """Save chunks and embeddings."""

    INDEX_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    np.save(
        EMBEDDINGS_FILE,
        embeddings
    )

    with open(
        CHUNKS_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            chunks,
            file,
            ensure_ascii=False,
            indent=2
        )


def build_index(
    chunks: list[str]
) -> np.ndarray:
    """Create embeddings and save the index."""

    embeddings = create_embeddings(chunks)

    save_index(
        chunks,
        embeddings
    )

    return embeddings


def index_document(
    chunks: list[str]
) -> dict:
    """
    Create an index for a document.

    This function is used by the FastAPI
    indexing endpoint.
    """

    if not chunks:
        raise ValueError(
            "No text chunks were provided."
        )

    embeddings = build_index(chunks)

    return {
        "message": "Document indexed successfully",
        "chunks": len(chunks),
        "embedding_dimension": int(
            embeddings.shape[1]
        ) if embeddings.ndim == 2 else 0,
        "embeddings_file": str(
            EMBEDDINGS_FILE
        ),
        "chunks_file": str(
            CHUNKS_FILE
        ),
    }


def load_index():
    """Load the saved RAG index."""

    if not EMBEDDINGS_FILE.exists():
        raise FileNotFoundError(
            f"Embeddings file not found: {EMBEDDINGS_FILE}"
        )

    if not CHUNKS_FILE.exists():
        raise FileNotFoundError(
            f"Chunks file not found: {CHUNKS_FILE}"
        )

    embeddings = np.load(
        EMBEDDINGS_FILE
    )

    with open(
        CHUNKS_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        chunks = json.load(file)

    return chunks, embeddings