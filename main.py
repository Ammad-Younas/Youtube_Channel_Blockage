import pyautogui
import keyboard
import time
import cv2
import numpy as np
import os

TARGET_FOLDER = "_internal/TARGETS"
CHECK_INTERVAL = 1
THRESHOLD = 0.8

def load_target_images_from_folder(folder):
    supported_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp")
    loaded = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(supported_extensions):
            path = os.path.join(folder, filename)
            img = cv2.imread(path)
            if img is not None:
                loaded.append((path, img))
            else:
                print("Failed to load image")
    return loaded

def find_and_press_if_match(targets):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    for path, target in targets:
        result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val >= THRESHOLD:
            print(f"Closing TAB...")
            keyboard.press_and_release("ctrl+w")
            return True

    return False

if __name__ == "__main__":
    print("Tracking started. Checking every 1 second...")
    targets = load_target_images_from_folder(TARGET_FOLDER)
    if not targets:
        print("No valid target images found. Exiting.")
        exit(1)

    while True:
        find_and_press_if_match(targets)
        time.sleep(CHECK_INTERVAL)
