from arrayStack import ArrayStack

def is_matched(expr):
	"""Return True if all delimiters are properly match. False otherwise"""
	lefty = '({['	# opening delimiters
	righty = ')}]'	# respetive closing delims
	S = ArrayStack()
	for c in expr:
		if c in lefty:
			S.push(c)	# push left delimiter on stack
		elif c in righty:
			if S.is_empty():
				return False
			if righty.index(c) != lefty.index(S.pop()):
				return False
	return S.is_empty()

def is_matched_html(raw):
	"""Return True if all HTML tags are properly match; False otherwise."""
	S = ArrayStack()
	j = raw.find('<')		# find the first '<' character if any.
	while j!= -1:
		k = raw.find('>', j+1)		# find the next '>' character
		if k == -1:					
			return False			# invalid tag
		tag = raw[j+1:k]			# strip away < >
		if not tag.startswith('/'):# this is opening tag
			S.push(tag)
		else:						# this is closing tag
			if S.is_empty():	
				return False		# nothing to match
			if tag[1:] != S.pop():
				return False		# mismatched delimiter
		j = raw.find('<', k + 1)	# find next '<' character (if any)
	return S.is_empty()				# were all opening tags matched?

if __name__ == "__main__":
	html = "<html> </html><body></body>"
	print(is_matched_html(html))
