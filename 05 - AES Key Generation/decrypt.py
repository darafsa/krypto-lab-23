import aes
from input_handler import *

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python decrypt.py <input_file:str> <key_file:str> <output_file:str>
# example:	python decrypt.py "Beispiel_1_Kryptotext.txt" "Beispiel_key.txt" "Beispiel_1_Kryptotext_decrypted.txt"


assert_arguments(3)

input_data = read_data(0)
key = read_data(1)
sbox_inv = read_file("res/SBoxInvers.txt")

decrypted_data = aes.decrypt(input_data, key, sbox_inv)
write(2, decrypted_data)
