import piece as PIECE

class Pawn(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        self.color = color
        self.name = 'Pawn'
        if color == 'black':
            self.symbol = 'bp'
        elif color == 'white':
            self.symbol = 'wp'
        else:
            print('Color is not known')
            0/0 # Error Terminates Program
        self.value = 1
        self.first_move = True

    def get_valid_moves(self, row, col, board_height=8, board_width=8):

        moves = []

        if self.color == 'white':
            pawn_direction = -1
        else:
            pawn_direction = 1

        if self.first_move:
            moves.append([[row + pawn_direction, col], [row + 2*pawn_direction, col]])
        else:
            moves.append([[row + pawn_direction, col]])

        for m in reversed(moves):
            r = m[0][0]
            c = m[0][1]
            if r >= board_height or r < 0 or c >= board_width or c < 0:
                index = moves.index(m)
                moves.pop(index)
        return moves

if __name__ == '__main__':
    p = Rook('black')
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

