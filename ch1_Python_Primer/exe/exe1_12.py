import random

def own_choice(a_list):
	return a_list[random.randrange(0,len(a_list))]


l = [i for i in range(10)]

print(own_choice(l))