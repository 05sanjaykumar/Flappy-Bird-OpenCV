import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab, ImageDraw
import time

# Configuration
GAME_REGION = (100, 100, 800, 600)  # (x, y, width, height)
DETECTION_COLOR_LOWER = np.array([16, 195, 239])
DETECTION_COLOR_UPPER = np.array([20, 255, 255])
REFRESH_RATE = 0.1  # seconds

def draw_overlay(draw, x, y, w, h):
    """Draw rectangle on PIL Image"""
    draw.rectangle([(x, y), (x+w, y+h)], outline="green", width=2)

def show_overlay(image):
    """Temporary display method - will replace with proper overlay"""
    cv2.imshow('Overlay Preview', cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))
    cv2.waitKey(1)

try:
    while True:
        # Capture screen
        screenshot = ImageGrab.grab(bbox=GAME_REGION)
        frame = np.array(screenshot)
        hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        
        # Detection
        mask = cv2.inRange(hsv, DETECTION_COLOR_LOWER, DETECTION_COLOR_UPPER)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Create overlay
        overlay = screenshot.copy()
        draw = ImageDraw.Draw(overlay)
        
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if w > 20 and h > 20:  # Filter small detections
                draw_overlay(draw, x, y, w, h)
        
        # Temporary display (replace this with real overlay)
        show_overlay(overlay)
        
        time.sleep(REFRESH_RATE)

except KeyboardInterrupt:
    cv2.destroyAllWindows()