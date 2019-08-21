class Piece():

    # Define Default Class Variables
    def __init__(self):
        self.color = 'null'
        self.name = 'null piece'
        self.symbol = '  '
        self.value = 0
        self.requires_board_state = False
        self.first_move = True

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
        self.first_move = True

    def copy(self):
        p = Piece()
        p.color = self.color
        p.name = self.name
        p.symbol = self.symbol
        p.value = self.value
        p.requires_board_state = self.requires_board_state
        p.first_move = self.first_move
        return p

    def get_valid_moves(self, row, col, board_height=8, board_width=8):
        pass

if __name__ == '__main__':
    p = Piece()
    print(p.color, p.name, p.value)
