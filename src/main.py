from fastapi import FastAPI
from src.settings import Settings

app = FastAPI()


@app.get("/")
async def read_root():
    settings = Settings()
    return {"string": settings.connection_str}
