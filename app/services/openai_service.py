import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

class OpenAIService:
    @staticmethod
    async def get_response(prompt: str, language: str = "ru"):
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            n=1,
            stop=None,
            language=language
        )
        return response.choices[0].text.strip()
