from sense_hat import SenseHat
from sensegame import Joystick
import time
import random
import symbols
from joystick import random_color

choices = {
    "RIGHT": symbols.right_arrow,
    "LEFT": symbols.left_arrow,
    "DOWN": symbols.down_arrow,
    "UP": symbols.up_arrow,
    "CENTER": symbols.circle
}
keys = list(choices.keys())

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
                self.key = keys[random.randint(0, 4)]
                self.color = random_color()
                self.sense.set_pixels(choices[self.key](self.color))
                self.counter = time.perf_counter()
                self.waiting = True
                self.idle = False
            time.sleep(1)                
            
    def _click(self, button):
        if (self.waiting and self.key == button):
            reaction_time = (time.perf_counter() - self.counter)
            if reaction_time > 59:
                text = f"{reaction_time//60:.0f}:{reaction_time%60:.2f}"
            else:
                text = f'{reaction_time:.2f}'
            self.sense.show_message(text, text_colour=self.color)
            self.waiting = False
            self.idle = True
            

if __name__ == "__main__":
    game = ReactionGame()
    game.play()
