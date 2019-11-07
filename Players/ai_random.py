# Imports
import sys
from random import randint

import player as PLAYER

sys.path.append('../BoardStuff')
import move as MOVE

class AI_Random(PLAYER.Player):

    def __init__(self, color):
        super().__init__(color)

    def request_move(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cf1 = alphabet[randint(0, 7)]
        cr1 = randint(1, 8)
        cf2 = alphabet[randint(0, 7)]
        cr2 = randint(1, 8)

        ai_move = MOVE.Move(starting=[cf1, cr1], attacking=[cf2, cr2])

        return ai_move
