import piece as PIECE

class Knight(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        name = 'Knight'
        symbol_char = 'n'
        value = 3
        requires_board_state = False
        super().declare_variables(color, name, symbol_char, value, requires_board_state)

    def get_valid_coordinates(self, row, col, board_height=8, board_width=8):

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

