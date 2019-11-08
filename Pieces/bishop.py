# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import move as MOVE


# Bishop Object
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
        route = []
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
            route.append([r, c])
            r += r_direction
            c += c_direction
        return route

    def get_potential_moves(self, row, col, board_height=8, board_width=8):

        routes = []

        # Up Left
        routes.append(self._diagonal_move(row, col, up=True, left=True))

        # Up Right
        routes.append(self._diagonal_move(row, col, up=True, left=False))

        # Down Right
        routes.append(self._diagonal_move(row, col, up=False, left=False))

        # Down Left
        routes.append(self._diagonal_move(row, col, up=False, left=True))

        for route in reversed(routes):
            if len(route) == 0:
                index = routes.index(route)
                routes.pop(index)

        origin = [row, col]
        return MOVE.Move.generate_moves(origin, routes)


# Bishop Test
if __name__ == '__main__':
    p = Bishop('black')
    print(p.color, p.name, p.value)

    print('\n---------------------------------------------------')
    print('For:', 0, 0)
    for move in p.get_potential_moves(0, 0):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 1, 1)
    for move in p.get_potential_moves(1, 1):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 4, 4)
    for move in p.get_potential_moves(4, 4):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 8, 8)
    for move in p.get_potential_moves(7, 7):
        move.print_move()

