import chromadb

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./data/chroma_db")
        self.collection = self.client.get_or_create_collection(name="image_captions")

    def add_image(self, image_id: str, caption: str, embedding: list, metadata=None):
        self.collection.add(
            ids=[image_id],
            documents=[caption],
            embeddings=[embedding],
            metadatas=[metadata]
        )
    
    def search_similar_images(self, query_embedding, top_k: int = 5):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results