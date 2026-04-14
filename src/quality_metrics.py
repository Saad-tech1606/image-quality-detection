import cv2
import numpy as np

def detect_blur(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def brightness_contrast(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    contrast = np.std(gray)
    return brightness, contrast

def quality_score(blur, brightness, contrast):
    score = (0.5 * blur) + (0.25 * brightness) + (0.25 * contrast)
    return score