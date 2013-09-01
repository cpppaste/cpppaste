class Hasher:
	@staticmethod
	def getPolinomialHash(string, power = 256, mod = 2**128):
		result = 0
		for character in string:
			result = (result * power + ord(character)) % mod
		return result