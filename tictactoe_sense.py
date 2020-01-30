from sense_emu import SenseHat
from sensegame import Joystick

from tictactoe import Piece, Player, Board

class Game:
    def __init__(self, board, player_one, player_two):
        self.sense = SenseHat()
        self.joystick = Joystick()
        self.joystick.register_key_press_callback(self.on_key_pressed)
        self.current_position = [1, 1]
        
    def play(self):
        self.draw_board()
        
    def draw_board(self):
        for i in range(2, 8, 3):
            for j in range(8):
                self.sense.set_pixel(i, j, (255, 255, 0))
                self.sense.set_pixel(j, i, (255, 255, 0))

    def on_key_pressed(self, key):
        if 

if __name__ == '__main__': 
    game = Game(Board(), Player(Piece('X')), Player(Piece('O')))
    game.play()