class Move:

    def __init__(self):
        self.passing_squares = None
        self.attacking_square = None

    def is_path_blocked(self, moves, start_square, row, col):
        """Checks to see if move path has an obstruction"""
        pass
        # valid = False
        # for m in moves:
        #     if [row, col] in m:
        #         valid = True
        #         index = m.index([row, col])
        #         for i in range(index+1):
        #             r = m[i][0]
        #             c = m[i][1]
        #             end_square = self.board[r][c]
        #             if i == index:
        #                 if start_square.piece.color == end_square.piece.color:
        #                     valid = False
        #             else:
        #                 if end_square.has_piece():
        #                     valid = False
        # return valid


if __name__ == '__main__':
    move = Move()
