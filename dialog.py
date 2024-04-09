import time
import keyboard

class Dialog:
    def __init__(self, *text):
        self.text = text

    def is_running(self) -> bool:
        return self.is_running


    def print(self):
        for te_xt in self.text:
            self.text_buffer = ""
            self.skip = False
            self.is_running = False
            for x in te_xt:
                if keyboard.is_pressed("space"):
                    self.skip = True
                self.is_running = True
                self.text_buffer += x
                if self.skip:
                    break
                print("\r" + self.text_buffer, end="")
                time.sleep(0.05)

            print("\r" + te_xt, end="")

            self.is_running = False
            print()
            if self.skip:
                time.sleep(0.05)
            else:
                time.sleep(0.05)