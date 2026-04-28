import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    EMBEDDING_MODEL: str = "text-embedding-3-small"
    GENERATION_MODEL: str = "gpt-4.1-mini"

    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100

    TOP_K: int = 5

settings = Settings()