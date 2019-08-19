class Move:

    def __init__(self, starting=None, attacking=None, passing=None):
        '''Constructor for Move Object; Contains Chess Move information
                starting: origin coordinate
                attacking: destination coordinate
                passing: list of passing coordinates between starting and attacking'''
        self.start_coordinate = starting
        self.pass_coordinates = passing
        self.attack_coordinate = attacking


if __name__ == '__main__':
    m1 = Move()
