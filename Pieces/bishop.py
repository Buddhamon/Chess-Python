import piece as PIECE

class Bishop(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        name = 'Bishop'
        symbol_char = 'b'
        value = 3
        requires_board_state = False
        super().declare_variables(color, name, symbol_char, value, requires_board_state)

    @staticmethod
    def _diagonal_move(r, c, up, left, board_height=8, board_width=8):
        move = []
        if up:
            r_direction = -1
        else:
            r_direction = 1
        if left:
            c_direction = -1
        else:
            c_direction = 1
        r += r_direction
        c += c_direction
        while r >= 0 and c >= 0 and r < board_height and c < board_width:
            move.append([r, c])
            r += r_direction
            c += c_direction
        return move

    def get_valid_moves(self, row, col, board_height=8, board_width=8):

        moves = []

        # Up Left
        moves.append(self._diagonal_move(row, col, up=True, left=True))

        # Up Right
        moves.append(self._diagonal_move(row, col, up=True, left=False))

        # Down Right
        moves.append(self._diagonal_move(row, col, up=False, left=False))

        # Down Left
        moves.append(self._diagonal_move(row, col, up=False, left=True))

        for m in reversed(moves):
            if len(m) == 0:
                index = moves.index(m)
                moves.pop(index)
        return moves


if __name__ == '__main__':
    p = Bishop('black')
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

