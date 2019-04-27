import player as PLAYER
from random import randint

class AI_Random(PLAYER.Player):

    def __init__(self, color):
        super().__init__(color)

    def request_move(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cf1 = alphabet[randint(0, 7)]
        cr1 = randint(0, 7)
        cf2 = alphabet[randint(0, 7)]
        cr2 = randint(0, 7)

        return [cf1, cr1, cf2, cr2]
