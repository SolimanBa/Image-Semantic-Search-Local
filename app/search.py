from app.vector_store import VectorStore
from app.embedder import TextEmbedder

class ImageSearch:
    def __init__(self):
        self.vector_store = VectorStore()
        self.embedder = TextEmbedder()
    
    def execute(self, query, top_k: int = 5):
        query_embedding = self.embedder.embed_text(query)
        result =  self.vector_store.search_similar_images(query_embedding, top_k=top_k)
        cleaned_results = []
        for img_id, caption, metadata, distance  in zip(result["ids"][0], result["documents"][0], result["metadatas"][0], result["distances"][0]):
            cleaned_results.append({
                "image_path": metadata["path"],
                "caption": caption,
                "distance": distance
            })
        return cleaned_results
    
# TESTING
# if __name__ == "__main__":
#     from app.embedder import TextEmbedder
#     embedder = TextEmbedder()
#     searcher = ImageSearch()
#     query = "human holding a snake"
#     results = searcher.execute(query, top_k=5)
#     print(f"Query: {query}")
#     print("Results:")
#     for result in results:
#         print(f"Image Path: {result['image_path']}, Caption: {result['caption']}, Distance: {result['distance']}")