from input_handler import *
import utils


# rotates a word to the left
def rot_word(word: list):
	return word[1:] + word[:1]


# substitutes a word with the entries from SBox
def sub_word(word: list, sbox: list):
	output_data = [None] * len(word)
	for byte in range(len(word)):
		output_data[byte] = sbox[word[byte]]
	return output_data


# word addition in galois field (^)
def add_words(word1: list, word2: list):
	output_word = [None] * len(word1)
	for i in range(len(word1)):
		output_word[i] = word1[i] ^ word2[i]
	return output_word


# generates 11 128-bit round keys for the AES standard
def generate_round_keys(key_data: str, sbox_data: list):
	rcon = [[rc, 0, 0, 0] for rc in [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54]]

	key = utils.split_data_in_blocks(key_data, 128)[0]
	sbox = utils.split_data_in_blocks(sbox_data, 128 * 16)[0]
	words = [[None]] * 44

	for i in range(4):
		words[i] = [key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]]

	for i in range(4, 44):
		tmp = words[i - 1]
		if i % 4 == 0:
			tmp = add_words(sub_word(rot_word(tmp), sbox), rcon[i // 4])
		words[i] = add_words(words[i - 4], tmp)

	round_keys = []
	for i in range(11):
		round_keys.append(words[i * 4] + words[i * 4 + 1] +
		                  words[i * 4 + 2] + words[i * 4 + 3])

	return round_keys
