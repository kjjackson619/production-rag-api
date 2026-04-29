from app.db.vector_store import VectorStore
from app.config import settings

class Retriever:
    def __int__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    
    def retrieve(self, query_vector):
        results = self.vector_store.search(
            query_vector,
            k=settings.TOP_K
        )

        return results