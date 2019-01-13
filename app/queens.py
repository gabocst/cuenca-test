from database import Queen, BoardSolution, session

class Nqueens:
	def __init__(self, N):
		self.N = N
		self.solutions = 0

	def saveSolution(self, board):
		str_solution = str(board).strip('[]')
		str_solution = str_solution.replace(' ', '')
		q = session.query(Queen).filter_by(n=self.N)
		for x in q:
			queen_id = x.id
		board_solution = BoardSolution(board=str_solution, queen_id=queen_id)  
		session.add(board_solution)  
		session.commit()

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
			self.saveSolution(board)
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
		q = session.query(Queen).filter_by(n=self.N)
		number_of_solutions = -1
		for x in q:
			number_of_solutions = x.number_of_solutions
		if number_of_solutions != -1:
			print("Number of solutions: ", number_of_solutions)
		else:
			k = 0
			board = [0] * self.N
			queen = Queen(n=self.N, number_of_solutions=0)  
			session.add(queen)  
			session.commit()
			if self.find_solution(board, k) == False: 
				print("There is not solution for this N")
				return False
			print("Number of solutions: ", self.solutions)
			queen.number_of_solutions = self.solutions
			session.commit()
		return True


def main():
	N = int(input("Select size of the board: "))
	queen = Nqueens(N)
	queen.solve_n_queens()

if __name__ == '__main__':
	main()