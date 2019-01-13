from queens import Nqueens

number_of_solutions = [92, 352, 724, 2680, 14200]

class TestNQueens(object):
    def test_one(self):
        for n in range(8,13):
            queen = Nqueens(n)
            assert queen.solve_n_queens() == number_of_solutions[n-8]