# function is_multiple(n, m)
# True, if n is a multiple of m.
# n = mi for exist integer i.

def is_multiple(n, m):
	return (n % m == 0)


if __name__ == "__main__":
	n = 39
	m = 13
	print("Testing exe1-1: n = {}, m = {}, result = {}".format(n,m,is_multiple(n,m)))
