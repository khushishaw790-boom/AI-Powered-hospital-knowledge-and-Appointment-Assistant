import os

from groq import Groq


class GroqClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = os.getenv(
            "GROQ_MODEL",
            "openai/gpt-oss-120b"
        )

        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not set")

        self.client = Groq(api_key=self.api_key)

    def generate_response(self, question: str, context: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a hospital knowledge assistant. "
                        "Answer the user's question using the provided context. "
                        "If the answer is not available in the context, "
                        "say that the information is not available."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Context:\n{context}\n\n"
                        f"Question:\n{question}"
                    ),
                },
            ],
            temperature=0.2,
            max_tokens=1024,
        )

        return response.choices[0].message.content


# Create the object that chat.py is importing
groq_client = GroqClient()