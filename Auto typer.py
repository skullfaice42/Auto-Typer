# has to install 'pip install pyautogui keyboard' before anything

import time
import keyboard
import pyautogui

def type_text(text):
    for char in text:
        if keyboard.is_pressed('ctrl+alt+s'):
            print("Typing terminated.")
            break
        pyautogui.typewrite(char)
        time.sleep(0.000000000001)  # 10ms delay

def main():
    text = input("What text would you like me to type? ")
    
    print("Press Ctrl + Alt + P to start typing and Ctrl + Alt + S to stop.")
    
    while True:
        if keyboard.is_pressed('ctrl+alt+p'):
            print("Typing started...")
            type_text(text)
            print("Typing completed or terminated.")
            break
        time.sleep(0.1)

if __name__ == "__main__":
    main()