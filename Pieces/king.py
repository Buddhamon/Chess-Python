# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import board as BOARD
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

    def get_potential_moves(self, row, col, board, move_count, board_height=8, board_width=8):

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

        # Castling ########## TODO: Check for Check in King Passing Squares
        if self.turn_last_moved == 0: # The following routes are the passing squares, and then ending square
            # White's King Side Castle
            if self.color == 'white' and board[7][7].piece.turn_last_moved == 0: # Hardcoded King Rook's Position
                routes.append([[row, col+1], [row, col+2], [row, col+2, 'isCastling']])
            # White's Queen Side Castle
            if self.color == 'white' and board[7][0].piece.turn_last_moved == 0: # Hardcoded Queen Rook's Position
                routes.append([[row, col-1], [row, col-2], [row, col-3], [row, col-2, 'isCastling']])
            # Black's King Side Castle
            if self.color == 'black' and board[0][7].piece.turn_last_moved == 0: # Hardcoded King Rook's Position
                routes.append([[row, col+1], [row, col+2], [row, col+2, 'isCastling']])
            # Black's Queen Side Castle
            if self.color == 'black' and board[0][0].piece.turn_last_moved == 0: # Hardcoded Queen Rook's Position
                routes.append([[row, col-1], [row, col-2], [row, col-3], [row, col-2, 'isCastling']])

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

    b = BOARD.Board()
    b = b.board
    p = King('black')
    print(p.color, p.name, p.value)

    print('\n---------------------------------------------------')
    print('For:', 0, 0)
    for move in p.get_potential_moves(0, 0, board=b, move_count=0):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 1, 1)
    for move in p.get_potential_moves(1, 1, board=b, move_count=0):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 4, 4)
    for move in p.get_potential_moves(4, 4, board=b, move_count=0):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 8, 8)
    for move in p.get_potential_moves(7, 7, board=b, move_count=0):
        move.print_move()

