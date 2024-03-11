import utils


# cbc encryption
# for each text block:
# 	1. xor text = plain text + previous encription output (salt)
# 	2. encryption of xor text
def encrypt(plain_text: str, block_size: int, key: int):
	cipher_text = ""
	init_vector = 0
	salt = init_vector

	text_blocks = utils.split_text_in_blocks(plain_text, block_size)

	for text_block in text_blocks:
		# pre encryption
		xor_text = text_block ^ salt

		# encryption
		input_text = xor_text
		output_text = utils.block_cipher_encryption(key, input_text)

		# post encryption
		salt = output_text
		cipher_text += utils.string_to_binary(output_text, block_size)

	return cipher_text[0:len(plain_text)]


# cbc decryption
# for each text block:
# 	1. decription of encrypted text
# 	2. decrypted text + previous encrypted text (salt)
def decrypt(cipher_text: str, block_size: int, key: int):
	plain_text = ""
	init_vector = 0
	salt = init_vector

	text_blocks = utils.split_text_in_blocks(cipher_text, block_size)

	for text_block in text_blocks:
		# decryption
		input_text = text_block
		output_text = utils.block_cipher_decryption(key, input_text)

		# post decryption
		xor_text = output_text ^ salt
		plain_text += utils.string_to_binary(xor_text, block_size)

		# 'pre' decryption (uses pre decryption text but has to happen after salt has been used in post decryption)
		salt = text_block

	return plain_text[0:len(cipher_text)]
