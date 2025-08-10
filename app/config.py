import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""
    
    # General settings
    APP_NAME: str = os.getenv("APP_NAME", "MyApp")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")

    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/mydatabase")
    # DB_HOST: str = os.getenv("DB_HOST", "localhost")
    # DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    # DB_USER: str = os.getenv("DB_USER", "user")
    # DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")
    # DB_NAME: str = os.getenv("DB_NAME", "mydatabase")

    #JWT Settings
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    # # Logging settings
    # LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
