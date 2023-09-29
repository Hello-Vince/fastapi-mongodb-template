from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )
    db_name: str = Field("bitcart", env="DB_DATABASE")
    db_user: str = Field("postgres", env="DB_USER")
    db_password: str = Field("", env="DB_PASSWORD")
    db_host: str = Field("127.0.0.1", env="DB_HOST")
    db_port: int = Field(5432, env="DB_PORT")

    @property
    def connection_str(self):
        return f"mongodb+srv://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
