from sense_hat import SenseHat
from sensegame import Joystick
import random


def random_color():
    new_color = [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)]
    index = random.randint(0, 2)
    new_color[index] -= 100
    return new_color

def hello(arg):
    global color
    if arg == "UP":
        new_value = position[1] - 1
        if new_value < 0:
            new_value = 7
            color = random_color()
        position[1] = new_value
    elif arg == "DOWN":
        new_value = position[1] + 1
        if new_value > 7:
            new_value = 0
            color = random_color()
        position[1] = new_value
    elif arg == "LEFT":
        new_value = position[0] - 1
        if new_value < 0:
            new_value = 7
            color = random_color()
        position[0] = new_value
    elif arg == "RIGHT":
        new_value = position[0] + 1
        if new_value > 7:
            new_value = 0
            color = random_color()
        position[0] = new_value
    elif arg == "CENTER":
        pass
    
    #sense.set_pixel(position[0], position[1], color)
    old_color = sense.get_pixel(*position)
    if not old_color == [0, 0, 0]:
        color = [
            int((old_color[0] + color[0])/2),
            int((old_color[1] + color[1])/2),
            int((old_color[2] + color[2])/2)
        ]
    sense.set_pixel(*position, color)

if __name__ == '__main__':
    sense = SenseHat()
    sense.clear()
    joystick = Joystick()

    # (x, y)
    position = [4, 4]
    color = (255, 0, 0)
        
    joystick.register_key_press_callback(hello)

    while True:
        pass
