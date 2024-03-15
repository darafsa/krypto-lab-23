import rsa_keygen
from input_handler import *

# note:		output_files will be generated in "./out/"
# usage: 	python generate_keys.py <length:int> <output_privat_key:str> <output_public_key:str> <output_primes:str>
# example:	python generate_keys.py 100 "private_key.txt" "public_key.txt" "primes.txt"


assert_arguments(4)

length = int(get_argument(0))

p = rsa_keygen.generate_prime(length)
q = rsa_keygen.generate_prime(length)

(e, n), (d, n) = rsa_keygen.generate_keys(p, q)

write(1, f"{d}\n{n}")
write(2, f"{e}\n{n}")
write(3, f"{p}\n{q}")
