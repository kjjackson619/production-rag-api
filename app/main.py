from fastapi import FastAPI
from app.db.vector_store import VectorStore
from app.retrieval.embedder import embed_query
from app.retrieval.retriever import Retriever
from app.generation.prompt import build_context
from app.generation.generator import generate_answer

app = FastAPI()

# Initialize global components
vector_store = VectorStore()
retriever = Retriever(vector_store)

@app.post("/ask")
def ask(question: str):
    # Step 1: Embed query
    query_vector = embed_query(question)

    # Step 2: Retrieve relevant chunks
    retrieved_chunks = retriever.retrieve(query_vector)

    # Step 3: Build context
    context = build_context(retrieved_chunks)

    # Step 4: Generate answer
    answer = generate_answer(context, question)

    return {
        "answer": answer,
        "sources": [c["source"] for c in retrieved_chunks]
    }