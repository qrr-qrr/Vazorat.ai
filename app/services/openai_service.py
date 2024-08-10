import openai
from app.core.config import settings

class OpenAIService:
    @staticmethod
    async def get_response(query: str, language: str):
        openai.api_key = settings.OPENAI_API_KEY
        
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are an AI assistant for the Ministries of Tajikistan. Respond in {language}."},
                    {"role": "user", "content": query}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error in OpenAI API call: {str(e)}")
