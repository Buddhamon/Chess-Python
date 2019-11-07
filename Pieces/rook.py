# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import move as MOVE


# Rook Object
class Rook(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        name = 'Rook'
        symbol_char = 'r'
        value = 5
        requires_board_state = False
        super().declare_variables(color, name, symbol_char, value, requires_board_state)

    def get_valid_moves(self, row, col, board_height=8, board_width=8):

        routes = []

        # Up
        routes.append([[row - (i+1), col] for i in range(row)])

        # Down
        routes.append([[row + (i+1), col] for i in range(board_height-(row+1))])

        # Left
        routes.append([[row, col - (i+1)] for i in range(col)])

        # Right
        routes.append([[row, col + (i+1)] for i in range(board_width-(col+1))])

        for route in reversed(routes):
            if len(route) == 0:
                index = routes.index(route)
                routes.pop(index)

        origin = [row, col]
        return MOVE.Move.generate_moves(origin, routes)


# Rook Test
if __name__ == '__main__':
    p = Rook('black')
    print(p.color, p.name, p.value)

    print('\n---------------------------------------------------')
    print('For:', 0, 0)
    for move in p.get_valid_moves(0, 0):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 1, 1)
    for move in p.get_valid_moves(1, 1):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 4, 4)
    for move in p.get_valid_moves(4, 4):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 8, 8)
    for move in p.get_valid_moves(7, 7):
        move.print_move()

