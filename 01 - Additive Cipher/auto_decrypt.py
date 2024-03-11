from input_handler import *
import additive_cypher

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python auto_decrypt.py <input_file:str> <output_file:str>
# example:	python auto_decrypt.py "sampleEncrypted.txt" "sampleEncrypted_auto_decrypted.txt"


# counts the characters in the input string and returns them in a dictionary
def count_chars(data: str):
	char_count = {}
	for char in data:
		char_count[char] = char_count[char] + 1 if char in char_count else 1
	return char_count


# matches the most frequent character from the cryptotext with the most
# frequent character of the language to calculate the key used
def calculate_key(data: str, most_common_char: str):
	char_count = count_chars(data)
	encrypted_char = max(char_count, key=char_count.get)
	return (ord(encrypted_char) - ord(most_common_char)) % 26


assert_arguments(2)

alphabet = [chr(65 + i) for i in range(26)]

input_data = read(0)

key = calculate_key(input_data, 'E')
decrypted_data = additive_cypher.decrypt(input_data, alphabet, key)

write(1, f"{key}\n{decrypted_data}")
