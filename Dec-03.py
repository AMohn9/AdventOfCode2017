
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

from math import ceil, pow
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

if __name__ == "__main__":
	print Solve(289326)

