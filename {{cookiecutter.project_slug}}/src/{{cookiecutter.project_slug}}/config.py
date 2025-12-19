import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    database_url: str = os.getenv("DATABASE_URL", "{{ cookiecutter.database_url }}")
    database_echo: bool = os.getenv("DATABASE_ECHO", "false").lower() == "true"


settings = Settings()
