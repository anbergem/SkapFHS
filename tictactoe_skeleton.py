class Piece:
    def __init__(self, symbol: str):
        # TODO: Don't allow symbols of more than one character
        self.symbol = symbol

    def __str__(self) -> str:
        """Magic method for print(some_piece) and str(some_piece)"""
        return self.symbol

    def __eq__(self, other) -> bool:
        """Magic method for checking equality (==)"""
        pass # TODO

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
    pass # TODO


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

    # TODO: More methods



class Game:
    def __init__(self, board: Board, player_one: Player, player_two: Player):
        self.board = board
        pass # Todo

    def play(self):
        print(self.board)
        # TODO

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
    game = Game(Board(), Player(), Player())
    game.play()