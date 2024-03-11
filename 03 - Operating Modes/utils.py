
# simple dummy encryption for testing
def block_cipher_encryption(key: int, plain_text: int):
	return plain_text ^ key


# simple dummy decryption for testing
def block_cipher_decryption(key: int, cipher_text: int):
	return cipher_text ^ key


# splits a given text into smaller text blocks
def split_text_in_blocks(text: str, block_size: int):
	block_list = [int(text[i:len(text)] + "0" * (i + block_size - len(text)), 2) if i + block_size >
               len(text) else int(text[i:i + block_size], 2) for i in range(0, len(text), block_size)]
	return block_list


# converts a string (e.g. "0110100") into binary data
def string_to_binary(string: str, length: int):
	return format(string, f"0{str(length)}b")
