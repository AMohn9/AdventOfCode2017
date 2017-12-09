
'''
You sit for a while and record part of the stream (your puzzle input). The characters represent groups - sequences that begin with { and end with }. Within a group, there are zero or more other things, separated by commas: either another group or garbage. Since groups can contain other groups, a } only closes the most-recently-opened unclosed group - that is, they are nestable. Your puzzle input represents a single, large group which itself contains many smaller ones.

Sometimes, instead of a group, you will find garbage. Garbage begins with < and ends with >. Between those angle brackets, almost any character can appear, including { and }. Within garbage, < has no special meaning.

In a futile attempt to clean up the garbage, some program has canceled some of the characters within it using !: inside garbage, any character that comes after ! should be ignored, including <, >, and even another !.

You don't see any characters that deviate from these rules. Outside garbage, you only find well-formed groups, and garbage always terminates according to the rules above.

Your goal is to find the total score for all groups in your input. Each group is assigned a score which is one more than the score of the group that immediately contains it. (The outermost group gets a score of 1.)

Additionally, to prove you've removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.
'''

import re

def RemoveCanceled(stream):
	p = re.compile('(!.)')
	return p.sub('', stream)

def RemoveGarbage(stream):
	p = re.compile('(<.*?>)')
	return p.subn('', stream)

def Solve(stream):
	stream = RemoveCanceled(stream)
	orig = stream
	stream, replaced = RemoveGarbage(stream)

	depth = 1
	score = 0
	for character in stream:
		if character == '{':
			score += depth
			depth += 1
		elif character == '}':
			depth -= 1
	return score, len(orig) - len(stream) - replaced * 2

depth = lambda L: isinstance(L, list) and sum(map(depth, L))+1
print depth([[[],[],[[]]]])

# if __name__ == "__main__":
# 	with open('Dec-09.dat') as f:
# 		stream = f.read()
# 		print Solve(stream)


