#function minmax()
# return min and max of a sequence

def minmax(seq):
	min, max = seq[0], seq[0]
	for number in seq:
		min = number if number < min else min
		max = number if number > max else max
	return min, max

if __name__ == "__main__":
	print("Test:[1,2,3]",minmax([1,2,3]))
	print("Test:[4,5,6,3,2,1,31,-1,-2,10,11]",minmax([4,5,6,3,2,1,31,-1,-2,10,11]))
