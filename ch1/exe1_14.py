def odd_pair(i_list):
	count = 0
	for i in i_list:
		number = bin(i)
		if number[-1] == "1":
			count += 1
	if count > 1:
		return True
	return False


a_list = [1,2,3,4,5,6,7,8,9,10]
b_list = [i for i in range(0,20,2)]


print(odd_pair(a_list))
print(odd_pair(b_list))