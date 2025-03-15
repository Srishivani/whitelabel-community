from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    SECRET_KEY: str = "test-secret-key-for-testing"  # default for testing
    DATABASE_URL: str = "mongodb://localhost:27017/test"
    SMTP_SERVER: str = "localhost"
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    STRIPE_API_KEY: Optional[str] = None

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
