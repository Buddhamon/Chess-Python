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
        """Initialization of Board Object; Declaring Variables"""
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.height = 8
        self.width = 8
        self.board = [[SQUARE.Square() for c in range(self.height)] for r in range(self.width)]
        self.history = []

    def _convert_coordinates(self, chess_file, chess_rank):
        """Converts Chess rank and file values to Array row and column values"""
        row = self.height - chess_rank
        col = self.alphabet.find(chess_file)
        return row, col

    def copy_board(self):
        """Creates and returns a copy of the board; called after every move"""
        b = [[SQUARE.Square() for c in range(self.height)] for r in range(self.width)]
        for r in range(self.width):
            for c in range(self.height):
                b[r][c] = self.board[r][c].copy()
        return b

    def set_piece(self, piece, chess_file, chess_rank):
        """Sets a piece on the Board"""
        row, col = self._convert_coordinates(chess_file, chess_rank)
        square = self.board[row][col]
        square.piece = piece

    def make_move(self, color, move):
        """Checks to see if move is valid and then performs valid move"""
        try:
            cf1 = move[0]
            cr1 = move[1]
            cf2 = move[2]
            cr2 = move[3]

            return self.move_piece(color, cf1, cr1, cf2, cr2)
        except:
            return False


    def move_piece(self, color, cf1, cr1, cf2, cr2):
        """Moves a Piece from the starting Chess Position to an end Chess Position"""
        row1, col1 = self._convert_coordinates(cf1, cr1)
        row2, col2 = self._convert_coordinates(cf2, cr2)
        valid = self.is_valid_move(color, row1, col1, row2, col2)
        if valid:
            # Add the previous position to history
            self.history.append(self.copy_board()) ######## This will need to be changed later on

            # Swap pieces
            start_square = self.board[row1][col1]
            end_square = self.board[row2][col2]
            end_square.piece = start_square.piece
            end_square.piece.first_move = False
            start_square.piece = PIECE.Piece()
        return valid

    def is_valid_move(self, color, row1, col1, row2, col2):
        """Checks to see if move is valid"""
        # Check to see if rows or cols are outside bounds
        if row1 >= self.height or row1 < 0 or row2 >= self.height or row2 < 0:
            return False
        if col1 >= self.width or col1 < 0 or col2 >= self.width or col2 < 0:
            return False

        # Check to see if the move is moving to the same place
        if row1 == row2 and col1 == col2:
            return False

        start_square = self.board[row1][col1]

        # Check to see if selected piece is correct color
        if start_square.piece.color != color:
            return False

        # Gets all potentially available moves for the piece; checks if piece requires board_state
        if start_square.piece.requires_board_state:
            moves = start_square.piece.get_valid_moves(row1, col1, self.board)
        else:
            moves = start_square.piece.get_valid_moves(row1, col1)

        # Check to see if move is found in the available moves, also check if the
        #       the path of the move is blocked
        return self.is_path_blocked(moves, start_square, row2, col2)

    def is_path_blocked(self, moves, start_square, row, col):
        """Checks to see if move path has an obstruction"""
        valid = False
        for m in moves:
            if [row, col] in m:
                valid = True
                index = m.index([row, col])
                for i in range(index+1):
                    r = m[i][0]
                    c = m[i][1]
                    end_square = self.board[r][c]
                    if i == index:
                        if start_square.piece.color == end_square.piece.color:
                            valid = False
                    else:
                        if end_square.has_piece():
                            valid = False
        return valid

    def set_standard_board(self):
        """Sets the Board with the standard Chess Opening"""
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

    def print_board(self, move_count=None):
        """Prints a String visualization of the Board"""
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
            if r != int((self.height-1)/2) or move_count is None:
                print(line)
            else:
                print(line, end='')
                print('      Move: ' + str(move_count))
            print('    -----------------------------------------')
        print('\n')



if __name__ == '__main__':
    white = 'white'
    black = 'black'

    b = Board()
    b.print_board()
    b.set_standard_board()
    b.print_board()
    print(b.move_piece(white, 'A', 2, 'A', 4))
    b.print_board(1)
