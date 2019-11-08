class Piece():

    # Define Default Class Variables
    def __init__(self):
        self.color = 'null'
        self.name = 'null piece'
        self.symbol = '  '
        self.value = 0
        self.requires_board_state = False
        self.turn_last_moved = 0


        # Define Class Variables
    def declare_variables(self, color, name, symbol_char, value, rbs):
        self.color = color
        self.name = name
        if color == 'black':
            self.symbol = 'b'+symbol_char
        elif color == 'white':
            self.symbol = 'w'+symbol_char
        else:
            print('Color is not known')
            0/0 # Error Terminates Program
        self.value = value
        self.requires_board_state = rbs
        self.turn_last_moved = 0

    def copy(self):
        p = Piece()
        p.color = self.color
        p.name = self.name
        p.symbol = self.symbol
        p.value = self.value
        p.requires_board_state = self.requires_board_state
        p.turn_last_moved = self.turn_last_moved
        return p

    def get_potential_moves(self, row, col, board_height=8, board_width=8):
        return []

    def update_turn_last_moved(self, turn_count):
        self.turn_last_moved = turn_count

if __name__ == '__main__':
    p = Piece()
    print(p.color, p.name, p.value)
