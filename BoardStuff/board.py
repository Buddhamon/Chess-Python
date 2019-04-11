import sys
import square as SQUARE
sys.path.append('../Pieces')
import piece as PIECE
import pawn as PAWN
import rook as ROOK
import knight as KNIGHT
import bishop as BISHOP
import queen as QUEEN
import king as KING

class Board:

    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.height = 8
        self.width = 8
        self.board = [[SQUARE.Square() for c in range(self.height)] for r in range(self.width)]


    def _convert_coordinates(self, chess_file, chess_rank):
        row = self.height - chess_rank
        col = self.alphabet.find(chess_file)
        return row, col

    def set_piece(self, piece, chess_file, chess_rank):
        row, col = self._convert_coordinates(chess_file, chess_rank)
        square = self.board[row][col]
        square.piece = piece

    def move_piece(self, color, cf1, cr1, cf2, cr2):
        row1, col1 = self._convert_coordinates(cf1, cr1)
        row2, col2 = self._convert_coordinates(cf2, cr2)
        valid = self.is_valid_move(color, row1, col1, row2, col2)
        if valid:
            square1 = self.board[row1][col1]
            square2 = self.board[row2][col2]
            square2.piece = square1.piece
            square1.piece = PIECE.Piece()
        return valid

    def is_valid_move(self, color, row1, col1, row2, col2):

        # Check to see if rows or cols are outside bounds
        if row1 >= self.height or row1 < 0 or row2 >= self.height or row2 < 0:
            return False
        if col1 >= self.width or col1 < 0 or col2 >= self.width or col2 < 0:
            return False

        # Check to see if the move is moving to the same place
        if row1 == row2 and col1 == col2:
            return False

        square1 = self.board[row1][col1]

        # Check to see if selected piece is correct color
        if square1.piece.color != color:
            return False

        valid = False
        moves = square1.piece.get_valid_moves(row1, col1)
        for m in moves:
            if [row2, col2] in m:
                valid = True
                index = m.index([row2, col2])
                for i in range(index+1):
                    r = m[i][0]
                    c = m[i][1]
                    square2 = self.board[r][c]
                    if i == index:
                        if square1.piece.color == square2.piece.color:
                            valid = False
                    else:
                        if square2.has_piece():
                            valid = False
        return valid

    def set_standard_board(self):
        white = 'white'
        black = 'black'

        # Pawn
        for i in range(8):
            self.set_piece(PAWN.Pawn(white), self.alphabet[i], 2)
        for i in range(8):
            self.set_piece(PAWN.Pawn(black), self.alphabet[i], 7)

        # Rooks
        self.set_piece(ROOK.Rook(white), 'A', 1)
        self.set_piece(ROOK.Rook(white), 'H', 1)
        self.set_piece(ROOK.Rook(black), 'A', 8)
        self.set_piece(ROOK.Rook(black), 'H', 8)

        # Knights
        self.set_piece(KNIGHT.Knight(white), 'B', 1)
        self.set_piece(KNIGHT.Knight(white), 'G', 1)
        self.set_piece(KNIGHT.Knight(black), 'B', 8)
        self.set_piece(KNIGHT.Knight(black), 'G', 8)

        # Knights
        self.set_piece(BISHOP.Bishop(white), 'C', 1)
        self.set_piece(BISHOP.Bishop(white), 'F', 1)
        self.set_piece(BISHOP.Bishop(black), 'C', 8)
        self.set_piece(BISHOP.Bishop(black), 'F', 8)

        # Queens
        self.set_piece(QUEEN.Queen(white), 'D', 1)
        self.set_piece(QUEEN.Queen(black), 'D', 8)

        # Kings
        self.set_piece(KING.King(white), 'E', 1)
        self.set_piece(KING.King(black), 'E', 8)

    def print_board(self):
        file_header = '      '
        for i in range(8):
            file_header += self.alphabet[i] + '    '
        print(file_header)
        print('    -----------------------------------------')
        for r in range(len(self.board)):
            line = ' ' + str(len(self.board)-r) + '  |'
            for c in range(len(self.board[r])):
                square = self.board[r][c]
                symbol = square.piece.symbol
                line += ' ' + symbol + ' |'
            print(line)
            print('    -----------------------------------------')
        print('\n')



if __name__ == '__main__':
    white = 'white'
    black = 'black'

    b = Board()
    b.print_board()
    b.set_standard_board()
    b.print_board()
