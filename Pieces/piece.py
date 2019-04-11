class Piece():

    # Define Class Variables
    def __init__(self):
        self.color = 'null'
        self.name = 'null piece'
        self.symbol = '  '
        self.value = 0

    def get_valid_moves(self, row, col, board_height=8, board_width=8):
        pass

if __name__ == '__main__':
    p = Piece()
    print(p.color, p.name, p.value)
