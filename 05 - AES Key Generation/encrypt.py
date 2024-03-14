import cbc
import ctr
import ecb
import ofb
from input_handler import *
import utils

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python encrypt.py <operating_mode:str> <input_file:str> <key_file:str> <output_file:str> [input_vector_file:str]
# example:	python encrypt.py cbc "Beispiel_Klartext.txt" "Beispiel_key.txt" "Beispiel_Klartext_cbc_encrypted.txt"


assert_arguments(4)
assert_mode(0, ["cbc", "ctr", "ecb", "ofb"])

mode = get_argument(0)

input_data = read_data(1)
key_data = read_data(2)
sbox_data = read_file("res/SBox.txt")

if mode == "cbc":
	encrypted_data = cbc.encrypt(input_data, key_data, sbox_data)
elif mode == "ctr":
	encrypted_data = ctr.encrypt(input_data, key_data, sbox_data)
elif mode == "ecb":
	encrypted_data = ecb.encrypt(input_data, key_data, sbox_data)
elif mode == "ofb":
	assert_arguments(5)
	input_vector_data = read_data(4)
	encrypted_data = ofb.encrypt(
		input_data, key_data, sbox_data, input_vector_data)

write(3, utils.bytes_to_hex(encrypted_data))
