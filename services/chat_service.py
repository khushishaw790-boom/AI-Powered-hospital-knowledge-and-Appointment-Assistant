from app.services.rag_service import answer_question


def chat(
    question: str,
    vector_store,
    llm
):

    return answer_question(
        question=question,
        vector_store=vector_store,
        llm=llm
    )