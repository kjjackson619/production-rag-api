from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def embed_query(query: str):
    response = client.embeddings.create(
        model=settings.EMBEDDING_MODEL,
        input=query
    )

    return response.data[0].embedding