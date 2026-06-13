from app.vector_store import VectorStore

class ImageSearch:
    def __init__(self):
        self.vector_store = VectorStore()
    
    def execute(self, query_embedding, top_k: int = 5):
        result =  self.vector_store.search_similar_images(query_embedding, top_k=top_k)
        cleaned_results = []
        for img_id, caption, metadata in zip(result["ids"][0], result["documents"][0], result["metadatas"][0]):
            cleaned_results.append({
                "image_path": metadata["path"],
                "caption": caption
            })
        return cleaned_results