from fastapi import FastAPI
from mangum import Mangum
from src.api import router as api_router

app = FastAPI(
    title="AI Quote App API",
    description="Backend API for the AI Quote App",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")

# Create handler for AWS Lambda
handler = Mangum(app)

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 