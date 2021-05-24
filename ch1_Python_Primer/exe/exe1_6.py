def beyound_old_sum(n):
	result = 0
	for i in range(1,n,2):
		result+= i
		print(i)
	return result

print("Test n = 10",beyound_old_sum(10))