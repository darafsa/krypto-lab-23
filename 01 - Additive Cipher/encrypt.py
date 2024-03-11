from input_handler import *
import additive_cypher

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python encrypt.py <input_file> <key> <output_file>
# example:	python encrypt.py "Klartext_1.txt" 3 "Klartext_1_encrypted.txt"


assert_arguments(3)

alphabet = [chr(65 + i) for i in range(26)]

input_data = read(0)
encrypted_data = additive_cypher.encrypt(input_data, alphabet, get_key(1))
write(2, encrypted_data)