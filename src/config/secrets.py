from pydantic_settings import BaseSettings, SettingsConfigDict


class Secrets(BaseSettings):
    """
    Loads secrets/configuration from the environment.
    """

    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="ignore")

    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"


secrets = Secrets()
