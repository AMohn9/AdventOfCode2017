
'''
The message includes a list of the offsets for each jump. Jumps are relative: -1 moves to the previous instruction, and 2 skips the next one. Start at the first instruction in the list. The goal is to follow the jumps until one leads outside the list.

In addition, these instructions are a little strange; after each jump, the offset of that instruction increases by 1. So, if you come across an offset of 3, you would move three instructions forward, but change it to a 4 for the next time it is encountered.
'''
from copy import copy

def Solve(lst):
	place = 0
	counter = 0
	while place >= 0 and place < len(lst):
		counter += 1
		lst[place] += 1
		place += lst[place] - 1
	return counter

'''
Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.
'''
def Solve2(lst):
	place = 0
	counter = 0
	while place >= 0 and place < len(lst):
		counter += 1
		if lst[place] >= 3:
			lst[place] -= 1
			place += lst[place] + 1
		else:
			lst[place] += 1
			place += lst[place] - 1
	print lst
	return counter


if __name__ == "__main__":
	with open('Dec-05.dat') as f:
		lst = [int(x) for x in f.read().splitlines()]
		print Solve(copy(lst))
		print Solve2(copy(lst))
		