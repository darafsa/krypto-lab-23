import aes_keygen
import utils


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
	output_data = [None] * len(data)
	for byte in range(len(data)):
		output_data[byte] = data[byte] ^ key[byte]
	return output_data


# substitutes each byte with the corresponding byte of the sbox
def sub_bytes(data: list, sbox: list):
	output_data = [None] * len(data)
	for byte in range(len(data)):
		output_data[byte] = sbox[data[byte]]
	return output_data


# moves each line i steps to the left
def shift_rows(data: list):
	output_data = [None] * len(data)
	for i in range(4):
		output_data[i:16:4] = shift_array(data[i:16:4], -i)
	return output_data


# moves each line i steps to the right
def shift_rows_inv(data: list):
	output_data = [None] * len(data)
	for i in range(4):
		output_data[i:16:4] = shift_array(data[i:16:4], i)
	return output_data


# mixes the columns of the data
def mix_columns(data: list):
	output_data = [None] * len(data)
	m = [
		2, 3, 1, 1,
		1, 2, 3, 1,
		1, 1, 2, 3,
		3, 1, 1, 2]

	for i in range(4):
		output_data[i * 4:(i + 1) * 4] = matrix_mult_vec(m, data[i * 4:(i + 1) * 4])
	return output_data


# mixes the columns of the data inversely
def mix_columns_inv(data: list):
	output_data = [None] * len(data)
	m = [
		14, 11, 13, 9,
		9, 14, 11, 13,
		13, 9, 14, 11,
		11, 13, 9, 14]

	for i in range(4):
		output_data[i * 4:(i + 1) * 4] = matrix_mult_vec(m, data[i * 4:(i + 1) * 4])
	return output_data


# encrypts 128-bit blocks according to the AES standard
def encrypt(data: str, key_data: str, sbox_data: str):
	blocks = utils.split_data_in_blocks(data, 128)
	round_keys = aes_keygen.generate_round_keys(key_data, sbox_data)
	sbox = utils.split_data_in_blocks(sbox_data, 128 * 16)[0]

	new_blocks = []
	for block in blocks:
		new_block = add_round_key(block, round_keys[0])
		for i in range(1, 10):
			new_block = sub_bytes(new_block, sbox)
			new_block = shift_rows(new_block)
			new_block = mix_columns(new_block)
			new_block = add_round_key(new_block, round_keys[i])
		new_block = sub_bytes(new_block, sbox)
		new_block = shift_rows(new_block)
		new_block = add_round_key(new_block, round_keys[10])
		new_blocks.append(new_block)

	return "\n".join(" ".join(format(byte, "x").zfill(2) for byte in block) for block in new_blocks)


# decrypts 128-bit blocks according to the AES standard
def decrypt(data: str, key: str, sbox_data: str):
	blocks = utils.split_data_in_blocks(data, 128)
	round_keys = utils.split_data_in_blocks(key, 128)
	sbox = utils.split_data_in_blocks(sbox_data, 128 * 16)[0]

	new_blocks = []
	for block in blocks:
		new_block = add_round_key(block, round_keys[10])
		new_block = shift_rows_inv(new_block)
		new_block = sub_bytes(new_block, sbox)
		for i in range(9, 0, -1):
			new_block = add_round_key(new_block, round_keys[i])
			new_block = mix_columns_inv(new_block)
			new_block = shift_rows_inv(new_block)
			new_block = sub_bytes(new_block, sbox)
		new_block = add_round_key(new_block, round_keys[0])
		new_blocks.append(new_block)

	return "\n".join(" ".join(format(byte, "x").zfill(2) for byte in block) for block in new_blocks)
