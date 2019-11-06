# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import square as SQUARE
import board as BOARD
import move as MOVE


# Pawn Object
class Pawn(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        name = 'Pawn'
        symbol_char = 'p'
        value = 1
        requires_board_state = True
        super().declare_variables(color, name, symbol_char, value, requires_board_state)

    def get_valid_moves(self, row, col, board, move_count, board_height=8, board_width=8):

        routes = []

        # Get Pawn direction from color
        if self.color == 'white':
            pawn_direction = -1
        else:
            pawn_direction = 1

        # Attacking Moves
        # Normal Attack
        if col-1 >= 0:
            square = board[row + pawn_direction][col-1]
            if square.piece.color != 'null' and square.piece.color != self.color:
                routes.append([[row + pawn_direction, col-1]])
        if col+1 < board_width:
            square = board[row + pawn_direction][col+1]
            if square.piece.color != 'null' and square.piece.color != self.color:
                routes.append([[row + pawn_direction, col+1]])
        # En Passant
        if self.color == 'white' and row == 3: # This is hardcoded to be the 5 rank
            if col-1 >= 0:
                square = board[row][col-1]
                if square.piece.color == 'black' and (square.piece.turn_last_moved == move_count-1):
                    routes.append([[row + pawn_direction, col-1, "isEnPassant"]])
            if col+1 < board_width:
                square = board[row][col+1]
                if square.piece.color == 'black' and (square.piece.turn_last_moved == move_count-1):
                    routes.append([[row + pawn_direction, col+1, "isEnPassant"]])

        if self.color == 'black' and row == 4: # This is hardcoded to be the 4 rank
            if col-1 >= 0:
                square = board[row][col-1]
                if square.piece.color == 'white' and (square.piece.turn_last_moved == move_count-1):
                    routes.append([[row + pawn_direction, col-1, "isEnPassant"]])
            if col+1 < board_width:
                square = board[row][col+1]
                if square.piece.color == 'white' and (square.piece.turn_last_moved == move_count-1):
                    routes.append([[row + pawn_direction, col+1, "isEnPassant"]])

        # Non-attacking Moves
        if self.turn_last_moved == 0:
            square = board[row + 2*pawn_direction][col]
            if square.piece.color == 'null':
                routes.append([[row + pawn_direction, col], [row + 2*pawn_direction, col]])
        else:
            square = board[row + pawn_direction][col]
            if square.piece.color == 'null':
                routes.append([[row + pawn_direction, col], [row + pawn_direction, col]])

        for route in reversed(routes):
            r = route[0][0]
            c = route[0][1]
            if r >= board_height or r < 0 or c >= board_width or c < 0:
                index = routes.index(route)
                routes.pop(index)

        origin = [row, col]
        return MOVE.Move.generate_moves(origin, routes)


# Pawn Test
if __name__ == '__main__':
    b = BOARD.Board()
    b = b.board
    p1 = Pawn('black')
    print(p1.color, p1.name, p1.value)

    print('\n---------------------------------------------------')
    print('For:', 1, 1)
    for move in p1.get_valid_moves(1, 1, b, 0):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 1, 6)
    for move in p1.get_valid_moves(1, 6, b, 0):
        move.print_move()
