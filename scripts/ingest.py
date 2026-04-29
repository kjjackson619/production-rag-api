from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import embed_chunks
from app.db.vector_store import VectorStore

def run_ingestion():
    vector_store = VectorStore()

    documents = load_documents("data/")

    all_chunks = []
    for doc in documents:
        chunks = chunk_text(doc)
        all_chunks.extend(chunks)

    embeddings = embed_chunks(all_chunks)

    vector_store.add(embeddings)

    print(f"Ingested {len(all_chunks)} chunks.")

if __name__ == "__main__":
    run_ingestion()