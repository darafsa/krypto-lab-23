from input_handler import *
import additive_cypher
import additive_cypher_auto

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python auto_decrypt.py <input_file:str> <output_file:str>
# example:	python auto_decrypt.py "sampleEncrypted.txt" "sampleEncrypted_auto_decrypted.txt"


assert_arguments(2)

alphabet = [chr(65 + i) for i in range(26)]

input_data = read(0)

key = additive_cypher_auto.calculate_key(input_data, 'E')
decrypted_data = additive_cypher.decrypt(input_data, alphabet, key)

write(1, f"{key}\n{decrypted_data}")
