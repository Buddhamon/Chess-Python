# Imports
import sys
sys.path.append('../Pieces')
import king as KING
sys.path.append('../BoardStuff')
import board as BOARD


# Variables
white = 'white'
black = 'black'
b_true = BOARD.Board()
b_test = BOARD.Board()

# Set Boards
b_test.set_piece(KING.King(white), 'A', 8)
b_test.set_piece(KING.King(white), 'A', 3)
b_test.set_piece(KING.King(white), 'D', 6)
b_test.set_piece(KING.King(black), 'A', 1)
b_test.set_piece(KING.King(white), 'H', 1)

b_true.set_piece(KING.King(white), 'H', 8)
b_true.set_piece(KING.King(white), 'A', 8)
b_true.set_piece(KING.King(white), 'C', 6)
b_true.set_piece(KING.King(white), 'H', 2)

# Test
true_values = []
test_values = []


test_values.append(b_test.move_piece(white, 'A', 8, 'B', 8))  # Move 1
true_values.append(True)
test_values.append(b_test.move_piece(white, 'B', 8, 'A', 8))  # Move 2
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 8, 'A', 8))  # Move 3
true_values.append(False)
test_values.append(b_test.move_piece(white, 'A', 8, 'A', 1))  # Move 4
true_values.append(False)
test_values.append(b_test.move_piece(white, 'A', 3, 'A', 2))  # Move 5
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 2, 'A', 1))  # Move 6
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 1, 'B', 2))  # Move 7
true_values.append(True)
test_values.append(b_test.move_piece(white, 'B', 1, 'H', 8))  # Move 8
true_values.append(False)
test_values.append(b_test.move_piece(white, 'B', 2, 'H', 8))  # Move 9
true_values.append(False)
test_values.append(b_test.move_piece(white, 'B', 2, 'C', 3))  # Move 10
true_values.append(True)
test_values.append(b_test.move_piece(white, 'C', 3, 'D', 4))  # Move 11
true_values.append(True)
test_values.append(b_test.move_piece(white, 'D', 4, 'E', 5))  # Move 12
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 5, 'F', 6))  # Move 13
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 6, 'G', 7))  # Move 14
true_values.append(True)
test_values.append(b_test.move_piece(white, 'G', 7, 'H', 8))  # Move 15
true_values.append(True)
test_values.append(b_test.move_piece(white, 'H', 8, 'H', 6))  # Move 16
true_values.append(False)
test_values.append(b_test.move_piece(white, 'D', 6, 'D', 7))  # Move 17
true_values.append(True)
test_values.append(b_test.move_piece(white, 'D', 7, 'C', 8))  # Move 18
true_values.append(True)
test_values.append(b_test.move_piece(white, 'C', 8, 'B', 8))  # Move 19
true_values.append(True)
test_values.append(b_test.move_piece(white, 'B', 8, 'A', 7))  # Move 20
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 7, 'B', 6))  # Move 21
true_values.append(True)
test_values.append(b_test.move_piece(white, 'B', 6, 'C', 6))  # Move 22
true_values.append(True)
test_values.append(b_test.move_piece(white, 'H', 1, 'H', 2))  # Move 22
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
