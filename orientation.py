from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()
pitch = sense.get_orientation_degrees()['pitch']

current_position = [4, 4]

while True:
    
    orientation = sense.get_orientation_degrees()
    new_pitch = orientation['pitch']
    diff = pitch - new_pitch
    if (abs(diff) > 30):
        if diff > 0:
            adding_value = 1
        else:
            adding_value = -1
        current_position[0] = current_position[0] + adding_value
        if current_position[0] < 0:
            current_position[0] = 0
        elif current_position[0] > 7:
            current_position[0] = 7
    sense.clear()
    sense.set_pixel(current_position[0], current_position[1], (255, 0, 0))
    pitch = new_pitch
    
    #time.sleep(0.5)
