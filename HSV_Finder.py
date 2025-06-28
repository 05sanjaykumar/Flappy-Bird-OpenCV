import cv2
import numpy as np
import pyautogui
from pynput import mouse
import sys

def on_click(x, y, button, pressed):
    if pressed:
        try:
            # Convert coordinates to integers
            x, y = int(x), int(y)
            
            # Capture the screen
            screenshot = pyautogui.screenshot()
            
            # Convert to numpy array and then to BGR for OpenCV
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Get the pixel color at clicked position
            bgr_color = frame[y, x]
            
            # Convert BGR to HSV
            hsv_color = cv2.cvtColor(np.uint8([[bgr_color]]), cv2.COLOR_BGR2HSV)[0][0]
            
            print(f"Clicked at position: ({x}, {y})")
            print(f"BGR color: {bgr_color}")
            print(f"HSV color: {hsv_color}")
            print("-" * 30)
            
        except Exception as e:
            print(f"Error: {e}")
            print("Make sure the app has accessibility permissions")
            print("-" * 30)

def main():
    print("HSV Color Finder - Click anywhere on your screen")
    print("Press Ctrl+C in the terminal to exit")
    print("-" * 30)
    
    try:
        # Start listening for mouse clicks
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()