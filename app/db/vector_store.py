import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int = 1536):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []
        self.sources = []

    def add(self, embeddings: list):
        vectors = np.array(
            [e["embedding"] for e in embeddings]
        ).astype("float32")

        self.index.add(vectors)

        for e in embeddings:
            self.texts.append(e["text"])
            self.sources.append(e["source"])

    def search(self, query_vector, k=5):
        query_vector = np.array([query_vector]).astype("float32")

        distances, indices = self.index.search(query_vector, k)

        results = []

        for i in indices[0]:
            results.append({
                "text": self.texts[i],
                "source": self.sources[i]
            })

        return results
