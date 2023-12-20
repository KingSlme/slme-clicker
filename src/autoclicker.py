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
        self.validCPS = True
        self.initialize_autoclicker()

    def initialize_autoclicker(self):
        listener = Listener(on_press=self.on_key_press)
        listener.start()

    def on_key_press(self, key):
        if key is not None and key == self.toggle_key and self.validCPS:
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
        if self.enabled and self.validCPS:
            pyautogui.click()
            pyautogui.PAUSE = self.delay
        root.after(1, self.autoclick, root)

    def check_valid_CPS(self):
        if self.cps >= 1:
            self.validCPS = True
        else:
            self.validCPS = False

    def set_varied_delay(self):
        if self.cps == 0 and self.variance == 0:
            random_float = 1
        elif self.cps - self.variance < 1:
            if 1 /(self.cps + self.variance) > 1:
                random_float = random.uniform(1, 1 / (self.cps + self.variance))
            else:
                random_float = 1
        else:
            random_float = random.uniform(1 / (self.cps - self.variance), 1 / (self.cps + self.variance))
        self.delay = random_float
        
    
    def set_varied_delay_loop(self, root):
        self.set_varied_delay()
        root.after(2000, self.set_varied_delay_loop, root)