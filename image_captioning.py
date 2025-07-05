# Simple Image Captioning AI 
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_real_caption(image_path):
    raw_image = Image.open(image_path).convert('RGB')
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    # BOLD + BORDERS
    print("=" * 50)
    print(f"\033[1m📝 CAPTION: {caption}\033[0m")
    print("=" * 50)

# Example
generate_real_caption("car1.jpg")
