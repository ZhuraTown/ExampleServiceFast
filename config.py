from typing import Sequence

from dotenv import load_dotenv
from pydantic import PostgresDsn, RedisDsn, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class InfrastructureSettings(BaseSettings):
    # POSTGRES CONFIG
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: int
    postgres_dsn: PostgresDsn | None = None

    @field_validator('postgres_dsn', mode='before')  # noqa
    @classmethod
    def get_postgres_dsn(cls, _, info: ValidationInfo):
        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            username=info.data['db_user'],
            password=info.data['db_password'],
            host=info.data['db_host'],
            port=info.data['db_port'],
            path=info.data['db_name'],
        )

    # REDIS CONFIG
    redis_host: str
    redis_port: int
    redis_db: str
    redis_password: str | None = None
    redis_user: str | None = None
    redis_dsn: RedisDsn | None = None

    @field_validator('redis_dsn', mode='before')  # noqa
    @classmethod
    def get_redis_dsn(cls, _, info: ValidationInfo):
        return RedisDsn.build(
            scheme='redis',
            host=info.data['redis_host'],
            port=info.data['redis_port'],
            path=info.data['redis_db'],
        )


class Settings(BaseSettings):
    infrastructure: InfrastructureSettings = InfrastructureSettings()


class ApiConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='API_')

    SECRET: str = "SECRET"
    HOST: str = '0.0.0.0'
    PORT: int = 8000
    RELOAD: bool = False
    WORKERS: int = 4
    ALLOWED_HOSTS: Sequence[str] = ['*']


api_settings = ApiConfig()
settings = Settings()