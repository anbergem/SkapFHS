from sense_hat import SenseHat
from sensegame import Joystick
import time
import random


class ReactionGame:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()
        self.counter = 0
        self.waiting = False
        self.idle = True
        self.joystick = Joystick()
        self.joystick.register_key_press_callback(self._click)
        
    def play(self):
        while True:
            if self.idle:
                time.sleep(random.randint(1, 100) / 50)
                self.sense.set_pixel(3, 4, 255, 255, 255)
                self.counter = time.perf_counter()
                self.waiting = True
                self.idle = False
            time.sleep(1)                
            
    def _click(self, button):
        if (self.waiting):
            reaction_time = (time.perf_counter() - self.counter)
            self.sense.show_message(f'{reaction_time:.2f}')
            self.waiting = False
            self.idle = True
            

if __name__ == "__main__":
    game = ReactionGame()
    game.play()
