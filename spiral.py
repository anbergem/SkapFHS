from sense_hat import SenseHat
import time

from joystick import random_color

sense = SenseHat()
sense.clear()

position = [3, 4]
increment = 1
rotation_list = ['UP', 'RIGHT', 'DOWN', 'LEFT']
counter = 0
sense.set_pixel(position[0], position[1], (255, 0, 0))

color = random_color()

while True:
    for i in range(2):
        # Change direction
        rotation = rotation_list[counter % len(rotation_list)]
        counter += 1
        
        #if counter % 2 == 0:
        color = random_color()
        
        # Move
        for _ in range(increment):
            if rotation == "UP":
                position[1] -= 1
            elif rotation == "DOWN":
                position[1] += 1
            elif rotation == "LEFT":
                position[0] -= 1
            elif rotation == "RIGHT":
                position[0] += 1
            
            if position == [7, 8]:
                break
                
            
            sense.set_pixel(position[0], position[1], color)            
            time.sleep(0.01)
        
        if position == [7, 8]:
            position = [3, 4]
            increment = 0
            counter = 0
            color = random_color()
            sense.set_pixel(position[0], position[1], color)
            break

    increment += 1
    