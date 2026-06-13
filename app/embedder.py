from sentence_transformers import SentenceTransformer

class TextEmbedder:
    def __init__(self):
        self.model_name = "sentence-transformers/all-MiniLM-L6-v2"
        self.model = SentenceTransformer(self.model_name)

    def embed_text(self, text: str):
        embedding = self.model.encode(text)
        return embedding

# TESTING
# from sentence_transformers import util

# if __name__ == "__main__":
#     embedder = TextEmbedder()
#     text = "A person holding a small snake in their hand"
#     embedding = embedder.embed_text(text)
#     print(f"Text: {text}")
#     print(f"Embedding Shape: {embedding.shape}")
#     print(f"type of embedding: {type(embedding)}")
#     snake = embedder.embed_text("snake")
#     reptile = embedder.embed_text("reptile")
#     laptop = embedder.embed_text("laptop")
#     similarity_1 = util.cos_sim(snake, reptile)
#     similarity_2 = util.cos_sim(snake, laptop)
#     print(f"Similarity between 'snake' and 'reptile': {similarity_1.item():.4f}")
#     print(f"Similarity between 'snake' and 'laptop': {similarity_2.item():.4f}")