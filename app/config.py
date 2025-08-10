import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""
    
    # General settings
    APP_NAME: str = os.getenv("APP_NAME", "MyApp")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")

    # Database settings
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_USER: str = os.getenv("DB_USER", "user")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")
    DB_NAME: str = os.getenv("DB_NAME", "mydatabase")

    # Logging settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
