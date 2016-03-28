from random import randint

board = []
num_of_ships = 2
sunken_ships = 0
#ship_size_max = 1

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def place_ships(num_of_ships):
    locations = [num_of_ships-1][1]
    ship_size = 1
    for i in range(num_of_ships):
        locations[i][0] = random_row(board)
        locations[i][1] = random_col(board)
        """for s in ship_size:
            locations[i][s][0] = random_row(board)
            locations[i][s][1] = random_col(board)"""
    for n in num_of_ships:
        print locations[n]
    return locations
"""print ship_row
print ship_col
for i in True:
    ship2_row = random_row(board)
    ship2_col = random_col(board)
    if ship2_row != ship1_row and ship2_col != ship1_col:
        break"""

# Start the Game

print "Let's play Battleship!"
print_board(board)

ships = place_ships(num_of_ships)
chances = 8

for turn in range(chances):
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")
    
    #for i in ships[0]:
        
    
    if guess_row == ship_row and guess_col == ship_col:
        sunken_ships+=1
        if sunken_ships < num_of_ships:
            print "You sunk my battleship!"
            print "There are " + str(num_of_ships) + " ships left."
        else:
            print "Congratulations! You sunk all of my battleship!"
            print "You win!"
            break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or    guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print turn + 1
        print_board(board)
        if turn == chances:
            print "Game Over"