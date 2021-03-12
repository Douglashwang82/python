# Find the interger part of a base-2 log of n.

def log_2(n):
	if n < 2:
		return 0
	else:
		return 1 + log_2(n//2)

print(log_2(1023))