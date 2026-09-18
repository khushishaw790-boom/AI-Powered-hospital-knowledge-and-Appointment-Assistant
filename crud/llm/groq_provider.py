from app.llm.base import LLMProvider


class GroqProvider(
    LLMProvider
):

    def __init__(
        self,
        api_key: str
    ):
        self.api_key = api_key

    def generate(
        self,
        prompt: str
    ) -> str:

        # Groq API integration will be added
        # during the AI phase.

        return "Groq response will be implemented here."