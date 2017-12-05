
'''
The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.
'''
def DiffLine(line):
	vals = [int(val) for val in line.split()]
	return max(vals) - min(vals)

def Solve(sheet):
	return sum( map(DiffLine, sheet.splitlines()) )

'''
It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.
'''
from itertools import combinations
def SolveLine(line):
	vals = [int(val) for val in line.split()]

	for val1, val2 in combinations(vals, 2):
		if not val1 % val2:
			return val1 / val2
		elif not val2 % val1:
			return val2 / val1

def Solve2(sheet):
	return sum( map(SolveLine, sheet.splitlines()) )


if __name__ == "__main__":
	with open('Dec-02.dat') as f:
		sheet = f.read()
		print Solve(sheet)
		print Solve2(sheet)