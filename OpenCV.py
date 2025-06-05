import cv2
import numpy as np
import mss

# Define the region of the screen where the game is running
# You can adjust these numbers to match your game window
monitor = {"top": 100, "left": 100, "width": 400, "height": 600}

with mss.mss() as sct:
    while True:
        # Capture screen
        screenshot = sct.grab(monitor)
        
        # Convert raw pixels to numpy array for OpenCV
        img = np.array(screenshot)

        # Optional: Convert BGRA to BGR
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        # Show the live game feed
        cv2.imshow("Live Game View", img)

        # Press 'q' to quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
