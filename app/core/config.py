from pydantic import BaseSettings, SecretStr
from functools import lru_cache

class Settings(BaseSettings):
    OPENAI_API_KEY: SecretStr
    DATABASE_URL: str = "postgresql+asyncpg://postgres:mdkaii@localhost/vazorat_ai"
    JWT_SECRET_KEY: SecretStr
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALLOWED_HOSTS: list = ["*"]
    DEBUG: bool = False

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()