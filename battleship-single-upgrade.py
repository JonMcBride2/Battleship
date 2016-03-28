from random import randint

def letsPlay():
	print
	print "Welcome to Battleship!"
	
	inPlay = True
	while inPlay:
		player_count = 0
		player_count = input("How many players are there? (1 or 2): ")
		
		while player_count <> 1 and player_count <> 2:
			print
			print str(player_count) + " is not a valid number of players."
			player_count = input("How many players are there? (1 or 2): ")
		
		if player_count == 1:			
			while player_count <> "1" and player_count <> "C":
				player_count = raw_input("Solo or Vs Comp? (1 or C): ")
				if player_count == "1":
					player_count = 1
					break
				elif player_count.upper() == "C":
					player_count = player_count.upper()
					break
				else:
					print
					print str(player_count) + " is not a valid response."
		
		ship_count = 0
		ship_count = input("How many ships would you like? (1 or 2): ")
		
		while ship_count <> 1 and ship_count <> 2:
			print
			print str(ship_count) + " is not a valid number of ships."
			ship_count = input("How many ships would you like? (1 or 2): ")
		
		print
		print "Let's play Battleship!"

		if player_count == 1:
			singlePlayerMode(ship_count)
		elif player_count == "C":
			"""print
			print "****Sorry. Vs Comp mode is in development. I'll start Solo mode for you.****" """
			vsCompMode(ship_count)
		else:
			twoPlayerMode(ship_count)
		
		print
		again = raw_input("Play again? (Y or N): ")
		if again.upper() != "Y": inPlay = False
	print
	print "Thanks for Playing!"

def print_board(board):
	print
	for row in board:
		print " ".join(row)
	print

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
	
def generateBoard(size): #Not Currently Used
	for x in range(size):
		board.append(["O"] * size)
	
def placeShips(numShips,numPlayers,board):
	ships = [[],[]]
	for player in range(0,numPlayers):
		for num in range(0,numShips):
			shipGen = True
			while shipGen:
				ship_row = random_row(board)
				ship_col = random_col(board)
				shipGen = False
				for ship in range(0,len(ships[player])):
					if ships[player][ship][0] == ship_row and ships[player][ship][1] == ship_col:
						shipGen = True
						break
			ships[player].append([ship_row,ship_col])
	return ships
	
def placeShips2(numShips,numPlayers,board,maxLength=1):
	ships = [[],[]]
	for player in range(0,numPlayers):
		for num in range(0,numShips):
			shipGen = True
			while shipGen:
				ship_row = random_row(board)
				ship_col = random_col(board)
				shipGen = False
				for ship in range(0,len(ships[player])):
					if ships[player][ship][0] == ship_row and ships[player][ship][1] == ship_col:
						shipGen = True
						break
			ships[player].append([ship_row,ship_col])
	return ships
	
"""def checkShips(player,guess,ships):
	for ship in (ships[player-1]):
		if ship == guess: return True
	return False
"""
def checkShips(guess,ships,player=0):
	if player==2: player = 0
	for ship in (ships[player]):
		if ship == guess: return True
	return False

def printShips(ships): #print ships for testing purposes
	for player in range(0,len(ships)):
		if len(ships[player]) > 0:
			print "Ships for Player " + str(player+1)
			for ship in ships[player]:
				print ship

def show_board(board,ship_row,ship_col):
	if board[ship_row][ship_col] == "X":
		board[ship_row][ship_col] = "*"
	else:
		board[ship_row][ship_col] = "S"
	print_board(board)

def show_boardShips(board,ships):
	for ship in ships:
		if board[ship[0]][ship[1]] == "X":
			board[ship[0]][ship[1]] = "*"
		else:
			board[ship[0]][ship[1]] = "S"
	print_board(board)

def computeStats(board,round,winner,player,playerCount):
	hits = 0
	boardMisses = 0
	for row in board:
		hits += row.count('*')
		boardMisses += row.count('X')
	misses = round - hits
	if playerCount == 2 and winner == "p1" and player == "p2": misses -= 1
	boardMisses = misses - boardMisses
	
	if player == "p1": 
		print "Player 1 Stats"
		print
	else:
		print "Player 2 Stats"
		print
	
	print "Rounds Played: ", round
	print "Hits: ", hits
	print "Misses: ", misses
	print "*Repeats/Out of the Ocean: ", boardMisses

def singlePlayerMode(numShips):
	board = []

	for x in range(5):
		board.append(["O"] * 5)

	print_board(board)
	
	if numShips <> 1:
		print str(numShips) + " ships is currently unsupported. Only 1 ship will be generated. Sorry."
		numShips = 1
	ships = placeShips(numShips,1,board)
	
	#printShips(ships)

	for round in range(4):
		print
		print "Round # " + str(round+1)
		print
		guess_row = input("Guess Row: ")
		guess_col = input("Guess Col: ")

		if checkShips([guess_row,guess_col],ships):
			board[guess_row][guess_col] = "X"
			print
			print "Congratulations! You sunk my battleship!"
			show_boardShips(board,ships[0])
			print
			computeStats(board,round+1,"p1","p1",1)
			break
		else:
			if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
				print
				print "Oops, that's not even in the ocean."
			elif(board[guess_row][guess_col] == "X"):
				print
				print "You guessed that one already."
			else:
				print
				print "You missed my battleship!"
				board[guess_row][guess_col] = "X"
			
			if round == 3:
				print
				print "Game Over"
				show_boardShips(board,ships[0])
				print
				computeStats(board,round+1,"comp","p1",1)
			else:
				print_board(board)

def vsCompMode(numShips):
	p1board = []
	compboard = []	

	for x in range(5):
		p1board.append(["O"] * 5)
		compboard.append(["O"] * 5)

	print_board(p1board)
	
	if numShips <> 1:
		print str(numShips) + " ships is currently unsupported. Only 1 ship will be generated. Sorry."
		numShips = 1
	ships = placeShips(numShips,2,p1board)
	
	printShips(ships)
	
	round = 1
	
	while round > 0:
		print
		print "Round # " + str(round)
		print
		
		#Player's turn
		
		guess_row = input("Guess Row: ")
		guess_col = input("Guess Col: ")

		if checkShips([guess_row,guess_col],ships,1):
			compboard[guess_row][guess_col] = "X"
			print
			print "Congratulations! You sunk my battleship!"
			show_boardShips(p1board,ships[0])
			show_boardShips(compboard,ships[1])
			print
			computeStats(compboard,round,"p1","p1",1)
			break
		else:
			if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
				print
				print "Oops, that's not even in the ocean."
			elif(compboard[guess_row][guess_col] == "X"):
				print
				print "You guessed that one already."
			else:
				print
				print "You missed my battleship!"
				compboard[guess_row][guess_col] = "X"
			
			"""print_board(p1board)"""
			print_board(compboard)
		#Player beats himself
		#Comp's turn
		
		guess_row = random_row(p1board)
		guess_col = random_col(p1board)
		
		if checkShips([guess_row,guess_col],ships,2):
			p1board[guess_row][guess_col] = "X"
			print "I sunk your battleship!"
			print "I win!"
			show_boardShips(p1board,ships[0])
			show_boardShips(compboard,ships[1])
			print
			computeStats(compboard,round,"comp","p1",2)
			break
			break
		else:
			if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
				print "Oops, that's not even in the ocean."
			elif(p1board[guess_row][guess_col] == "X"):
				print "Oops, I guessed that one already."
			else:
				print "I missed your battleship!"
				p1board[guess_row][guess_col] = "X"
			
			#print_board(p1board)
			#print_board(compboard)
		round += 1

"""

Ways to expand this game

Make multiple battleships: you'll need to be careful because you need to make sure that you don't place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you'll need to make sure you don't accidentally place part of a ship off the side of the board.

Make your game a two-player game. +

Use functions to allow your game to have more features like rematches+, statistics+ and more!

Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!

"""

def twoPlayerMode(numShips):
	p1board = []
	p2board = []
	
	for x in range(5):
		p1board.append(["O"] * 5)
		p2board.append(["O"] * 5)
		
	print_board(p1board)
	print_board(p2board)
		
	if numShips <> 1:
		print str(numShips) + " ships is currently unsupported. Only 1 ship will be generated. Sorry."
		numShips = 1
	ships = placeShips(numShips,2,p1board)
	
	printShips(ships)
	
	round = 1
	
	while round > 0:
		print
		print "Round " + str(round)
		print
		print "Player 1: It's your turn."
		
		guess_row = input("Guess Row: ")
		guess_col = input("Guess Col: ")
		
		if checkShips([guess_row,guess_col],ships,1):
			p2board[guess_row][guess_col] = "X"
			print
			print "Congratulations! You sunk the battleship!"
			print "Player 1 wins!"
			show_boardShips(p1board,ships[0])
			show_boardShips(p2board,ships[1])
			print
			computeStats(p2board,round,"p1","p1",2)
			print
			computeStats(p1board,round,"p1","p2",2)
			break
		else:
			if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
				print "Oops, that's not even in the ocean."
			elif(p2board[guess_row][guess_col] == "X"):
				print "You guessed that one already."
			else:
				print "You missed my battleship!"
				p2board[guess_row][guess_col] = "X"
			
			print_board(p1board)
			print_board(p2board)
				
		print
		print "Player 2: It's your turn."
		print
		
		guess_row = input("Guess Row: ")
		guess_col = input("Guess Col: ")
		
		if checkShips([guess_row,guess_col],ships,2):
			p1board[guess_row][guess_col] = "X"
			print
			print "Congratulations! You sunk the battleship!"
			print "Player 2 wins!"
			show_boardShips(p1board,ships[0])
			show_boardShips(p2board,ships[1])
			print
			computeStats(p2board,round,"p2","p1",2)
			print
			computeStats(p1board,round,"p2","p2",2)
			break
			break
		else:
			if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
				print "Oops, that's not even in the ocean."
			elif(p1board[guess_row][guess_col] == "X"):
				print "You guessed that one already."
			else:
				print "You missed my battleship!"
				p1board[guess_row][guess_col] = "X"
			
			print_board(p1board)
			print_board(p2board)
				
		round += 1

"""def update_board(board,shipr,shipc,guessr,guessc):
	if guessr == shipr and guessc == shipc:
			board[guessr][guessc] = "X"
			print "Congratulations! You sunk my battleship!"
			show_board(board)
			break
		else:
			if (guessr < 0 or guessr > 4) or (guessc < 0 or guessc > 4):
				print "Oops, that's not even in the ocean."
			elif(board[guessr][guessc] == "X"):
				print "You guessed that one already."
			else:
				print "You missed my battleship!"
				board[guessr][guessc] = "X"
"""

letsPlay()