from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

class ImageCaptioner:
    def __init__(self):
        self.model_name = "Salesforce/blip-image-captioning-base"
        self.processor = BlipProcessor.from_pretrained(self.model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(self.model_name)

    def generate_caption(self, image_path: str) ->str:
        image = Image.open(image_path)
        inputs = self.processor(image, return_tensors="pt")
        captions = self.model.generate(**inputs, max_length=50, min_length=10, num_beams=5)  
        captions = self.processor.decode(captions[0], skip_special_tokens=True)
        return str(captions)
    

# TESTING
# if __name__ == "__main__":
#     captioner = ImageCaptioner()
#     caption = captioner.generate_caption("data\\images\\IMG_20230719_101048.jpg")
#     print(f"Generated Caption: {caption}")


# The processor handles:
# Image
# ↓
# Resize
# Normalize
# Convert to tensors
# Format inputs
# ↓
# Model