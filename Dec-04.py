
'''
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.
'''

def CheckOnePassphrase(passphrase):
	words = set()
	for word in passphrase.split():
		if word in words:
			return False
		words.add(word)
	return True

def Solve(passphrase_list):
	return len(filter(CheckOnePassphrase, passphrase_list))

'''
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.
'''
def CheckOnePassphrase2(passphrase):
	words = set()
	for word in passphrase.split():
		sorted_word = ''.join(sorted(word))
		if sorted_word in words:
			return False
		words.add(sorted_word)
	return True

def Solve2(passphrase_list):
	return len(filter(CheckOnePassphrase2, passphrase_list))

if __name__ == "__main__":
	with open('Dec-04.dat') as f:
		passphrase_list = f.read().splitlines()
		print Solve(passphrase_list)
		print Solve2(passphrase_list)

