from input_handler import *
import additive_cypher

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python auto_decrypt.py <input_file> <output_file>
# example:	python auto_decrypt.py "sampleEncrypted.txt" "sampleEncrypted_decrypted.txt"


def count_chars(string: str, alphabet: list):
	char_count = {char: 0 for char in alphabet}
	for char in string:
		if char in char_count:
			char_count[char] += 1
	return char_count


def calculate_key(encrypted_char: str, most_common_char: str):
	return (ord(encrypted_char) - ord(most_common_char)) % 26


assert_arguments(2)

alphabet = [chr(65 + i) for i in range(26)]

input_data = read(0)

char_count = count_chars(input_data, alphabet)
key = calculate_key(max(char_count, key=char_count.get), 'E')
decrypted_data = additive_cypher.decrypt(input_data, alphabet, key)

write(1, f"{key}\n{decrypted_data}")