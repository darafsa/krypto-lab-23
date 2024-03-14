
# splits given data into smaller blocks which each are split into bytes
def split_data_in_blocks(data: str, block_size: int):
	# size of the block in hex format; e.g. 128 bit -> 32 hex letters
	block_hex_size = int(block_size / 4)
	# data is split into text blocks of 128 bit
	blocks = [data[i:i + block_hex_size].ljust(block_hex_size, '0')
           for i in range(0, len(data), block_hex_size)]
	# each text block is then split into its hex bytes and is then converted into integers
	byte_blocks = [[int(block[byte:byte + 2], 16)
                 for byte in range(0, len(block), 2)] for block in blocks]
	return byte_blocks


# doubles a number by cycling to the left; stays in mod 8
def byte_double(a: int):
	bits = format(a, 'b').zfill(8)
	bits = bits[len(bits) - 8:len(bits)]
	t = (a << 1) % 2**8
	if bits[0] != '0':
		return t ^ int("1b", 16)
	return t


# multiplicates two numbers by using russian pawn multiplication
def mult(a: int, b: int):
	start_sum = b if a % 2 != 0 else 0
	return mult_rek(a, b, start_sum)


# recursive implementation of russion pawn multiplication
def mult_rek(a: int, b: int, sum: int):
	if a <= 1:
		return sum
	a //= 2
	b = byte_double(b)

	if a % 2 != 0:
		sum = sum ^ b

	return mult_rek(a, b, sum)


# matrix multiplication in galois field
def matrix_mult_vec(matrix: list, vector: list):
	output_vec = [0] * 4
	for i in range(4):
		row = matrix[i * 4:(i + 1) * 4]
		output_vec[i] ^= mult(row[0], vector[0])
		output_vec[i] ^= mult(row[1], vector[1])
		output_vec[i] ^= mult(row[2], vector[2])
		output_vec[i] ^= mult(row[3], vector[3])
	return output_vec


# shifts array by n steps
def shift_array(data: list, n: int):
	return data[-n:] + data[:-n]


# xors round key to data
def add_round_key(data: list, key: list):
	for byte in range(len(data)):
		data[byte] ^= key[byte]


# substitutes each byte with the corresponding byte of the sbox
def sub_bytes(data: list, sbox: list):
	for byte in range(len(data)):
		data[byte] = sbox[data[byte]]


# moves each line i steps to the left
def shift_rows(data: list):
	# new_data = [None] * len(data)
	for i in range(4):
		data[i:16:4] = shift_array(data[i:16:4], -i)
	# for i in range(len(data)):
	# 	data[i] = new_data[i]


# moves each line i steps to the right
def shift_rows_inv(data: list):
	for i in range(4):
		data[i:16:4] = shift_array(data[i:16:4], i)


# mixes the columns of the data
def mix_columns(data: list):
	m = [
		2, 3, 1, 1,
		1, 2, 3, 1,
		1, 1, 2, 3,
		3, 1, 1, 2]

	for i in range(4):
		data[i * 4:(i + 1) * 4] = matrix_mult_vec(m, data[i * 4:(i + 1) * 4])


# mixes the columns of the data inversely
def mix_columns_inv(data: list):
	m = [
		14, 11, 13, 9,
		9, 14, 11, 13,
		13, 9, 14, 11,
		11, 13, 9, 14]

	for i in range(4):
		data[i * 4:(i + 1) * 4] = matrix_mult_vec(m, data[i * 4:(i + 1) * 4])


# encrypts 128-bit blocks according to the AES standard
def encrypt(data: str, key: str, sbox_data: str):
	blocks = split_data_in_blocks(data, 128)
	round_keys = split_data_in_blocks(key, 128)
	sbox = split_data_in_blocks(sbox_data, 128 * 16)[0]

	for block in blocks:
		add_round_key(block, round_keys[0])
		for i in range(1, 10):
			sub_bytes(block, sbox)
			shift_rows(block)
			mix_columns(block)
			add_round_key(block, round_keys[i])
		sub_bytes(block, sbox)
		shift_rows(block)
		add_round_key(block, round_keys[10])

	return "\n".join(" ".join(format(byte, "x").zfill(2) for byte in block) for block in blocks)


# decrypts 128-bit blocks according to the AES standard
def decrypt(data: str, key: str, sbox_data: str):
	blocks = split_data_in_blocks(data, 128)
	round_keys = split_data_in_blocks(key, 128)
	sbox = split_data_in_blocks(sbox_data, 128 * 16)[0]

	for block in blocks:
		add_round_key(block, round_keys[10])
		shift_rows_inv(block)
		sub_bytes(block, sbox)
		for i in range(9, 0, -1):
			add_round_key(block, round_keys[i])
			mix_columns_inv(block)
			shift_rows_inv(block)
			sub_bytes(block, sbox)
		add_round_key(block, round_keys[0])

	return "\n".join(" ".join(format(byte, "x").zfill(2) for byte in block) for block in blocks)
