from app.services.openai_service import OpenAIService

class TextAnalysisService:
    @staticmethod
    async def analyze_text(text: str, language: str):
        prompt = f"Analyze the following text and provide a summary, key points, and sentiment analysis. Text: {text}"
        response = await OpenAIService.get_response(prompt, language)
        return response

    @staticmethod
    async def analyze_document(document_text: str, language: str):
        prompt = f"Analyze the following document and provide a summary, main topics, and key findings. Document: {document_text}"
        response = await OpenAIService.get_response(prompt, language)
        return response