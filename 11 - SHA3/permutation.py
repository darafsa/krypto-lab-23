
# rotation[i][j]
rotation = [[0, 1, 62, 28, 27],
            [36, 44, 6, 55, 20],
            [3, 10, 43, 25, 39],
            [41, 45, 15, 21, 8],
            [18, 2, 61, 56, 14]]

round_constants = [
	"0000000000000001",
	"0000000000008082",
	"800000000000808A",
	"8000000080008000",
	"000000000000808B",
	"0000000080000001",
	"8000000080008081",
	"8000000000008009",
	"000000000000008A",
	"0000000000000088",
	"0000000080008009",
	"000000008000000A",
	"000000008000808B",
	"800000000000008B",
	"8000000000008089",
	"8000000000008003",
	"8000000000008002",
	"8000000000000080",
	"000000000000800A",
	"800000008000000A",
	"8000000080008081",
	"8000000000008080",
	"0000000080000001",
	"8000000080008008"]

# convert constants to little endian
round_constants = [format(int(constant, 16), 'b').zfill(64)[::-1]
                   for constant in round_constants]


# element links oben: a[0][0][63]
# element links unten: a[4][0][63]
# element rechts unten: a[4][4][0]
# element rechts oben: a[0][4][0]

# returns the strided index of the array
def get_index(i: int, j: int, k: int):
	return 64 * 5 * (i % 4) + 64 * (j % 4) + (63 - (k % 64))


# returns a block at position i, j
def get_block(data: str, i: int, j: int):
	return data[get_index(i, j, 0):get_index(i, j, 0) + 64]


# bitwise xor for the entire input string
def __xor(a: str, b: str):
	# make the strings the same length
	a = a.ljust(len(b), "0")
	b = b.ljust(len(a), "0")
	return "".join(str(int(a[i] != b[i])) for i in range(len(a)))


# bitwise and for the entire input string
def __and(a: str, b: str):
	a = a.ljust(len(b), "0")
	b = b.ljust(len(a), "0")
	return "".join(str(int(int(a[i]) + int(b[i]) == 2)) for i in range(len(a)))


# bitwise negation for the entire input string
def __not(a: str):
	return "".join(str(int(a[i] == "0")) for i in range(len(a)))


# permutation function
def f(data: str):
	for r in range(24):
		data = theta(data)
		data = rho(data)
		data = pi(data)
		data = chi(data)
		data = iota(data, r)
	return data


# calculates the parity of a given column
def parity(data: str, j: int, k: int):
	return str(sum([int(data[get_index(i, j, k)]) for i in range(5)]) % 2)


# combines (xor) a column with the parity of the left and right column
def theta(data: str):
	new_data = ""
	for i in range(5):
		for j in range(5):
			for k in range(64):
				bit = __xor(data[get_index(i, j, k)], parity(data, j - 1, k))
				bit = __xor(bit, parity(data, j + 1, k - 1))
				new_data += bit
	return new_data


# cyclical rotation of the individual blocks
def rho(data: str):
	new_data = ""
	for i in range(5):
		for j in range(5):
			block = get_block(data, i, j)
			new_data += block[64 - rotation[i][j]:] + block[:64 - rotation[i][j]]
	return new_data


# rotation of each word
def pi(data: str):
	new_data = ""
	for i in range(5):
		for j in range(5):
			block = get_block(data, j, 3 * i + j)
			new_data += block
	return new_data


# non-linear function for mixing columns
def chi(data: str):
	new_data = ""
	for i in range(5):
		for j in range(5):
			new_block = __not(get_block(data, i, j + 1))
			new_block = __and(new_block, get_block(data, i, j + 2))
			new_block = __xor(new_block, get_block(data, i, j))
			new_data += new_block
	return new_data


# adds constants to first block
def iota(data: str, r: int):
	return __xor(get_block(data, 0, 0), round_constants[r]) + data[64:]
