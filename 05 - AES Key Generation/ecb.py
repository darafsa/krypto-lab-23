import utils
import aes


# ecb encryption
# encrypts each plain text block with the key
def encrypt(data: str, key_data: str, sbox_data: str):
	encrypted_data = []
	round_keys = aes.generate_round_keys(key_data)
	sbox = utils.split_data_in_blocks(sbox_data, 128 * 16)[0]

	blocks = utils.split_data_in_blocks(data, 128)

	for block in blocks:
		output_data = aes.encrypt_block(block, round_keys, sbox)
		encrypted_data.append(output_data)

	return encrypted_data


# ecb decryption
# decrypts each cipher text block with the key
def decrypt(data: str, key_data: str, sbox_data: str):
	decrypted_data = []
	round_keys = aes.generate_round_keys(key_data)
	sbox = utils.split_data_in_blocks(sbox_data, 128 * 16)[0]

	blocks = utils.split_data_in_blocks(data, 128)

	for block in blocks:
		output_data = aes.decrypt_block(block, round_keys, sbox)
		decrypted_data.append(output_data)

	return decrypted_data
