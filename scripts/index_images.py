from app.captioner import ImageCaptioner
from app.scanner import scan_images
from app.embedder import TextEmbedder
from app.vector_store import VectorStore
import json

captioner = ImageCaptioner()
embedder = TextEmbedder()
vector_store = VectorStore()

def index_images(root_dir: str):
    images = scan_images(root_dir)
    print(f"Found {len(images)} images. Indexing...")
    success_count = 0
    fail_count = 0
    existing_ids = set(vector_store.collection.get()["ids"])
    for idx, image_path in enumerate(images, start=1):
        if str(image_path) in existing_ids:
            print(f"Image {image_path} already indexed. Skipping.")
            continue
        try:
            print(f"[{idx}/{len(images)}] {image_path}")
            caption = captioner.generate_caption(str(image_path))
            #save caption to captions/captions.jsonl
            with open("data/captions/captions.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps({"image_path": str(image_path), "caption": caption}) + "\n")
            embedding = embedder.embed_text(caption)
            img_id = str(image_path)
            vector_store.add_image(image_id=img_id, caption=caption, embedding=embedding, metadata={"path": str(image_path)})
            success_count += 1
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            fail_count += 1
    print(f"Indexing complete.\n Total Images:{len(images)}\nSuccess: {success_count}\nFail: {fail_count}")

if __name__ == "__main__":
    index_images("data/images")