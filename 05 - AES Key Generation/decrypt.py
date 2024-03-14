import cbc
import ctr
import ecb
import ofb
from input_handler import *
import utils

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python decrypt.py <operating_mode:str> <input_file:str> <key_file:str> <output_file:str> [input_vector_file:str]
# example:	python decrypt.py cbc "Beispiel_Kryptotext_cbc.txt" "Beispiel_key.txt" "Beispiel_Kryptotext_cbc_decrypted.txt"


assert_arguments(4)
assert_mode(0, ["cbc", "ctr", "ecb", "ofb"])

mode = get_argument(0)

input_data = read_data(1)
key_data = read_data(2)
sbox_inv_data = read_file("res/SBoxInvers.txt")
sbox_data = read_file("res/SBox.txt")

if mode == "cbc":
	decrypted_data = cbc.decrypt(input_data, key_data, sbox_inv_data)
elif mode == "ctr":
	decrypted_data = ctr.decrypt(input_data, key_data, sbox_data)
elif mode == "ecb":
	decrypted_data = ecb.decrypt(input_data, key_data, sbox_inv_data)
elif mode == "ofb":
	assert_arguments(5)
	input_vector_data = read_data(4)
	decrypted_data = ofb.decrypt(
		input_data, key_data, sbox_data, input_vector_data)

write(3, utils.bytes_to_hex(decrypted_data))
