from input_handler import *
import vigenere_cypher

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python decrypt.py <input_file:str> <key:str> <output_file:str>
# example:	python decrypt.py "Kryptotext_TAG.txt" "TAG" "Kryptotext_TAG_decrypted.txt"


assert_arguments(3)

alphabet = [chr(65 + i) for i in range(26)]

input_data = read(0)
decrypted_data = vigenere_cypher.decrypt(input_data, alphabet, get_key(1))
write(2, decrypted_data)