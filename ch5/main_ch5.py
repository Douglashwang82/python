from arrayStack import ArrayStack
from arrayQueue import ArrayQueue
# from caesarCipher import CasesarCipher

# #data section
# msg = "WHEN DO YOU DECIDE TO BECOME STRONG?"
# cipher = CasesarCipher(10)

# #executing section
# print("Origin message: ", msg)
# coded = cipher.encrypt(msg)
# print("Encrypted messge: ", coded)
# decoded = cipher.decrypt(coded)
# print("Decoded message: ", decoded)
# bruforce = cipher._brute_force_cracker(coded)
# print("Brute force cracked: ", bruforce)

# matrix_3d = [[[1,2,3],[2]]]
# print(matrix_3d[0])
# print(matrix_3d[0][0])
# print(matrix_3d[0][0][0])

# a_list = [0]
# print(a_list)

# b_list = [0] * 10
# print(b_list)

# c_list = [[0] *10] * 10
# print(c_list)

# c_list[5][5] = 99
# print(c_list)

# a_stack = ArrayStack()
# a_stack.push(1)
# a_stack.push(2)
# a_stack.push(3)
# print(a_stack.top())
# print(len(a_stack))
# print(a_stack.is_empty())
# a_stack.pop()
# print(len(a_stack))



a_queue = ArrayQueue()

for i in range(10):
	a_queue.enqueue(i)
	print(a_queue._data)

a_queue.dequeue()
a_queue.enqueue(11)
print(a_queue._data)

a_queue.dequeue()

print(a_queue.dequeue())
print(a_queue._data)