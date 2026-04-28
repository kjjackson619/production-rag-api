from app.config import settings

def chunk_text(document: dict):
    text = document["text"]
    source = document["source"]

    chunks = []
    start = 0

    while start < len(text):
        end = start + settings.CHUNK_SIZE

        chunk = text[start:end]

        chunks.append({
            "text": chunk,
            "source": source
        })

        start += settings.CHUNK_SIZE - settings.CHUNK_OVERLAP

    return chunks