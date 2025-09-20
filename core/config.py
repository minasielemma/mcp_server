
import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import Any

from pydantic import (
    AnyHttpUrl,
    PostgresDsn,
    field_validator,
)
from pydantic_core.core_schema import ValidationInfo

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.getenv("POSTGRES_DB", "mcp_db")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))

FASTAPI_SECRET_KEY = os.getenv("FASTAPI_SECRET_KEY", "supersecret")
JWT_ALGORITHM = "HS256"

EMAIL_ACCOUNT = os.getenv("EMAIL_ACCOUNT", "etguesthome@gmail.com")
APP_PASSWORD = os.getenv("APP_PASSWORD", "your-app-password")
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"



class Settings(BaseSettings):
    PROJECT_NAME: str = "MCP Server"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    ENV_NAME: str = "local"

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: str | None, values: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v

        postgres_dsn = PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_SERVER"),
            path=values.data.get("POSTGRES_DB"),
        )
        return postgres_dsn.unicode_string()

    AWS_LAMBDA_INITIALIZATION_TYPE: str = "Not a lambda"


settings = Settings(
    POSTGRES_SERVER=POSTGRES_HOST,
    POSTGRES_USER=POSTGRES_USER,
    POSTGRES_PASSWORD=POSTGRES_PASSWORD,
    POSTGRES_DB=POSTGRES_DB,
)