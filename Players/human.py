import player as PLAYER

class Human(PLAYER.Player):

    def __init__(self, color):
        super().__init__(color)

    def request_move(self):
        valid = False
        while not valid:
            try:
                start = input('Enter Start Position: ')
                end = input('Enter End Position: ')
                print()
                cf1 = start[0].upper()
                cr1 = int(start[1])
                cf2 = end[0].upper()
                cr2 = int(end[1])
                return [cf1, cr1, cf2, cr2]
            except:
                # Invalid Entry
                pass

