from sense_hat import SenseHat
import time

sense = SenseHat()
sense.low_light = True

starting_value = 50
color = [starting_value]*3
adding_value = (255 - starting_value) / 64
sense.clear()

while True:
    for i in range(3):    
        for y in range(8):
            for x in range(8):
                #sense.set_pixel(x, y, 255*y/7, 0, 255*x/7)
                color[i] = int(color[i] + adding_value)
                #color[1] = int(color[1] + multiplicator)
                #color[2] = int(color[2] + multiplicator)
                sense.set_pixel(x, y, color)
                print(y, x)
                time.sleep(0.1)
        color[i] = starting_value
        #sense.clear()
    
    
    
    
    
