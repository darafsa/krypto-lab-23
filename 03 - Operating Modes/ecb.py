import utils


# ecb encryption
# encrypts each plain text block with the key
def encrypt(plain_text: str, block_size: int, key: int):
	cipher_text = ""

	text_blocks = utils.split_text_in_blocks(plain_text, block_size)

	for text_block in text_blocks:
		output_text = utils.block_cipher_encryption(key, text_block)
		cipher_text += utils.string_to_binary(output_text, block_size)

	return cipher_text[0:len(plain_text)]


# ecb decryption
# decrypts each cipher text block with the key
def decrypt(cipher_text: str, block_size: int, key: int):
	plain_text = ""

	text_blocks = utils.split_text_in_blocks(cipher_text, block_size)

	for text_block in text_blocks:
		output_text = utils.block_cipher_decryption(key, text_block)
		plain_text += utils.string_to_binary(output_text, block_size)

	return plain_text[0:len(cipher_text)]
