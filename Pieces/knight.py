# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import move as MOVE


# Knight Object
class Knight(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        name = 'Knight'
        symbol_char = 'n'
        value = 3
        requires_board_state = False
        super().declare_variables(color, name, symbol_char, value, requires_board_state)

    def get_valid_moves(self, row, col, board_height=8, board_width=8):

        routes = []

        routes.append([[row-1, col-2]])  # 1
        routes.append([[row-2, col-1]])  # 2
        routes.append([[row-2, col+1]])  # 3
        routes.append([[row-1, col+2]])  # 4
        routes.append([[row+1, col+2]])  # 5
        routes.append([[row+2, col+1]])  # 6
        routes.append([[row+2, col-1]])  # 7
        routes.append([[row+1, col-2]])  # 8

        for route in reversed(routes):
            r = route[0][0]
            c = route[0][1]
            if r >= board_height or r < 0 or c >= board_width or c < 0:
                index = routes.index(route)
                routes.pop(index)

        origin = [row, col]
        return MOVE.Move.generate_moves(origin, routes)


# Knight Test
if __name__ == '__main__':
    p = Knight('black')
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

