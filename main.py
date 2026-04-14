import cv2
import argparse
from src.quality_metrics import detect_blur, brightness_contrast, quality_score
from src.enhancement import sharpen, histogram_equalization
from src.model import load_resnet

# CLI Argument (industry feel)
parser = argparse.ArgumentParser()
parser.add_argument("--image", type=str, default="dataset/sample.jpg")
args = parser.parse_args()

image_path = args.image
image = cv2.imread(image_path)

if image is None:
    print("❌ Error: Image not found")
    exit()

# Metrics
blur = detect_blur(image)
brightness, contrast = brightness_contrast(image)
score = quality_score(blur, brightness, contrast)

print(f"📊 Blur: {blur:.2f}")
print(f"💡 Brightness: {brightness:.2f}, Contrast: {contrast:.2f}")
print(f"⭐ Quality Score: {score:.2f}")

# Classification
if score < 150:
    print("⚠️ Poor Quality Image → Enhancing...")
    enhanced = sharpen(image)
    enhanced = histogram_equalization(enhanced)
else:
    print("✅ Good Quality Image")
    enhanced = image

# Save output
cv2.imwrite("output.jpg", enhanced)

# Load ResNet (DL exposure)
model = load_resnet()
print("🤖 ResNet loaded for feature extraction")

print("✅ Process Complete. Check output.jpg")