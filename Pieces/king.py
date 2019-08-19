import piece as PIECE

class King(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        name = 'King'
        symbol_char = 'k'
        value = 1000
        requires_board_state = True
        super().declare_variables(color, name, symbol_char, value, requires_board_state)

    def get_valid_coordinates(self, row, col, board, board_height=8, board_width=8):

        moves = []

        # Up Left
        moves.append([[row-1, col-1]])

        # Up Right
        moves.append([[row-1, col+1]])

        # Down Right
        moves.append([[row+1, col+1]])

        # Down Left
        moves.append([[row+1, col-1]])

        # Up
        moves.append([[row-1, col]])

        # Down
        moves.append([[row+1, col]])

        # Left
        moves.append([[row, col-1]])

        # Right
        moves.append([[row, col+1]])

        for m in reversed(moves):
            r = m[0][0]
            c = m[0][1]
            if r >= board_height or r < 0 or c >= board_width or c < 0:
                index = moves.index(m)
                moves.pop(index)
        return moves


if __name__ == '__main__':
    p = King('black')
    print(p.color, p.name, p.value)
    print('For:', 0, 0)
    for move in p.get_valid_coordinates(0, 0, board=None):
        print('Move:', move)
    print('For:', 1, 1)
    for move in p.get_valid_coordinates(1, 1, board=None):
        print('Move:', move)
    print('For:', 4, 4)
    for move in p.get_valid_coordinates(4, 4, board=None):
        print('Move:', move)
    print('For:', 8, 8)
    for move in p.get_valid_coordinates(7, 7, board=None):
        print('Move:', move)

