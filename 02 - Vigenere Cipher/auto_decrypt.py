from input_handler import *
import vigenere_cypher
import vigenere_cypher_auto

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python auto_decrypt.py <input_file:str> <output_file:str>
# example:	python auto_decrypt.py "Kryptotext_TAG.txt" "Kryptotext_TAG_auto_decrypted.txt"


assert_arguments(2)

alphabet = [chr(65 + i) for i in range(26)]

input_data = read(0)

key_length = vigenere_cypher_auto.calculate_key_length(
    input_data, alphabet, 0.07)
key = vigenere_cypher_auto.calculate_key(input_data, 'E', key_length, alphabet)
decrypted_data = vigenere_cypher.decrypt(input_data, alphabet, key)

write(1, f"{key}\n{decrypted_data}")
