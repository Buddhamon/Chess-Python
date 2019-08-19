import piece as PIECE

class Rook(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        name = 'Rook'
        symbol_char = 'r'
        value = 5
        requires_board_state = False
        super().declare_variables(color, name, symbol_char, value, requires_board_state)

    def get_valid_coordinates(self, row, col, board_height=8, board_width=8):

        moves = []

        # Up
        moves.append([[row - (i+1), col] for i in range(row)])

        # Down
        moves.append([[row + (i+1), col] for i in range(board_height-(row+1))])

        # Left
        moves.append([[row, col - (i+1)] for i in range(col)])

        # Right
        moves.append([[row, col + (i+1)] for i in range(board_width-(col+1))])

        for m in reversed(moves):
            if len(m) == 0:
                index = moves.index(m)
                moves.pop(index)
        return moves


if __name__ == '__main__':
    p = Rook('black')
    print(p.color, p.name, p.value)
    print('For:', 0, 0)
    for move in p.get_valid_coordinates(0, 0):
        print('Move:', move)
    print('For:', 1, 1)
    for move in p.get_valid_coordinates(1, 1):
        print('Move:', move)
    print('For:', 4, 4)
    for move in p.get_valid_coordinates(4, 4):
        print('Move:', move)
    print('For:', 8, 8)
    for move in p.get_valid_coordinates(7, 7):
        print('Move:', move)

