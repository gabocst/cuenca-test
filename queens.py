class Nqueens:
	def __init__(self, N):
		self.N = N
		self.solutions = 0

	# This function check if a queen can be placed in one position
	def is_valid(self, board, k): 
		for i in range(k):
			if board[i] == board[k] or abs(board[i] - board[k]) == abs(i - k):
				return False
		return True

	def find_solution(self, board, k): 
		# base case: If all queens are placed, count one more solution and then return true 
		if k >= self.N: 
			self.solutions = self.solutions + 1
			return True
		success = False
		board[k] = 0
		for row in range(self.N): 
			# Place this queen in board[k]
			board[k] = board[k] + 1
			if self.is_valid(board, k): 
				if k != self.N:
					# try put next queen on board
					success = self.find_solution(board, k+1) or success
				else:
					success = True
		return success

	# This function solves the N Queen problem using Backtracking
	def solve_n_queens(self): 
		k = 0
		board = [0] * self.N
		if self.find_solution(board, k) == False: 
			print("There is not solution for this N")
			return False
		print(self.solutions)
		return True


def main():
	N = int(input("Select N: "))
	queen = Nqueens(N)
	queen.solve_n_queens()

if __name__ == '__main__':
	main()