import os 
from fastapi import FastAPI
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: Optional[str] = "My FastAPI app"
    admin_email: Optional[str]
    database_url: Optional[str]
    secret_key: Optional[str]

    class Config:
        env_file = ".env"

settings = Settings()
app = FastAPI()

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "database_url": settings.database_url
    }