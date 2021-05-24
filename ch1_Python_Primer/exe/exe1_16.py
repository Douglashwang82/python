def scale(data,factor):
	for j in range(len(data)):
		data[j] *= factor

# This doesnt change the state of the object
def scale2(data,factor):
	for val in data:
		val *= factor
		

# a list with 1,2,3,4....19
a_list = [i for i in range(20)]


# multuple elements by factor
scale(a_list,2)

# doesnt work
scale2(a_list,2)
print(a_list)

# try on comp, this work
b_list = [i*2 for i in a_list]

print(b_list)