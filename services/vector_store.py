import json
from pathlib import Path

import numpy as np


INDEX_PATH = Path(
    "data/vector_index/index.json"
)


def load_index() -> list[dict]:

    if not INDEX_PATH.exists():
        return []

    with INDEX_PATH.open(
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


def save_index(index: list[dict]):

    INDEX_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with INDEX_PATH.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            index,
            file,
            ensure_ascii=False,
        )


def add_to_index(
    chunk_id: int,
    document_id: int,
    content: str,
    embedding: list[float],
):

    index = load_index()

    index.append(
        {
            "chunk_id": chunk_id,
            "document_id": document_id,
            "content": content,
            "embedding": embedding,
        }
    )

    save_index(index)


def search_similar(
    query_embedding: list[float],
    top_k: int = 5,
) -> list[dict]:

    index = load_index()

    if not index:
        return []

    query_vector = np.array(
        query_embedding,
        dtype=np.float32,
    )

    results = []

    for item in index:

        vector = np.array(
            item["embedding"],
            dtype=np.float32,
        )

        score = float(
            np.dot(
                query_vector,
                vector,
            )
        )

        results.append(
            {
                "chunk_id": item["chunk_id"],
                "document_id": item["document_id"],
                "content": item["content"],
                "score": score,
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True,
    )

    return results[:top_k]