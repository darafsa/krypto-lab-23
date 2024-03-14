import utils
import aes


# ctr encryption
# for each text block:
# 	1. encryption of counting vector
# 	2. plain text + encrypted counting vector
def encrypt(data: str, key_data: str, sbox_data: str):
	encrypted_data = []
	round_keys = aes.generate_round_keys(key_data)
	sbox = utils.split_data_in_blocks(sbox_data, 128 * 16)[0]

	init_vector = 0
	counter = 0

	blocks = utils.split_data_in_blocks(data, 128)

	for block in blocks:
		# pre encryption
		input_data = init_vector + counter
		counter += 1

		# encryption
		output_data = aes.encrypt_block(
			utils.int_to_block(input_data, 128), round_keys, sbox)

		# post encryption
		encrypted_data.append(utils.xor_blocks(block, output_data))

	return encrypted_data


# ctr decryption
# uses encryption with the cipher text instead of the plain text
def decrypt(data: str, key_data: str, sbox_data: str):
	return encrypt(data, key_data, sbox_data)
