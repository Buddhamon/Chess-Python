# Imports
import sys
sys.path.append('../Pieces')
# import piece as PIECE
import pawn as PAWN
sys.path.append('../BoardStuff')
import board as BOARD


# Variables
white = 'white'
black = 'black'
b_true = BOARD.Board()
b_test = BOARD.Board()

# Set Boards
b_test.set_piece(PAWN.Pawn(white), 'A', 2)
b_test.set_piece(PAWN.Pawn(black), 'B', 6)

b_true.set_piece(PAWN.Pawn(white), 'B', 6)


# Test

true_values = []
test_values = []

test_values.append(b_test.move_piece(white, 'A', 2, 'A', 1))  # Move 1
true_values.append(False)
test_values.append(b_test.move_piece(white, 'A', 2, 'A', 4))  # Move 2
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 4, 'A', 5))  # Move 2
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 5, 'B', 6))  # Move 2
true_values.append(True)

print('-------------------- TRUE ---------------------\n')
b_true.print_board()
print('-------------------- TEST ---------------------\n')
b_test.print_board()


accurate = True
for i in range(len(true_values)):
    if true_values[i] != test_values[i]:
        accurate = False
        print('Error Move', i+1,'--- truth:', true_values[i], '||| test:',test_values[i])
