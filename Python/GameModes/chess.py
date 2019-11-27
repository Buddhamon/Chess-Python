# Imports
import sys

sys.path.append('../Players')
import human as HUMAN
import ai_random as AI_RANDOM
import ai_algo1 as AI_ALGO1
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

class Chess:

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

    def setup_game(self):
        """
        Setup players and rules for Chess Game
        """
        # Redeclare players
        # self.white_player = HUMAN.Human('white')
        # self.white_player = AI_RANDOM.AI_Random('white')
        self.white_player = AI_ALGO1.AI_Algo1('white')
        # self.white_player = AI_CNN1.AI_Cnn1('white', '../Models/cnn3.h5')
        # self.white_player = AI_MLP1.AI_Mlp1('white', '../Models/mlp1_1.h5')
        # self.white_player = AI_MLP2.AI_Mlp2('white', '../Models/mlp2_1.h5')
        # self.white_player = AI_MLP3.AI_Mlp3('white', '../Models/mlp3_1.h5')
        # self.black_player = HUMAN.Human('black')
        self.black_player = AI_RANDOM.AI_Random('black')
        # self.black_player = AI_ALGO1.AI_Algo1('black')
        # self.black_player = AI_CNN1.AI_Cnn1('black', '../Models/cnn3.h5')
        # self.black_player = AI_MLP1.AI_Mlp1('black', '../Models/mlp1_2.h5')
        # self.black_player = AI_MLP2.AI_Mlp2('black', '../Models/mlp2_1.h5')
        # self.black_player = AI_MLP3.AI_Mlp3('black', '../Models/mlp3_2.h5')

    def play_game(self, visible_board=True):
        """
        Game Loop for Chess Game
        :return: is_checkmate, is_draw
        """
        if visible_board:
            self.chess_board.print_board()
        while not self.is_checkmate and not self.is_draw:

            valid = False
            while not valid:
                # Request move from player
                if self.white_turn:
                    cf1, cr1, cf2, cr2 = self.white_player.request_move(self.chess_board)
                    valid = self.chess_board.move_piece(self.white_player.color, cf1, cr1, cf2, cr2)
                else:
                    cf1, cr1, cf2, cr2 = self.black_player.request_move(self.chess_board)
                    valid = self.chess_board.move_piece(self.black_player.color, cf1, cr1, cf2, cr2)

            # After valid move change player's turn and check for game over condition
            if self.white_turn:
                self.white_turn = False
                self.is_checkmate = self.chess_board.is_checkmate("black")
                if not self.is_checkmate:
                    self.is_draw = self.chess_board.is_draw("black")
            else:
                self.white_turn = True
                self.is_checkmate = self.chess_board.is_checkmate("white")
                if not self.is_checkmate:
                    self.is_draw = self.chess_board.is_draw("white")

            if visible_board:
                self.chess_board.print_board()

        color_that_won = ''
        if self.is_checkmate:
            if self.white_turn:
                color_that_won = 'black'
                print("Black Wins")
            else:
                color_that_won = 'white'
                print("White Wins")
        else:
            print("Draw")

        return color_that_won



# Run Game
if __name__ == '__main__':

    # Input Parameters to Chess Main
    number_of_games = 1
    visible_board = True

    # Execute the rest of Chess Main
    white_wins = 0
    black_wins = 0
    draws = 0

    for i in range(number_of_games):
        print('Game', i+1)
        chess_game = Chess()
        chess_game.setup_game()
        color_that_won = chess_game.play_game(visible_board=visible_board)
        if color_that_won == 'white':
            white_wins += 1
        elif color_that_won == 'black':
            black_wins += 1
        else:
            draws += 1

    print('Number of White Wins:', white_wins)
    print('Number of Black Wins:', black_wins)
    print('Number of Draws:', draws)
