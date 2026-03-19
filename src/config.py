from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class EnvData(BaseSettings):
    # REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_PORT: int

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


class Config(BaseModel):
    env_data: EnvData = EnvData()
    
config = Config()