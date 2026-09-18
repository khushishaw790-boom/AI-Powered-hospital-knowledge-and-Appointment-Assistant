from app.services.emergency_guard import (
    is_emergency,
    emergency_response
)

from app.services.prompt_builder import (
    build_prompt
)


def answer_question(
    question: str,
    vector_store,
    llm
):

    if is_emergency(question):
        return {
            "answer": emergency_response(),
            "sources": []
        }

    results = vector_store.search(
        [],
        top_k=5
    )

    context = "\n\n".join(
        item["text"]
        for item in results
    )

    prompt = build_prompt(
        question,
        context
    )

    answer = llm.generate(prompt)

    sources = [
        {
            "document": "hospital knowledge base",
            "relevance": 0.0
        }
    ]

    return {
        "answer": answer,
        "sources": sources
    }