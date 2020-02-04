from sense_hat import SenseHat
from sensegame import Joystick
import time

from tictactoe import Piece, Player, Board

loop_time_seconds = 0.2
border_color = (255, 255, 0)
error_color = (255, 0, 0)

class Game:
    def __init__(self, board, player_one, player_two):
        self.board = board
        
        self.sense = SenseHat()
        self.joystick = Joystick()
        self.joystick.register_key_press_callback(self.on_key_pressed)
        # Use (x, y) coordinates
        self.current_position = [1, 1]
        self.taken = {}
        self.current_player = player_one
        self.next_player = player_two
        
    def play(self):
        self.sense.clear()
        while True:
            self.draw_board()
            time.sleep(loop_time_seconds)
            
            winner = self.board.winner()
            if winner is not None:
                break
            
        self.sense.show_message(f"Winner: ")
        self.sense.show_message(str(self.next_player.piece), text_colour=self.next_player.color)

    def _iter_cells(self):
        for y in range(3):
            for x in range(3):
                yield (x, y)
        
    def _get_cell_color(self, cell):
        if (cell == tuple(self.current_position)):
            return tuple(self.current_player.color)
        elif (cell in self.taken):
            return self.taken[cell]
        else:
            return (0, 0, 0)
        
        
    def draw_board(self):
        cells = [self._get_cell_color(cell) for cell in self._iter_cells()] 
        self.sense.set_pixels(cells)

    def on_key_pressed(self, key):
        if key == "UP":
            self.current_position[1] = self.current_position[1]-1 if self.current_position[1]-1 > 0 else 0
        elif key == "DOWN":
            self.current_position[1] = self.current_position[1]+1 if self.current_position[1]+1 < 3 else 3
        elif key == "LEFT":
            self.current_position[0] = self.current_position[0]-1 if self.current_position[0]-1 > 0 else 0
        elif key == "RIGHT":
            self.current_position[0] = self.current_position[0]+1 if self.current_position[0]+1 < 3 else 3
        elif key == "CENTER":
            self.select_square()
            
    def select_square(self):
        if self.board.is_taken(*self.current_position):
            self.board.update(*self.current_position, self.current_player.piece)
            self.current_player, self.next_player = self.next_player, self.current_player
        else:
            self.sense.set_pixel(*self.current_position, error_color)

class SensePlayer(Player):
    def __init__(self, piece, color):
        super().__init__(piece)
        self.color = color

if __name__ == '__main__':
    player_one_color = (0, 255, 0)
    player_two_color = (0, 0, 255)
    game = Game(Board(), SensePlayer(Piece('X'), player_one_color), SensePlayer(Piece('O'), player_two_color))
    game.play()
   
  
  
   
  
  
  
  
 
 
  
  