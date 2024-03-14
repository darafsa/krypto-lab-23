import utils
import aes


# cbc encryption
# for each text block:
# 	1. xor text = plain text + previous encription output (salt)
# 	2. encryption of xor text
def encrypt(data: str, key_data: str, sbox_data: str):
	encrypted_data = []
	round_keys = aes.generate_round_keys(key_data)
	sbox = utils.split_data_in_blocks(sbox_data, 128 * 16)[0]

	init_vector = [0] * (128 // 8)
	salt = init_vector

	blocks = utils.split_data_in_blocks(data, 128)

	for block in blocks:
		# encryption
		input_data = utils.xor_blocks(block, salt)
		output_data = aes.encrypt_block(input_data, round_keys, sbox)

		# post encryption
		salt = output_data
		encrypted_data.append(output_data)

	return encrypted_data


# cbc decryption
# for each text block:
# 	1. decription of encrypted text
# 	2. decrypted text + previous encrypted text (salt)
def decrypt(data: str, key_data: str, sbox_data: str):
	decrypted_data = []
	round_keys = aes.generate_round_keys(key_data)
	sbox = utils.split_data_in_blocks(sbox_data, 128 * 16)[0]

	init_vector = [0] * (128 // 8)
	salt = init_vector

	blocks = utils.split_data_in_blocks(data, 128)

	for block in blocks:
		# decryption
		output_data = aes.decrypt_block(block, round_keys, sbox)

		# post decryption
		xor_data = utils.xor_blocks(output_data, salt)
		decrypted_data.append(xor_data)

		# 'pre' decryption (uses pre decryption text but has to happen after salt has been used in post decryption)
		salt = block

	return decrypted_data
