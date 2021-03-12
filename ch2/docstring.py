#Dcoumnetation example

def foo():
	"""Single line docstring"""
	print("Hello World")

def foo_second():
	"""Multiple Docstring

	data:
	
	factors:
	"""
	for _ in range(10):
		print("Hello Ten Times.")


# raise TypeError("Example error")


print("After raise")

class foos(object):
	"""docstring for foos"""
	def __init__(self, arg):
		super(foos, self).__init__()
		self.arg = arg
	def __add__(self, b):
		self.arg = self.arg - b


f1 = foos(10)
f2 = foos(20)
f1 + f2.arg
print(f1.arg)


