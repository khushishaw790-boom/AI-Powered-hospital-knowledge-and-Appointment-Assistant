from app.llm.base import LLMProvider


class RetrievalOnlyProvider(
    LLMProvider
):

    def generate(
        self,
        prompt: str
    ) -> str:

        return (
            "Retrieval-only mode is active. "
            "The answer must be generated from "
            "the retrieved hospital knowledge."
        )