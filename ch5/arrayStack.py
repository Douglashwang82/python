class Empty(Exception):
	pass

class ArrayStack:
	"""LIFO Stack implementation using a Python list as underlyinh storage."""

	def __init__(self):
		"""Create an empty stack"""
		self._data = []
	
	def __len__(self):
		"""Return the length of the stack."""
		return len(self._data)

	def push(self, element):
		"""Add a new element into the stack"""
		self._data.append(element)

	def is_empty(self):
		"""Return Ture if the stack is empty."""
		return len(self._data) == 0

	def pop(self):
		"""pop the last element in the stack"""
		if self.is_empty():
			raise Empty("Stack is empty.")
		else:
			return self._data.pop() # Python list has pop() method.

	def top(self):
		"""Access the top of the stack.
		
			Raise exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty("Stack is empty.")
		else:
			return self._data[-1]

