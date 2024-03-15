import diffie_hellman
from input_handler import *

# note:		output_files will be generated in "./out/"
# usage: 	python key_exchange.py <length:int> <output_file:str>
# example:	python key_exchange.py 100 "output.txt"


assert_arguments(2)

length = int(get_argument(0))

p, q = diffie_hellman.generate_primes(length)
g = diffie_hellman.generate_generator(p, q)
A, B, S = diffie_hellman.generate_secrets(g, p)

write(1, f"{p}\n{g}\n{A}\n{B}\n{S}")
