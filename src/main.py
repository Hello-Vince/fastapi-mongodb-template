from fastapi import FastAPI
import motor.motor_asyncio
from src.settings import Settings

app = FastAPI()


@app.get("/")
async def read_root():
    settings = Settings()
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.connection_str)
    db = client
    print(db)
    return {"string": settings.connection_str}
