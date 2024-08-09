from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router
from app.core.config import settings

app = FastAPI(title="Vazorat AI")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Vazorat AI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
