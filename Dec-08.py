

'''
Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

What is the largest value in any register after completing the instructions in your puzzle input?

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).
'''

import operator
from collections import defaultdict

def Solve(instructions):
	registers = defaultdict(int)
	ops = {
		'<': operator.lt,
		'<=': operator.le,
		'==': operator.eq,
		'!=': operator.ne,
		'>=': operator.ge,
		'>': operator.gt
	}

	highest = 0
	for i in instructions:
		register, command, val, iffy, ref, op, comp_val = i.split()
		val = int(val)
		comp_val = int(comp_val)
		if command == 'dec':
			val *= -1
		operation = ops.get(op)
		if operation(registers[ref], comp_val):
			registers[register] += val
			highest = max(highest, registers[register])

	return max(registers.values()), highest

if __name__ == "__main__":
	with open('Dec-08.dat') as f:
		instructions = f.read().splitlines()
		print Solve(instructions)

