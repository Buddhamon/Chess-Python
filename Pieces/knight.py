import piece as PIECE

class Knight(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        self.color = color
        self.name = 'Knight'
        if color == 'black':
            self.symbol = 'bn'
        elif color == 'white':
            self.symbol = 'wn'
        else:
            print('Color is not known')
            0/0 # Error Terminates Program
        self.value = 3

    def get_valid_moves(self, row, col, board_height=8, board_width=8):

        moves = []

        moves.append([[row-1, col-2]])  # 1
        moves.append([[row-2, col-1]])  # 2
        moves.append([[row-2, col+1]])  # 3
        moves.append([[row-1, col+2]])  # 4
        moves.append([[row+1, col+2]])  # 5
        moves.append([[row+2, col+1]])  # 6
        moves.append([[row+2, col-1]])  # 7
        moves.append([[row+1, col-2]])  # 8

        for m in reversed(moves):
            r = m[0][0]
            c = m[0][1]
            if r >= board_height or r < 0 or c >= board_width or c < 0:
                index = moves.index(m)
                moves.pop(index)
        return moves


if __name__ == '__main__':
    p = Knight('black')
    print(p.color, p.name, p.value)
    print('For:', 0, 0)
    for move in p.get_valid_moves(0, 0):
        print('Move:', move)
    print('For:', 1, 1)
    for move in p.get_valid_moves(1, 1):
        print('Move:', move)
    print('For:', 4, 4)
    for move in p.get_valid_moves(4, 4):
        print('Move:', move)
    print('For:', 8, 8)
    for move in p.get_valid_moves(7, 7):
        print('Move:', move)

