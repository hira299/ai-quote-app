from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    version: str

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify API status
    """
    return HealthResponse(
        status="healthy",
        version="1.0.0"
    ) 