#funtion is_even()
#True, n is even
#Cannot use modulo division operators.

def is_even(n):
	b = bin(n)
	return True if b[-1] == "0" else False

if __name__ == "__main__":
	#Testing
	print("Test 3",is_even(3))
	print("Test 122",is_even(122))

