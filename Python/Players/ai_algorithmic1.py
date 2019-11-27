# Imports
import sys
import random
import player as PLAYER

class AI_Random(PLAYER.Player):

    def __init__(self, color):
        """
        Initialization for Random AI Object
        """
        super().__init__(color)

    def request_move(self, board):
        """
        Asks the AI what move to make, AI submits possible move to Chess game
        :return: a starting location and ending location for chess move
        """

        best_start_coordinate, best_end_coordinate = self.get_best_move(board)
        cf1, cr1 = board._convert_to_chess_coordinates(best_start_coordinate[0], best_start_coordinate[1])
        cf2, cr2 = board._convert_to_chess_coordinates(best_end_coordinate[0], best_end_coordinate[1])

        return cf1, cr1, cf2, cr2

    def get_best_move(self, board):
        pass
