import faiss
import numpy as np
import os
import pickle

class VectorStore:
    def __init__(self, dim: int = 1536, index_path ="faiss.index", meta_path="meta.pkl"):
        self.dim = dim
        self.index_path = index_path
        self.meta_path = meta_path

        if os.path.exists(index_path) and os.path.exists(meta_path):
            self.load()
        else:
            self,index = faiss.IndexFlatL2(dim)
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

        for i, dist in zip(indices[0], distances[0]):
            results.append({
                "text": self.texts[i],
                "source": self.sources[i],
                "score": float(dist)
            })

        return results
    

    def save(self):
        faiss.write_index(self.index, self.index_path)

        with open(self.meta_path, "wb") as f:
            pickle.dump({
                "texts": self.texts,
                "sources": self.sources
            }, f)

    
    def load(self):
        self.index = faiss.read_index(self.index_path)

        with open(self.meta_path, "rb") as f:
            data = pickle.load(f)
            self.texts = data["texts"]
            self.sources = data["sources"]