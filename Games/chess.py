# Imports
import sys

sys.path.append('../Players')
import human as HUMAN
import ai_random as AI_RANDOM

sys.path.append('../BoardStuff')
import board as BOARD
import square as SQUARE

sys.path.append('../Pieces')
import piece as PIECE
import pawn as PAWN
import rook as ROOK
import knight as KNIGHT
import bishop as BISHOP
import queen as QUEEN
import king as KING

class Chess:

    def __init__(self):
        """Initialization for Chess Object"""

        # Setup chess board
        self.chess_board = BOARD.Board()
        self.chess_board.set_standard_board()

        # Declare win conditions
        self.check = False
        self.checkmate = False
        self.stalemate = False
        self.fifty_move_draw = False
        self.insufficient_material = False

        # Declare players
        self.white_player = None
        self.black_player = None

        # Other
        self.white_turn = True

    def setup_game(self):
        """Setup players and rules for Chess Game"""
        # Redeclare players
        self.white_player = AI_RANDOM.AI_Random('white')
        self.black_player = AI_RANDOM.AI_Random('black')

    def begin_game(self):
        """Game Loop for Chess Game"""

        move_count = 1
        self.chess_board.print_board()
        while not self.checkmate:

            valid = False
            while not valid:
                # Request move from player
                if self.white_turn:
                    move = self.white_player.request_move()
                    valid = self.chess_board.make_move(self.white_player.color, move)
                else:
                    move = self.black_player.request_move()
                    valid = self.chess_board.make_move(self.black_player.color, move)

            # After valid move change player's turn
            if self.white_turn:
                self.white_turn = False
            else:
                self.white_turn = True

            self.chess_board.print_board(move_count)
            move_count += 1

        # Return winner

# Run Game
if __name__ == '__main__':
    chess_game = Chess()
    chess_game.setup_game()
    chess_game.begin_game()
