''' Finding a maximum elements in a given S'''
import random 
S  = [random.randint(0,1000) for _ in range(1000)]

def find_maximum(S, n):
	if n == 1:
		return S[0]
	else:
		return max(S[0],find_maximum(S, n -1))

# print(find_maximum(S, len(S)))


#Long Version

def find_maximum_long_version(S):
	length = len(S)
	if length == 0:
		return False
	def _find_maximum(S,n,current):
		if n == 0:
			return S[0]
		else:
			if S[n] > current:
				return _find_maximum(S, n-1, S[n])
			else:
				return _find_maximum(S, n-1, current)
	cur = S[0]
	return _find_maximum(S,length - 1, cur)

# print(find_maximum_long_version(S))


# This still break the python intepretor. Maximum depth violation.
def last_element(n):
	if n == 1:
		return S[0]
	else:
		return last_element(n-1)
print(last_element(len(S)))

