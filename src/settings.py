from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

import models as models


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )
    is_development: bool = Field(False, env="IS_DEVELOPMENT")
    db_name: str = Field("bitcart", env="DB_DATABASE")
    db_user: str = Field("postgres", env="DB_USER")
    db_password: str = Field("", env="DB_PASSWORD")
    db_host: str = Field("127.0.0.1", env="DB_HOST")
    db_port: int = Field(5432, env="DB_PORT")
    secret_key: str = Field("secret", env="SECRET")
    algorithm: str = Field("HS256", env="ALGORITHM")

    @property
    def connection_str(self):
        if self.is_development:
            return (
                f"mongodb://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
                "?authSource=admin&retryWrites=true&w=majority"
            )
        else:
            return f"mongodb+srv://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}?retryWrites=true&w=majority"


async def initiate_database():
    client = AsyncIOMotorClient(Settings().connection_str)
    await init_beanie(
        database=client.get_default_database(), document_models=models.__all__
    )
