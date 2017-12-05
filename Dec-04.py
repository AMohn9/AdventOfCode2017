
def CheckOnePassphrase(passphrase):
	words = set()
	for word in passphrase.split():
		if word in words:
			return False
		words.add(word)
	return True

def Solve(passphrase_list):
	return len(filter(CheckOnePassphrase, passphrase_list))

if __name__ == "__main__":
	with open('Dec-04.dat') as f:
		passphrase_list = f.read().splitlines()
		print Solve(passphrase_list)