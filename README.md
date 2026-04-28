Production RAG API
A modular, production-style Retrieval-Augmented Generation (RAG) system built with FastAPI, FAISS, and OpenAI.
Overview
This project implements a complete RAG pipeline that allows users to query custom datasets using natural language, with responses grounded in retrieved context rather than model hallucination.
The system is designed to reflect real-world AI architecture patterns used in production environments.
Architecture
The system is divided into two core pipelines:
1. Ingestion Pipeline (Offline)
Load raw documents
Chunk text with overlap
Generate embeddings
Store vectors in FAISS
2. Query Pipeline (Runtime)
Embed user query
Retrieve top-K relevant chunks
Inject context into prompt
Generate grounded response using LLM
Tech Stack
Python
FastAPI
FAISS (vector search)
OpenAI API (embeddings + generation)
NumPy
Features
Modular architecture (ingestion, retrieval, generation layers)
Context-aware responses using RAG
Source tracking for retrieved chunks
Config-driven settings
Extensible for production enhancements (reranking, filtering, etc.)
Project Structure
app/
  ingestion/
  retrieval/
  generation/
  db/
  main.py
  config.py
Example Use Case
Query internal documents such as:
company knowledge bases
support documentation
PDFs or text corpora
Instead of relying on general LLM knowledge, responses are grounded in your data.
Future Improvements
Persistent vector storage
Metadata filtering
Reranking layer
Streaming responses
Authentication + multi-user support
Why This Project Matters
Most “AI projects” stop at prompt engineering.
This system demonstrates:
understanding of LLM limitations
ability to design retrieval pipelines
backend system architecture
real-world AI integration
Running the Project
uvicorn app.main:app --reload
License
MIT