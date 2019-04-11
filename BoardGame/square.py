import sys
sys.path.append('../Pieces')
import piece as PIECE

class Square:

    def __init__(self):
        self.color = 'null'
        self.rank = 0
        self.file = 0
        self.piece = PIECE.Piece()

    def has_piece(self):
        if self.piece.name == 'null piece':
            return False
        else:
            return True

if __name__ == '__main__':
    s = Square()
    print(s.piece.name, s.rank, s.file)
