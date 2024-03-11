import utils


# ofb encryption
# for each text block:
# 	1. encryption of previous encrypted vector (starting with init vector)
# 	2. plain text + encrypted vector
def encrypt(plain_text: str, block_size: int, key: int, init_vector: int):
	cipher_text = ""
	input_vector = init_vector

	text_blocks = utils.split_text_in_blocks(plain_text, block_size)

	for text_block in text_blocks:
		# encryption
		input_text = input_vector
		output_text = utils.block_cipher_encryption(key, input_text)

		# post encryption
		input_vector = output_text
		xor_text = text_block ^ output_text
		cipher_text += utils.string_to_binary(xor_text, block_size)

	return cipher_text[0:len(plain_text)]


# ofb decryption
# uses encryption with the cipher text instead of the plain text
def decrypt(cipher_text: str, block_size: int, key: int, init_vector: int):
	return encrypt(cipher_text, block_size, key, init_vector)
