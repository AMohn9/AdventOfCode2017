
'''
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

Using the Manhattan Distance, how many steps are required to carry the data from the square identified in your puzzle input all the way to the center?
'''

from math import ceil, pow, sqrt
def nextSquare(square):
	root = int(ceil(pow(square, .5)))
	if not root % 2:
		root += 1
	return root, root**2


def Solve(square):
	corner_root, corner = nextSquare(square)
	prev_corner = (corner_root - 2)**2

	first_mid = prev_corner + corner_root/2
	jumpsize = corner_root - 1
	middles = [first_mid + i*(jumpsize) for i in xrange(4)]

	closest_middle = min([abs(square - mid) for mid in middles])

	return closest_middle + corner_root/2

'''
As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?
'''
def Solve2(val):
	mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
	row, col = 1, 2
	next_square = 0
	while next_square < val:
		next_square = 0
		# Above
		if row > 0:
			next_square += mat[row-1][col]
			# Above left
			if col > 0:
				next_square += mat[row-1][col-1]
			# Above right
			if col < len(mat) - 1:
				next_square += mat[row-1][col+1]
		# Sides
		if col > 0:
			next_square += mat[row][col-1]
		if col < len(mat) - 1:
			next_square += mat[row][col+1]

		# Below
		if row < len(mat) - 1:
			next_square += mat[row+1][col]
			# Below left
			if col > 0:
				next_square += mat[row+1][col-1]
			# Below right
			if col < len(mat) - 1:
				next_square += mat[row+1][col+1]
		mat[row][col] = next_square

		# Move to next square
		if row == 0:
			if col == 0:
				row += 1
			else:
				col -= 1
		elif col == 0:
			if row == len(mat)-1:
				col += 1
			else:
				row += 1
		elif row == len(mat)-1:
			if col == len(mat)-1:
				# Grow mat
				for r in mat:
					r.insert(0, 0)
					r.append(0)
				mat.insert(0, [0]*(len(mat)+2))
				mat.append([0]*(len(mat)+2))
				row += 1
				col += 2
			else:
				col += 1
		elif col == len(mat)-1:
			row -= 1
		else:
			print "BAD BAD BAD", row, col
			exit()
	return next_square



if __name__ == "__main__":
	print Solve(289326)
	print Solve2(289326)

