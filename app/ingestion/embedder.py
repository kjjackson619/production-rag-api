from openai import OpenAI
from app.config import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)

def embed_chunks(chunks: list):
    texts = [chunk["text"] for chunk in chunks]

    reponse = client.embeddings.create(
        model=settings.EMBEDDING_MODEL,
        input=texts
    )

    embeddings = []

    for chunk, emb in zip(chunks, response.data):
        embeddings.append({
            "embedding": emb.embedding,
            "text": chunk["text"],
            "source": chunk["source"]
        })

    return embeddings