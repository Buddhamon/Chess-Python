import sys
import square as SQUARE
import move as MOVE

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
        self.move_count = 1

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

    def perform_move(self, color, move):
        """Checks to see if Move is valid and then performs valid Move"""
        try:
            cf1 = move.start_coordinate[0]
            cr1 = move.start_coordinate[1]
            cf2 = move.attack_coordinate[0]
            cr2 = move.attack_coordinate[1]

            return self.move_piece(color, cf1, cr1, cf2, cr2)
        except:
            return False


    def move_piece(self, color, cf1, cr1, cf2, cr2):
        """Moves a Piece from the starting Chess Position to an end Chess Position"""
        row1, col1 = self._convert_coordinates(cf1, cr1)
        row2, col2 = self._convert_coordinates(cf2, cr2)
        response = self.is_valid_move(color, row1, col1, row2, col2)
        if response["valid"]:
            # Add the previous position to history
            self.history.append(self.copy_board()) ######## TODO: This will need to be changed later on

            # Swap pieces
            start_square = self.board[row1][col1]
            end_square = self.board[row2][col2]
            if response['isQueening']:
                end_square.piece = QUEEN.Queen(color)
            else:
                end_square.piece = start_square.piece ######## TODO:This will need to flag for captured piece when determining draw
            end_square.piece.turn_last_moved = self.move_count
            if response["isEnPassant"]:
                self.board[row1][col2].piece = PIECE.Piece()
            start_square.piece = PIECE.Piece()
            if response["isCastling"]:
                if col2 - col1 > 0: # King Side Castle
                    self.board[row2][col2-1].piece = self.board[row2][col2+1].piece
                    self.board[row2][col2-1].piece.turn_last_moved = self.move_count
                    self.board[row2][col2+1].piece = PIECE.Piece()
                else: # Queen Side Castle
                    self.board[row2][col2+1].piece = self.board[row2][col2-2].piece
                    self.board[row2][col2+1].piece.turn_last_moved = self.move_count
                    self.board[row2][col2-2].piece = PIECE.Piece()
            self.move_count += 1
        return response["valid"]

    def is_valid_move(self, color, row1, col1, row2, col2):
        """Checks to see if move is valid and flags if the move is an En Passant, a Castling, or Queening move;
        Sends back dictionary"""
        response = dict()
        response["valid"] = False
        response["isCastling"] = False
        response["isEnPassant"] = False
        response["isQueening"] = False

        # Check to see if rows or cols are outside bounds
        if row1 >= self.height or row1 < 0 or row2 >= self.height or row2 < 0:
            return response
        if col1 >= self.width or col1 < 0 or col2 >= self.width or col2 < 0:
            return response

        # Check to see if the move is moving to the same place
        if row1 == row2 and col1 == col2:
            return response

        start_square_piece = self.board[row1][col1].piece
        end_square_piece = self.board[row2][col2].piece

        # Check to see if selected piece is correct color
        if start_square_piece.color != color:
            return response

        # Check to see if target square's piece is not the same as the correct color
        if end_square_piece.color == color:
            return response

        # Gets all potentially available moves for the piece; checks if piece requires board_state
        if start_square_piece.requires_board_state:
            moves = start_square_piece.get_valid_moves(row1, col1, self.board, self.move_count)
        else:
            moves = start_square_piece.get_valid_moves(row1, col1)

        # Check to see if move is found in the available moves, then checks if the
        #       the path of the move is blocked
        attack_coordinate = [row2, col2]
        for move in moves:
            if attack_coordinate == move.attack_coordinate:
                response["isEnPassant"] = move.isEnPassant
                response["isCastling"] = move.isCastling
                response["isQueening"] = move.isQueening
                response["valid"] = self.is_move_blocked(move)
        return response

    def is_move_blocked(self, move):
        """Checks to see if move path has an obstruction or is blocked"""
        valid = True
        for coordinate in move.pass_coordinates:
            r = coordinate[0]
            c = coordinate[1]
            pass_square = self.board[r][c]
            if pass_square.has_piece():
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

    def print_board(self):
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
            if r != int((self.height-1)/2) or self.move_count is None:
                print(line)
            else:
                print(line, end='')
                print('      Move: ' + str(self.move_count))
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
    b.print_board()
