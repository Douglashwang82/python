def are_distinct(a_list):
	length = len(a_list)
	for i in range(length):
		for j in range(i+1,length):
			if a_list[i] == a_list[j]:
				return False
	return True

x_list = [i for i in range(0,100)]
y_list = [1,2,3,4,5,53,3,5,4,3,3,3,2,3,4,3]
z_list = [1,2,1]
h_list = [1]
print(are_distinct(x_list))
print(are_distinct(y_list))
print(are_distinct(z_list))
print(are_distinct(h_list))