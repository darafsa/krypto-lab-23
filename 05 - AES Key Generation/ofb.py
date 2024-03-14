import utils
import aes


# ofb encryption
# for each text block:
# 	1. encryption of previous encrypted vector (starting with init vector)
# 	2. plain text + encrypted vector
def encrypt(data: str, key_data: str, sbox_data: str, init_vector_data: str):
	encrypted_data = []
	round_keys = aes.generate_round_keys(key_data)
	sbox = utils.split_data_in_blocks(sbox_data, 128 * 16)[0]
	input_vector = utils.split_data_in_blocks(init_vector_data, 128)[0]

	blocks = utils.split_data_in_blocks(data, 128)

	for block in blocks:
		# encryption
		input_data = input_vector
		output_data = aes.encrypt_block(input_data, round_keys, sbox)

		# post encryption
		input_vector = output_data
		xor_data = utils.xor_blocks(block, output_data)
		encrypted_data.append(xor_data)

	return encrypted_data


# ofb decryption
# uses encryption with the cipher text instead of the plain text
def decrypt(data: str, key_data: str, sbox_data: str, init_vector_data: str):
	return encrypt(data, key_data, sbox_data, init_vector_data)
