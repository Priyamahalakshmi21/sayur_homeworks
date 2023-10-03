#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. 
#You can use "B" to print black squares
# Define the size of the chessboard (8x8 for a standard chessboard)
board_size = 8
for row in range(board_size):
    for col in range(board_size):
        if (row + col) % 2 == 0:
            print('\u25A0', end=' ')  
        else:
            print('\u25A1', end=' ')  
    print()  