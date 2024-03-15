from input_handler import *
import sha3

# note:		input_files need to be stored in "./res/", output_files will be generated in "./out/"
# usage: 	python hash.py <input_file:str> <output_file:str>
# example:	python hash.py "file.txt" "file_hash.txt"


assert_arguments(2)

input_data = read_data(0)
hash_data = sha3.hash(input_data)
write(1, hash_data)
