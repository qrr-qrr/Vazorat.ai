from fastapi import APIRouter, HTTPException
from app.services.openai_service import OpenAIService

router = APIRouter()

@router.post("/query/")
async def process_query(query: str, language: str = "ru"):
    try:
        response = await OpenAIService.get_response(query, language)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
