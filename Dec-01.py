
'''
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.
'''
def Solve(string):
	return sum([ int(value) for i, value in enumerate(string) if value == string[i-1] ])


'''
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.
'''
def Solve2(string):
	return sum([ int(value) for i, value in enumerate(string) if value == string[i-len(string)/2] ])


if __name__ == "__main__":
	with open('Dec-01.dat') as f:
		string = f.read()
		print Solve(string)
		print Solve2(string)
