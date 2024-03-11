import utils


# ctr encryption
# for each text block:
# 	1. encryption of counting vector
# 	2. plain text + encrypted counting vector
def encrypt(plain_text: str, block_size: int, key: int):
	cipher_text = ""
	init_vector = 0
	counter = 0

	text_blocks = utils.split_text_in_blocks(plain_text, block_size)

	for text_block in text_blocks:
		# pre encryption
		input_text = init_vector + counter
		counter += 1

		# encryption
		output_text = utils.block_cipher_encryption(key, input_text)

		# post encryption
		xor_text = text_block ^ output_text
		cipher_text += utils.string_to_binary(xor_text, block_size)

	return cipher_text[0:len(plain_text)]


# ctr decryption
# uses encryption with the cipher text instead of the plain text
def decrypt(cipher_text: str, block_size: int, key: int):
	return encrypt(cipher_text, block_size, key)
