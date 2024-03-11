from input_handler import *
import additive_cypher

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python decrypt.py <input_file> <key> <output_file>
# example:	python decrypt.py "Kryptotext_1_Key_7.txt" 7 "Kryptotext_1_Key_7_decrypted.txt"

assert_arguments(3)

alphabet = [chr(65 + i) for i in range(26)]

input_data = read(0)
decrypt_data = additive_cypher.decrypt(input_data, alphabet, get_key(1))
write(2, decrypt_data)
