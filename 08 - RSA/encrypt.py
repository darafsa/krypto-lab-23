import rsa
from input_handler import *

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python encrypt.py <input_file:str> <key_file:str> <output_file:str>
# example:	python encrypt.py "ExampleText.txt" "ExampleKey.txt" "ExampleText_encrypted.txt"


assert_arguments(3)

input_data = read_data(0)[0]
keys = read_data(1)

encrypted_data = rsa.encrypt(input_data, keys[0], keys[1])

write(2, str(encrypted_data))
