import pyautogui
from pynput.keyboard import KeyCode, Listener
import random

class Autoclicker:
    def __init__(self):
        self.cps = 10.0
        self.variance = 2.5
        self.delay = None
        self.toggle_key = None
        self.enabled = False
        self.initialize_autoclicker()

    def initialize_autoclicker(self):
        listener = Listener(on_press=self.on_key_press)
        listener.start()

    def on_key_press(self, key):
        if key is not None and key == self.toggle_key:
            self.enabled = not self.enabled

    def set_cps(self, value):
        self.cps = value

    def set_variance(self, value):
        self.variance = value

    def set_toggle_key(self, value):
        if value == "":
            self.toggle_key = None
        else:
            self.toggle_key = KeyCode.from_char(value)

    def autoclick(self, root):
        if self.enabled:
            pyautogui.click()
            pyautogui.PAUSE = self.delay
        root.after(1, self.autoclick, root)
        
    
    def set_varied_delay(self, root):
        random_float = random.uniform((1 / (self.cps - self.variance)), (1 / (self.cps + self.variance)))
        self.delay = max(0.01, random_float)
        root.after(2000, self.set_varied_delay, root)