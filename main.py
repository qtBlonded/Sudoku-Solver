"""
This is an attempt to make a sudoko solver.

Author: Quinn Bardwell
Date: 08/08/19
"""

class Board(object):
	"""
	Class that stores a board with values 1-9 or 0 if the number is not known.
	A board with *options* of possible/value numbers (1-9) that correspond to that
	position. 
	And methods to help solve the sudoko.
	"""
	HEIGHT = 9
	WIDTH = 9
	def __init__(self):
		self.board = [[0,0,0, 0,0,0, 0,0,0]
					 ,[0,0,0, 0,0,0, 0,0,0]
					 ,[0,0,0, 0,0,0, 0,0,0]

					 ,[0,0,0, 0,0,0, 0,0,0]
					 ,[0,0,0, 0,0,0, 0,0,0]
					 ,[0,0,0, 0,0,0, 0,0,0]

					 ,[0,0,0, 0,0,0, 0,0,0]
					 ,[0,0,0, 0,0,0, 0,0,0]
					 ,[0,0,0, 0,0,0, 0,0,0]]
		self.board_options = [[0,0,0, 0,0,0, 0,0,0]
							 ,[0,0,0, 0,0,0, 0,0,0]
					 		 ,[0,0,0, 0,0,0, 0,0,0]

					 		 ,[0,0,0, 0,0,0, 0,0,0]
					 		 ,[0,0,0, 0,0,0, 0,0,0]
					 		 ,[0,0,0, 0,0,0, 0,0,0]

					 		 ,[0,0,0, 0,0,0, 0,0,0]
					 		 ,[0,0,0, 0,0,0, 0,0,0]
					 		 ,[0,0,0, 0,0,0, 0,0,0]]
		for row in range(self.HEIGHT):
			for col in range(self.WIDTH):
				self.board_options[row][col] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

	def add_number(self, row, col, num):
		self.board[row][col] = num
		self.board_options[row][col] = {num}
		self.update_board_options(row, col, num)
		#UPDATE BOARD OPTIONS


	def check_board(self):
		S = set()
		for x in range(self.HEIGHT):
			for y in range(self.WIDTH):
				S.add(self.board[x][y])
			if len(S) != 9 or 0 in S:
				return False
			S.clear()
		for x in range(self.HEIGHT):
			for y in range(self.WIDTH):
				S.add(self.board[y][x])
			if len(S) != 9 or 0 in S:
				return False
			S.clear()

		for i in range((x//3)*3, x//3*3+3):
			for j in range((y//3)*3, y//3*3+3):
				pass

		return True

	def print_board(self):
		print("Printing board...")
		for row in range(self.HEIGHT):
			for col in range(self.WIDTH):
				print(" " + str(self.board[row][col]) + " ", end="")
				if (col+1)%3 == 0 and col != 8:
					print("|", end="")
			print()
			if (row+1)%3 == 0 and row != 8:
				print(" " + "-"*25)
		print()

	def print_board_options(self):
		print("Printing board options...")
		for row in range(self.HEIGHT):
			for col in range(self.WIDTH):
				print(" " + str(self.board_options[row][col]) + " ", end="")
				if (col+1)%3 == 0 and col != 8:
					print("|", end="")
			print("\n")
			if (row+1)%3 == 0 and row != 8:
				print(" " + "-"*25)
		print()

	def update_board_options(self, row, col, num):
		for row_search in range(self.HEIGHT):
			if row_search != row and num in self.board_options[row_search][col]:
				self.board_options[row_search][col].remove(num)
		for col_search in range(self.WIDTH):
			if col_search != col and num in self.board_options[row][col_search]:
				self.board_options[row][col_search].remove(num)
		for row_search in range((row//3)*3, row//3*3+3):
			for col_search in range((col//3)*3, col//3*3+3):
				if not (row_search == row and col_search == col) \
				and num in self.board_options[row_search][col_search]:
					self.board_options[row_search][col_search].remove(num)

	def create_board(self):
		print("Adding numbers to board...")
		self.add_number(0, 0, 8)
		self.add_number(0, 4, 6)
		self.add_number(0, 5, 7)
		self.add_number(0, 8, 1)
		self.add_number(1, 0, 5)
		self.add_number(1, 2, 9)
		self.add_number(1, 4, 1)
		self.add_number(1, 5, 2)
		self.add_number(1, 7, 3)
		self.add_number(1, 8, 8)
		self.add_number(2, 2, 6)
		self.add_number(2, 7, 7)
		self.add_number(3, 0, 1)
		self.add_number(3, 4, 7)
		self.add_number(4, 0, 7)
		self.add_number(4, 2, 2)
		self.add_number(4, 4, 9)
		self.add_number(4, 6, 5)
		self.add_number(4, 8, 4)
		self.add_number(5, 4, 3)
		self.add_number(5, 8, 7)
		self.add_number(6, 1, 5)
		self.add_number(6, 6, 4)
		self.add_number(7, 0, 2)
		self.add_number(7, 1, 8)
		self.add_number(7, 3, 3)
		self.add_number(7, 4, 4)
		self.add_number(7, 6, 1)
		self.add_number(7, 8, 6)
		self.add_number(8, 0, 3)
		self.add_number(8, 3, 6)
		self.add_number(8, 4, 5)
		self.add_number(8, 8, 2)

	def solve_board(self):
		print("Solving board...")
		changed = True
		iteration = 0
		while changed:
			iteration += 1
			print("Solve iteration", iteration)
			changed = False
			#Add checks for unique possible numbers within a 3x3 cell, row, and column
			for row in range(self.HEIGHT):
				for col in range(self.WIDTH):
					if len(self.board_options[row][col]) == 1 \
					and self.board[row][col] == 0:
						num = list(self.board_options[row][col])[0]
						#print("\n\n" + str(num) + "\n\n") #for debugging
						self.update_board_options(row, col, num)
						self.board[row][col] = num
						changed = True
			for row in range(self.HEIGHT):
				for col in range(self.WIDTH):
					if 
		print()

if __name__ == "__main__":
	B = Board()
	B.print_board()
	
	location = [[0, 6, 4], [0, 7, 1], [0, 8, 2], [1, 4, 9], [1, 5, 8], [1, 8, 3]
			   ,[2, 0, 1], [2, 4, 3], [3, 2, 3], [3, 7, 6], [4, 0, 9], [4, 3, 6]
			   ,[4, 5, 4], [4, 8, 1], [5, 1, 5], [5, 6, 8], [6, 4, 1], [6, 8, 7]
			   ,[7, 0, 3], [7, 3, 2], [7, 4, 5], [8, 0, 2], [8, 1, 8], [8, 2, 6]]
	for item in location:
		B.add_number(*item)
	
	#B.create_board()
	B.print_board()

	B.solve_board()	
	B.print_board()
	B.print_board_options()


