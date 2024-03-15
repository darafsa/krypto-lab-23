import random
import permutation

d = 224
r = 1152
c = 448
b = c + r


# appends the string with 10*1 so that it's divisible by r
# then divides it into r large blocks
def pad(string: str):
	padding_length = r - len(string) % r

	if padding_length == 1:
		padding_length += r

	padding = "1" + "0" * (padding_length - 2) + "1"
	string += padding

	return list(map(''.join, zip(*[iter(string)] * r)))


# hashes a given hex string using the sha-3 standard
def hash(data: str):
	# hex to bin and reverse order (little endian)
	data = format(int(data, 16), 'b')[::-1]
	data += "01"
	blocks = pad(data)
	s = "0" * b

	for block in blocks:
		s = permutation.__xor(s, block + "0" * c)
		s = permutation.f(s)

	return format(int(s[:d], 2), 'x')
