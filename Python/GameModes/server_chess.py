# Imports
import sys

sys.path.append('../Players')
import human as HUMAN
import ai_random as AI_RANDOM
import ai_cnn1 as AI_CNN1
import ai_mlp1 as AI_MLP1
import ai_mlp2 as AI_MLP2
import ai_mlp3 as AI_MLP3

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

class Server_Chess:

    def __init__(self):
        """
        Initialization for Chess Object
        """

        # Setup chess board
        self.chess_board = BOARD.Board()
        self.chess_board.set_standard_board()

        # Declare game over conditions
        self.is_checkmate = False
        self.is_draw = False

        # Declare players
        self.white_player = None
        self.black_player = None

        # Other
        self.white_turn = True

    def setup_game(self, white_player_id, black_player_id):
        """
        Setup players and rules for Chess Game
        """
        # Redeclare players
        if white_player_id == 0:
            self.white_player = HUMAN.Human('white')
        elif white_player_id == 1:
            self.white_player = AI_RANDOM.AI_Random('white')
        elif white_player_id == 2:
            self.white_player = AI_CNN1.AI_Cnn1('white', '../Models/cnn1_3.h5')
        elif white_player_id == 3:
            self.white_player = AI_MLP1.AI_Mlp1('white', '../Models/mlp1_1.h5')
        elif white_player_id == 4:
            self.white_player = AI_MLP2.AI_Mlp2('white', '../Models/mlp2_1.h5')
        elif white_player_id == 5:
            self.white_player = AI_MLP3.AI_Mlp3('white', '../Models/mlp3_1.h5')

        if black_player_id == 0:
            self.black_player = HUMAN.Human('black')
        elif black_player_id == 1:
            self.black_player = AI_RANDOM.AI_Random('black')
        elif black_player_id == 2:
            self.black_player = AI_CNN1.AI_Cnn1('black', '../Models/cnn1_3.h5')
        elif black_player_id == 3:
            self.black_player = AI_MLP1.AI_Mlp1('black', '../Models/mlp1_1.h5')
        elif black_player_id == 4:
            self.black_player = AI_MLP2.AI_Mlp2('black', '../Models/mlp2_1.h5')
        elif black_player_id == 5:
            self.black_player = AI_MLP3.AI_Mlp3('black', '../Models/mlp3_1.h5')

    def play_chess_move(self, color, cf1, cr1, cf2, cr2):
        """
        Game Loop for Chess Game
        :return: is_checkmate, is_draw
        """
        pass
        # if self.white_turn and color == "white":
        #     pass
        # elif not self.white_turn and color == "black":
        #     pass
        # else:
        #     print('error, not your turn')
        #
        # return valid_move, is_checkmate, is_draw



# Run Game
if __name__ == '__main__':
    pass
    # chess_game = Chess()
    # chess_game.setup_game()
    # color_that_won = chess_game.play_game(visible_board=True)
