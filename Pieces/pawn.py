# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import square as SQUARE
import board as BOARD

class Pawn(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        name = 'Pawn'
        symbol_char = 'p'
        value = 1
        requires_board_state = True
        super().declare_variables(color, name, symbol_char, value, requires_board_state)

    def get_valid_coordinates(self, row, col, board, board_height=8, board_width=8):

        moves = []

        # Get Pawn direction from color
        if self.color == 'white':
            pawn_direction = -1
        else:
            pawn_direction = 1

        # Attacking Moves ...but not En Passant? Should this occur in chess.py since it is a unique rule?
        if col-1 >= 0:
            square = board[row + pawn_direction][col-1]
            if square.piece.color != 'null' and square.piece.color != self.color:
                moves.append([[row + pawn_direction, col-1]])
        if col+1 < board_width:
            square = board[row + pawn_direction][col+1]
            if square.piece.color != 'null' and square.piece.color != self.color:
                moves.append([[row + pawn_direction, col+1]])

        # Non-attacking Moves
        if self.first_move:
            square = board[row + 2*pawn_direction][col]
            if square.piece.color == 'null':
                moves.append([[row + pawn_direction, col], [row + 2*pawn_direction, col]])
        else:
            square = board[row + pawn_direction][col]
            if square.piece.color == 'null':
                moves.append([[row + pawn_direction, col], [row + pawn_direction, col]])

        for m in reversed(moves):
            r = m[0][0]
            c = m[0][1]
            if r >= board_height or r < 0 or c >= board_width or c < 0:
                index = moves.index(m)
                moves.pop(index)
        return moves

if __name__ == '__main__':
    b = BOARD.Board()
    b = b.board
    p1 = Pawn('black')
    print(p1.color, p1.name, p1.value)
    print('For:', 1, 1)
    for move in p1.get_valid_coordinates(1, 1, b):
        print('Move:', move)
    print('For:', 1, 6)
    for move in p1.get_valid_coordinates(1, 6, b):
        print('Move:', move)
