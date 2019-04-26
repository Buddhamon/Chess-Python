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

        self.first_move = True

    def get_valid_moves(self, row, col, board, board_height=8, board_width=8):

        moves = []

        # Get Pawn direction from color
        if self.color == 'white':
            pawn_direction = -1
        else:
            pawn_direction = 1


        # ERROR. Must check to see if this is a valid position first!

        # Attacking Moves ((Diagonal) ...& En Passant?)
        # if board[row + pawn_direction][col-1].piece.color != self.color:
        #
        # moves.append([[row + pawn_direction, col-1], [row + pawn_direction, col+1]])
        #
        # # Non-attacking Moves
        # if self.first_move:
        #     moves.append([[row + pawn_direction, col], [row + 2*pawn_direction, col]])
        # else:
        #     moves.append([[row + pawn_direction, col]])




        # for m in reversed(moves):
        #     r = m[0][0]
        #     c = m[0][1]
        #     if r >= board_height or r < 0 or c >= board_width or c < 0:
        #         index = moves.index(m)
        #         moves.pop(index)
        #
        #
        return moves

if __name__ == '__main__':
    board = BOARD.Board()
    p = Pawn('black')
    print(p.color, p.name, p.value)
    print('For:', 0, 0)
    for move in p.get_valid_moves(0, 0, board):
        print('Move:', move)
    print('For:', 1, 1)
    for move in p.get_valid_moves(1, 1, board):
        print('Move:', move)
    print('For:', 4, 4)
    for move in p.get_valid_moves(4, 4, board):
        print('Move:', move)
    print('For:', 8, 8)
    for move in p.get_valid_moves(7, 7, board):
        print('Move:', move)

