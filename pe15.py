"""Lattice paths"""

def memoization(n=20, m=20):

	def count_routes(m,n):
		if n == 0 or m == 0:
			return 1
		elif (m,n) in path_dict:
			return path_dict[(m,n)]
		else:
			path_dict[(m,n)] = count_routes(m,n-1) + count_routes(m-1,n)
			return path_dict[(m,n)]

	global path_dict
	path_dict = {}
	print(count_routes(20,20))

	

def Combinations(n=40, r=20):
	from math import factorial
	print(factorial(n) / (factorial(r) * factorial(n-r)))


def dynamic_programming(m=20, n=20):
	grid = [[0 for _ in range(m)] for _ in range(n)]

	for i in range(m):
		grid[i][0] = 1

	for j in range(n):
		grid[0][j] = 1

	for i in range(1, m+1):
		for j in range(1, n+1):
			grid[i][j] = grid[i-1][j] + grid[i][j-1]

	print(grid[m][n])


if __name__ == '__main__':
	#Combinations()
	#memoization()
	dynamic_programming()