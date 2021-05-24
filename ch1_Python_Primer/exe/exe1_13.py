# Pseudo code Reversing a list
# Input:reverse(n)
# 	k = -1
# 	for i in range(len(n)//2):
#		n[i], n[k] = n[k],n[i]
#		k -= 1

a_list = [1,2,3,4,5]
b_list = [1,2,3,4]

def reverse(x_list):
	k = -1
	for i in range(len(x_list)//2):
		x_list[i], x_list[k] = x_list[k],x_list[i]
		k -= 1

print(a_list)
reverse(a_list)
print(a_list)

print(b_list)
reverse(b_list)
print(b_list)