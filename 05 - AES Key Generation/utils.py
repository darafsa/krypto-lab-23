
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


# splits given data into smaller blocks which each are split into bytes
def split_data_in_blocks(data: str, block_size: int):
	# size of the block in hex format; e.g. 128 bit -> 32 hex letters
	block_hex_size = int(block_size / 4)
	# data is split into text blocks of 128 bit
	blocks = [data[i:i + block_hex_size].ljust(block_hex_size, '0')
           for i in range(0, len(data), block_hex_size)]
	# each text block is then split into its hex bytes and is then converted into integers
	byte_blocks = [[int(block[byte:byte + 2], 16)
                 for byte in range(0, len(block), 2)] for block in blocks]
	return byte_blocks


# converts a string (e.g. "0110100") into binary data
def string_to_binary(string: str, length: int):
	return format(string, f"0{str(length)}b")


# converts a list of blocked bytes into a string in hex representation
def bytes_to_hex(data: list):
	return "\n".join(" ".join(format(byte, "x").zfill(2) for byte in block) for block in data)


# shifts array by n steps
def shift_array(data: list, n: int):
	return data[-n:] + data[:-n]


# transforms a integer into a block of bytes
def int_to_block(n: int, block_size: int):
	return [int(format(n, 'x').zfill(32)[byte:byte + 2], 16) for byte in range(0, block_size // 4, 2)]


# adds (xor) to blocks together byte by byte
def xor_blocks(block1: list, block2: list):
	output_block = [None] * len(block1)
	for byte in range(len(block1)):
		output_block[byte] = block1[byte] ^ block2[byte]
	return output_block
