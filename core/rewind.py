import pyautogui
import time
from focusVLC import focusVLC

focusVLC()
pyautogui.keyDown("ctrl")
pyautogui.keyDown("alt")
pyautogui.press("left")
pyautogui.keyUp("alt")
pyautogui.keyUp("ctrl")
