from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__name__).parent
ENV_PATH = BASE_DIR / '.env'


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ENV_PATH
        case_sensitive = True


settings = Settings()
