class CasesarCipher:
	"""Class for doing encryption and decryption using a Caesar cipher."""

	def __init__(self, shift):
		"""Construct Caesar cipher using given integer shift for rotation"""
		encoder = [None] * 26				# temp array for encryption
		decoder = [None] * 26				# temp array for decryption
		for k in range(26):
			encoder[k] = chr((k + shift) % 26 + ord('A'))
			decoder[k] = chr((k - shift) % 26 + ord('A'))
		self._forward = ''.join(encoder)	# will store as string
		self._backward = ''.join(decoder)	# since fixed

	def encrypt(self, message):
		"""Return string representing encrypted message"""
		return self._transform(message, self._forward)

	def decrypt(self, secret):
		"""Return decrypted message given encrypted secret."""
		return self._transform(secret, self._backward)

	def _transform(self, origin, code):
		"""Utility to perform transformation based on given code string"""
		msg = list(origin)
		for k in range(len(msg)):
			if msg[k].isupper():
				j = ord(msg[k]) - ord('A')
				msg[k] = code[j]
		return ''.join(msg)

	def _brute_force_cracker(self, secret):
		"""Brute force cracker for 26 possibiles"""
		msg = list(secret)
		cracker = [None] * 26
		for i in range(26):
			for k in range(26):
				cracker[k] = chr((k + i) % 26 + ord('A'))
			temp = self._transform(msg, ''.join(cracker))
			print("Troughly apporach: ",temp)

if __name__ == '__main__':
	cipher = CasesarCipher(3)
	message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
	coded = cipher.encrypt(message)
	print('Secret: ', coded)
	answer = cipher.decrypt(coded)
	print('Message: ',answer)
	cipher._brute_force_cracker(coded)
