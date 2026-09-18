from app.services.indexing import load_index, create_embeddings
from app.llm.groq_client import groq_client

import numpy as np


def search_similar_chunks(
    question: str,
    top_k: int = 3
):
    """
    Find the most relevant document chunks
    for the user's question.
    """

    chunks, embeddings = load_index()

    if not chunks:
        return []

    # Create embedding for the question
    question_embedding = create_embeddings([question])[0]

    # Calculate similarity scores
    scores = np.dot(
        embeddings,
        question_embedding
    )

    # Get top matching indexes
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for index in top_indices:
        results.append({
            "chunk": chunks[index],
            "score": float(scores[index])
        })

    return results


def ask_rag(
    question: str,
    top_k: int = 3
):
    """
    Complete RAG pipeline:

    Question
       ↓
    Search relevant chunks
       ↓
    Build context
       ↓
    Send context + question to Groq
       ↓
    Return answer
    """

    results = search_similar_chunks(
        question=question,
        top_k=top_k
    )

    if not results:
        context = "No relevant information was found."
    else:
        context_parts = []

        for result in results:
            context_parts.append(
                result["chunk"]
            )

        context = "\n\n".join(context_parts)

    answer = groq_client.generate_response(
        question=question,
        context=context
    )

    return {
        "answer": answer,
        "sources": results
    }