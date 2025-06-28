import cv2
import numpy as np
import mss
import pyautogui
import time

# Define screen region of your game
MONITOR = {"top": 100, "left": 100, "width": 800, "height": 600}

# Bird HSV color range (your yellow bird)
BIRD_COLOR_LOWER = np.array([16, 195, 239])
BIRD_COLOR_UPPER = np.array([20, 255, 255])

# Pipe HSV range (adjust based on your pipes)
PIPE_COLOR_LOWER = np.array([50, 100, 100])
PIPE_COLOR_UPPER = np.array([90, 255, 255])

# Area thresholds
MIN_BIRD_AREA = 50
MIN_PIPE_AREA = 100

# Delay before bot starts
print("[INFO] Bot will start in 3 seconds. Switch to the game window.")
time.sleep(3)

def detect_bird(hsv):
    mask = cv2.inRange(hsv, BIRD_COLOR_LOWER, BIRD_COLOR_UPPER)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest) > MIN_BIRD_AREA:
            return cv2.boundingRect(largest)
    return None

def detect_pipes(hsv):
    mask = cv2.inRange(hsv, PIPE_COLOR_LOWER, PIPE_COLOR_UPPER)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    pipes = []
    for cnt in contours:
        if cv2.contourArea(cnt) > MIN_PIPE_AREA:
            pipes.append(cv2.boundingRect(cnt))
    pipes = sorted(pipes, key=lambda box: box[0])  # sort by X
    return pipes

def should_flap(bird, pipes):
    if not bird or not pipes:
        return False

    bird_x, bird_y, bw, bh = bird
    for pipe in pipes:
        pipe_x, pipe_y, pw, ph = pipe
        if pipe_x > bird_x:
            # Estimate pipe gap mid-point (adjust as needed)
            gap_y = pipe_y + ph + 45
            return bird_y > gap_y
    return False

# Start bot
with mss.mss() as sct:
    while True:
        frame = np.array(sct.grab(MONITOR))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        bird = detect_bird(hsv)
        pipes = detect_pipes(hsv)

        if should_flap(bird, pipes):
            pyautogui.press('space')

        # Optional: comment this to avoid hogging CPU
        time.sleep(0.01)

