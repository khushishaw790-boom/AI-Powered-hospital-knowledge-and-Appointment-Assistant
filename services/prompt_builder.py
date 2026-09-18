def build_prompt(
    question: str,
    context: str
) -> str:

    return f"""
You are a hospital knowledge assistant.

Answer the user's question using only
the provided hospital context.

If the answer is not available in the
context, say that the information is
not available in the hospital knowledge base.

Hospital Context:
{context}

User Question:
{question}
"""