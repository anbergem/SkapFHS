from typing import Optional


class Piece:
    def __init__(self, symbol):
        if len(symbol) != 1:
            raise ValueError(f"Invalid input. Only a symbol of one character is allowed: {len(symbol)}")
        self.symbol = symbol

    def __str__(self):
        """Magic method for print(some_piece) and str(some_piece)"""
        return self.symbol

    def __eq__(self, other):
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
    def EMPTY():
        """Represents and empty piece"""
        return Piece(" ")

class Player:
    def __init__(self, piece: Piece, name: str = None):
        self.piece = piece
        self.name = name

    def __str__(self):
        """Prints either the name, if present, or the symbol"""

        return self.name if self.name is not None else self.piece.symbol


class Board:
    win_conditions = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
    )
    def __init__(self):
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

    def is_taken(self, row, column) -> bool:
        return self._pieces[row][column] != Piece.EMPTY()
    
    def get_piece(self, row, column) -> Piece:
        return self._pieces[row][column]

    def winner(self) -> Optional[Piece]:
        for win_condition in self.win_conditions:
            three_pieces = [self._pieces[row][column] for row, column in win_condition]
            first_piece = three_pieces[0]
            if first_piece != Piece.EMPTY() and three_pieces.count(first_piece) == len(three_pieces):
                return first_piece
        return None
    
    def is_tie(self) -> bool:
        for row in self._pieces:
            for piece in row:
                if piece == Piece.EMPTY():
                    return False
        return True

    def update(self, row: int, column: int, piece: Piece):
        self._pieces[row][column] = piece



class Game:
    def __init__(self, board: Board, player_one: Player, player_two: Player):
        self._board = board
        self._current_player = player_one
        self._next_player = player_two

    def play(self):
        while True:
            print(self._board)
            row, column = self._ask_for_input(self._current_player)
            self._board.update(row, column, self._current_player.piece)
            if (self._check_for_victory()):
                return
            self._current_player, self._next_player = self._next_player, self._current_player

    def _ask_for_input(self, player: Player):
        while True:
            try:
                place = input(f"{player}'s turn (row column): ")
                row, column = map(int, place.strip().split(' '))
                if not self._board.is_taken(row, column):
                    return row, column
            except Exception as e:
                print("Invalid input ... ", e)

    def _get_player(self, piece: Piece):
        if self._current_player.piece == piece:
            return self._current_player
        elif self._next_player == piece:
            return self._next_player
        raise ValueError(f'No player with the piece: {piece}')

    def _check_for_victory(self) -> bool:
        winner_piece = self._board.winner()
        if winner_piece is not None:
            winner = self._get_player(winner_piece)
            print(self._board)
            print(f'Congratulations, {winner}!')
            return True
        return False

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
    cross = Piece("X")
    circle = Piece("O")
    game = Game(Board(), Player(cross), Player(circle))
    game.play()