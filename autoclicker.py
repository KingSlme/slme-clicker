import pyautogui
from pynput.keyboard import KeyCode, Listener

class Autoclicker:
    def __init__(self):
        self.cps = 10.0
        self.variance = 5.0
        self.toggle_key = None
        self.enabled = False
        self.initialize_autoclicker()

    def initialize_autoclicker(self):
        listener = Listener(on_press=self.on_key_press)
        listener.start()

    def on_key_press(self, key):
        if key is not None and key == self.toggle_key:
            self.enabled = not self.enabled

    def set_toggle_key(self, value):
        if value == "":
            self.toggle_key = None
        else:
            self.toggle_key = KeyCode.from_char(value)

    def set_cps(self, value):
        self.cps = value

    def set_variance(self, value):
        self.variance = value

    def autoclick(self, root):
        if self.enabled:
            pyautogui.click()
            pyautogui.PAUSE = 1 / self.cps
        root.after(1, self.autoclick, root)
    