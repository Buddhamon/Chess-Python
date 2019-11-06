# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import move as MOVE


# King Object
class King(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        name = 'King'
        symbol_char = 'k'
        value = 1000
        requires_board_state = True
        super().declare_variables(color, name, symbol_char, value, requires_board_state)

    def get_valid_moves(self, row, col, board, move_count, board_height=8, board_width=8):

        routes = []

        # Up Left
        routes.append([[row-1, col-1]])

        # Up Right
        routes.append([[row-1, col+1]])

        # Down Right
        routes.append([[row+1, col+1]])

        # Down Left
        routes.append([[row+1, col-1]])

        # Up
        routes.append([[row-1, col]])

        # Down
        routes.append([[row+1, col]])

        # Left
        routes.append([[row, col-1]])

        # Right
        routes.append([[row, col+1]])

        # Castle King Side
        # if self.color == 'white':
        #     board[7][7]

        # Castle Queen Side

        for route in reversed(routes):
            r = route[0][0]
            c = route[0][1]
            if r >= board_height or r < 0 or c >= board_width or c < 0:
                index = routes.index(route)
                routes.pop(index)

        origin = [row, col]
        return MOVE.Move.generate_moves(origin, routes)


# King Test
if __name__ == '__main__':
    p = King('black')
    print(p.color, p.name, p.value)

    print('\n---------------------------------------------------')
    print('For:', 0, 0)
    for move in p.get_valid_moves(0, 0, board=None, move_count=0):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 1, 1)
    for move in p.get_valid_moves(1, 1, board=None, move_count=0):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 4, 4)
    for move in p.get_valid_moves(4, 4, board=None, move_count=0):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 8, 8)
    for move in p.get_valid_moves(7, 7, board=None, move_count=0):
        move.print_move()

