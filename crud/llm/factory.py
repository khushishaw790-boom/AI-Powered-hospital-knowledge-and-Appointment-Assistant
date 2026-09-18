from app.llm.retrieval_only import (
    RetrievalOnlyProvider
)

from app.llm.groq_provider import (
    GroqProvider
)


def get_llm_provider(
    provider: str,
    api_key: str = ""
):

    if provider == "groq":
        return GroqProvider(api_key)

    return RetrievalOnlyProvider()