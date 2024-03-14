import aes
from input_handler import *

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python encrypt.py <input_file:str> <key_file:str> <output_file:str>
# example:	python encrypt.py "Beispiel_1_Klartext.txt" "Beispiel_key.txt" "Beispiel_1_Klartext_encrypted.txt"


assert_arguments(3)

input_data = read_data(0)
key = read_data(1)
sbox = read_file("res/SBox.txt")

encrypted_data = aes.encrypt(input_data, key, sbox)
write(2, encrypted_data)
