from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}

def scan_images(root_dir: str) -> list[Path]:
    images = []
    image_dir = Path(root_dir)
    for root, dirs, files in image_dir.walk():
        for file in files:
            file_path = root / file #'/' joins pathes since root is a Path object and file is a string, it overloads the + operator to create a new Path object
            if file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
                images.append(file_path)
    return images

# we can iterate using image_dir.rglob("*") to recursively find all files in the directory and its subdirectories, then check if the file extension is in the supported extensions set.
# for file_path in image_dir.rglob("*"):
#     if file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
#         images.append(file_path)

################
# TESTING
################
# if __name__ == "__main__":
#     images = scan_images("data/images")
#     print(f"Found {len(images)} images:")
#     for image in images[:5]:
#         print(image)