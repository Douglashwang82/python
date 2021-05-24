# Function beyound_sum()
# return the sum of numbers smaller than n

def beyound_sum(n):
	results = 0
	for number in range(0, n):
		results += number**2
	return results

if __name__ == "__main__":
	print("Test:n = 100 ",beyound_sum(100))
	print("Test:n = 10 ",beyound_sum(10))
	print("Test:n = 4",beyound_sum(4))


