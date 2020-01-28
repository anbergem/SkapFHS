class Piece:
    def __init__(self, symbol: str):
        if type(symbol) != str:
            raise ValueError(f"Symbol must be a string: {symbol}")
        elif len(symbol) != 1:
            raise ValueError(f"Symbol must be 1 letter: {symbol}")
        self.symbol = symbol

    def __str__(self) -> str:
        """Magic method for print(some_piece) and str(some_piece)"""
        return self.symbol

    def __eq__(self, other) -> bool:
        """Magic method for checking equality (==)"""
        return self.symbol == other.symbol

    # A static method is one that does not use "self"
    # Therefore, it does not need an instance to be used.
    # We can therefore say Piece.EMPTY(), and we will get an
    # empty piece. We can not say for example Board.play().
    # This is because Board is a class, not an object. We can,
    # however, say Board().play(). Board() creates an object,
    # and we call play on that object.
    @staticmethod
    def EMPTY() -> 'Piece':
        """Represents and empty piece"""
        return Piece(" ")

class Player:
    def __init__(self, piece: Piece):
        self.piece = piece


class Board:
    def __init__(self):
        # Update these pieces, to update the board! self._pieces[row][column] = some_piece
        self._pieces = [
            [Piece.EMPTY(), Piece.EMPTY(), Piece.EMPTY()],
            [Piece.EMPTY(), Piece.EMPTY(), Piece.EMPTY()],
            [Piece.EMPTY(), Piece.EMPTY(), Piece.EMPTY()],
        ]

    def __str__(self):
        str = "\n" * 5
        str +=  "-------------"
        for row in self._pieces:
            # Even though _print_row is static, we can call it from inside the object.
            # Not the other way around. Both self._print_row and Board._print_row is allowed.
            str += self._print_row(row[0], row[1], row[2])

        return str

    @staticmethod
    def _print_row(first, second, third):
        str = "\n"
        str += f"| {first} | {second} | {third} |\n"
        str += "-------------"

        return str

    def update(self, row: int, column: int, piece: Piece):
        self._pieces[row][column] = piece

    def get_winner(self):
        return None

    def is_valid_input(self, row, column):
        if (0 < row < 3) and (0 < column < 3) and self._pieces[row][column] != Piece.EMPTY(): # Check boundaries
            return True
        return False

class Game:
    def __init__(self, board: Board, player_one: Player, player_two: Player):
        self.board = board
        self.player_one = player_one
        self.player_two = player_two
        self.player_ones_turn = True

    def play(self):
        finished = False
        while not finished:
            print(self.board)
            if self.player_ones_turn:
                current_player = self.player_one
            else:
                current_player = self.player_two
            row, column = self.ask_for_input(current_player)
            self.board.update(row, column, current_player.piece)
            winner = self.board.get_winner()
            if winner is not None:
                self.celebrate_victory(winner)
                finished = True

            self.player_ones_turn = not self.player_ones_turn

    def ask_for_input(self, player: Player):
        while True:
            string = input(f"{player}'s turn (row column): ")
            try:
                row, column = string.strip().split(' ')
                row, column = int(row), int(column)

                if self.board.is_valid_input(row, column):
                    return row, column
            except:
                # IF PROGRAM CRASHES
                print("Invalid input. Please enter a row and column separated by space.")

    def celebrate_victory(self, winner):
        return


"""
This block is used when you want to execute some code in this file. For example if we 
were to import this file into another file, using 
>>> from tictactoe import Game
If we did not have the following block, the two lines would be run, even though we were
saying 
$ python some_other_file.py
We do not want that! We only want to run these lines, when we are executing THIS file, that is
$ python tictactoe.py
In all other cases, we don't want to run the following lines. 
"""
if __name__ == '__main__':
    cross = Piece('X')
    circle = Piece('O')
    game = Game(Board(), Player(cross), Player(circle))
    game.play()