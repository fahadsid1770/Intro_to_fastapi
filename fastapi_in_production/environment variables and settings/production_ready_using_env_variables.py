import os
import uvicorn
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name : Optional[str] = "My fastapi app"
    admin_email: Optional[str] = "email@gmail.com"
    database_url: Optional[str] = "hfkjdshfkjshd"
    secret_key: Optional[str] = "jfkdjfkd"
    allowed_hosts: Optional[List] = ["*"]
    debug: Optional[bool] = False

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()

app = FastAPI()

@app.middleware("http")   # runs before and/or after every request 
async def validate_host(request, call_next):
    settings = get_settings()
    host = request.headers.get("host","").split(":")[0]
    if settings.debug or host in settings.allowed_hosts:
        return await call_next(request)
    raise HTTPException(status_code=400, detail="Invalid host")

@app.get("/info")
async def info():
    settings = get_settings()
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "debug_mode": settings.debug
    }

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)