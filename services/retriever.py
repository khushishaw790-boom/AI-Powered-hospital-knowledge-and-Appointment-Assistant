from app.services.embedding import create_embedding


def retrieve(
    query: str,
    vector_store,
    top_k: int = 5
):
    query_embedding = create_embedding(
        query
    )

    return vector_store.search(
        query_embedding,
        top_k
    )