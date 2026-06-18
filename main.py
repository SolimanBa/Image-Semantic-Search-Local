from app.ui import demo
from scripts.index_images import index_images

if __name__ == "__main__":
    index_images("data/images")
    demo.launch()