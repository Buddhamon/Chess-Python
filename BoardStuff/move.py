class Move:

    def __init__(self, starting, attacking):
        '''Constructor for Move Object; Contains Chess Move information
                start_coordinate: origin coordinate
                attack_coordinate: destination coordinate
                pass_coordinates: list of passing coordinates between starting and attacking'''
        self.start_coordinate = starting
        self.attack_coordinate = attacking
        self.pass_coordinates = []
        self.isEnPassant = False
        self.isCastling = False
        self.isQueening =False

    @staticmethod
    def generate_moves(origin, routes):
        '''Generates a list of Moves from a routes data-structure created by a piece'''
        moves = []
        for route in routes:
            pass_coordinates = []
            for coordinate in route:
                if coordinate[-1] == 'isEnPassant':
                    coordinate.pop(-1)
                    m = Move(origin, coordinate)
                    m.isEnPassant = True
                elif coordinate[-1] == 'isCastling':
                    coordinate.pop(-1)
                    m = Move(origin, coordinate)
                    m.isCastling = True
                elif coordinate[-1] == 'isQueening':
                    coordinate.pop(-1)
                    m = Move(origin, coordinate)
                    m.isQueening = True
                else:
                    m = Move(origin, coordinate)
                m.pass_coordinates = pass_coordinates.copy()
                moves.append(m)
                pass_coordinates.append(coordinate)
        return moves

    def print_move(self):
        print('Move:')
        print('\tstart:', self.start_coordinate)
        print('\tpass:', self.pass_coordinates)
        print('\tattack:', self.attack_coordinate)
        if self.isEnPassant:
            print('\tisEnPassant:', self.isEnPassant)
        if self.isCastling:
            print('\tisCastling:', self.isCastling)
        if self.isQueening:
            print('\tisQueening:', self.isQueening)

if __name__ == '__main__':
    m0 = Move(['E', 2], ['E', 4])
    m0.print_move()
    print()
    print('---------------------------------------------------')

    origin1 = [0, 0]
    routes_ds1 = [
        [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]],
        [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
    ]
    moves1 = Move.generate_moves(origin1, routes_ds1)
    for m in moves1:
        m.print_move()
    print()
    print('---------------------------------------------------')

    origin2 = [1, 1]
    routes_ds2 = [
        [[0, 1]],
        [[2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]],
        [[1, 0]],
        [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]
    ]
    moves2 = Move.generate_moves(origin2, routes_ds2)
    for m in moves2:
        m.print_move()
    print()
    print('---------------------------------------------------')

    origin3 = [4, 4]
    routes_ds3 = [
        [[3, 4], [2, 4], [1, 4], [0, 4]],
        [[5, 4], [6, 4], [7, 4]],
        [[4, 3], [4, 2], [4, 1], [4, 0]],
        [[4, 5], [4, 6], [4, 7]]
    ]
    moves3 = Move.generate_moves(origin3, routes_ds3)
    for m in moves3:
        m.print_move()

    print()
    print('---------------------------------------------------')

    origin4 = [3, 4]
    routes_ds4 = [
        [[2, 3, 'isEnPassant']],
         [[2, 4]]
    ]
    moves4 = Move.generate_moves(origin4, routes_ds4)
    for m in moves4:
        m.print_move()

    print()
    print('---------------------------------------------------')

    origin5 = [6, 4]
    routes_ds5 = [
        [[7, 4, 'isQueening']],
         [[7, 5, 'isQueening']]
    ]
    moves5 = Move.generate_moves(origin5, routes_ds5)
    for m in moves5:
        m.print_move()

