from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, Any
from app.services.openai_service import OpenAIService
from app.services.text_analysis_service import TextAnalysisService
from app.core.auth import get_current_user
from app.db.database import get_db
from app.models.models import Query, User
from pydantic import BaseModel

router = APIRouter()

class QueryModel(BaseModel):
    query: str
    language: str = "ru"

class TextAnalysisModel(BaseModel):
    text: str
    language: str = "ru"

class DocumentComparisonModel(BaseModel):
    doc1: str
    doc2: str
    language: str = "ru"

@router.post("/query/")
async def process_query(
    query: QueryModel, 
    current_user: User = Depends(get_current_user), 
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    try:
        response = await OpenAIService.get_response(query.query, query.language)
        
        # Сохраняем запрос в базу данных
        db_query = Query(
            text=query.query,
            language=query.language,
            response=response,
            user_id=current_user.id
        )
        db.add(db_query)
        await db.commit()
        
        return {"response": response}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze_text/")
async def analyze_text(
    text_analysis: TextAnalysisModel, 
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    try:
        analysis = await TextAnalysisService.analyze_text(text_analysis.text, text_analysis.language)
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze_document/")
async def analyze_document(
    text_analysis: TextAnalysisModel, 
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    try:
        analysis = await TextAnalysisService.analyze_document(text_analysis.text, text_analysis.language)
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/compare_documents/")
async def compare_documents(
    comparison: DocumentComparisonModel, 
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    try:
        analysis = await TextAnalysisService.compare_documents(comparison.doc1, comparison.doc2, comparison.language)
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))