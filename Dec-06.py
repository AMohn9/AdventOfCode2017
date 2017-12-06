
'''
In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. The goal of the reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks (ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks. It continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is produced that has been seen before.

Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already been seen, how many block redistribution cycles must be performed before that same state is seen again?'
'''

def Solve(lst):
	states = dict()
	state_num = 0
	while repr(lst) not in states:
		states[repr(lst)] = state_num
		state_num += 1
		index = max(xrange(len(lst)), key=lst.__getitem__)
		to_redistribute = lst[index]
		lst[index] = 0
		for i in xrange(to_redistribute):
			index = (index + 1) % len(lst)
			lst[index] += 1
	return state_num, state_num - states[repr(lst)]

if __name__ == "__main__":
	with open('Dec-06.dat') as f:
	 	lst = [int(x) for x in f.read().split()]
	 	print Solve(lst)