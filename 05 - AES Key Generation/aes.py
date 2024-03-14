import utils
import arithmetic
import input_handler


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
		output_data[i:16:4] = utils.shift_array(data[i:16:4], -i)
	return output_data


# moves each line i steps to the right
def shift_rows_inv(data: list):
	output_data = [None] * len(data)
	for i in range(4):
		output_data[i:16:4] = utils.shift_array(data[i:16:4], i)
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
		i_start = i * 4
		i_end = (i + 1) * 4
		output_data[i_start:i_end] = arithmetic.matrix_mult(m, data[i_start:i_end])

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
		i_start = i * 4
		i_end = (i + 1) * 4
		output_data[i_start:i_end] = arithmetic.matrix_mult(m, data[i_start:i_end])
	return output_data


# rotates a word to the left
def rot_word(word: list):
	return utils.shift_array(word, -1)


# substitutes a word with the entries from SBox
def sub_word(word: list, sbox: list):
	return sub_bytes(word, sbox)


# word addition in galois field (^)
def add_words(word1: list, word2: list):
	output_word = [None] * len(word1)
	for i in range(len(word1)):
		output_word[i] = word1[i] ^ word2[i]
	return output_word


# generates 11 128-bit round keys for the AES standard
def generate_round_keys(key_data: str):
	rcon = [[rc, 0, 0, 0] for rc in [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54]]

	key = utils.split_data_in_blocks(key_data, 128)[0]
	sbox_data = input_handler.read_file("res/SBox.txt")
	sbox = utils.split_data_in_blocks(sbox_data, 128 * 16)[0]
	words = [[None]] * 44

	for i in range(4):
		words[i] = [key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]]

	for i in range(4, 44):
		tmp = words[i - 1]
		if i % 4 == 0:
			tmp = add_words(sub_word(rot_word(tmp), sbox), rcon[i // 4])
		words[i] = add_words(words[i - 4], tmp)

	round_keys = []
	for i in range(11):
		round_keys.append(words[i * 4] + words[i * 4 + 1] +
		                  words[i * 4 + 2] + words[i * 4 + 3])

	return round_keys


# encrypts 128-bit blocks according to the AES standard
def encrypt_block(block: list, round_keys: list, sbox: list):
	new_block = add_round_key(block, round_keys[0])
	for i in range(1, 10):
		new_block = sub_bytes(new_block, sbox)
		new_block = shift_rows(new_block)
		new_block = mix_columns(new_block)
		new_block = add_round_key(new_block, round_keys[i])
	new_block = sub_bytes(new_block, sbox)
	new_block = shift_rows(new_block)
	new_block = add_round_key(new_block, round_keys[10])

	return new_block


# decrypts 128-bit blocks according to the AES standard
def decrypt_block(block: list, round_keys: list, sbox: list):
	new_block = add_round_key(block, round_keys[10])
	new_block = shift_rows_inv(new_block)
	new_block = sub_bytes(new_block, sbox)
	for i in range(9, 0, -1):
		new_block = add_round_key(new_block, round_keys[i])
		new_block = mix_columns_inv(new_block)
		new_block = shift_rows_inv(new_block)
		new_block = sub_bytes(new_block, sbox)
	new_block = add_round_key(new_block, round_keys[0])

	return new_block
