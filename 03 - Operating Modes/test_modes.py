import ecb
import cbc
import ofb
import ctr
import math

# usage: 	python test_modes.py


plain_text = "0010101110101001010111010101000101010110101010010110100101010101001010010101010101110101010011111"
block_size = 5
key = 0b10101
init_vector = 0b11011

if pow(2, block_size) < math.ceil(len(plain_text) / block_size):
	print(
		f"Block size of {block_size} is too small for the length of the input text! (Overflow)")
	exit()


cipher_text = ecb.encrypt(plain_text, block_size, key)
plain_text = ecb.decrypt(cipher_text, block_size, key)
print(f"ecb: {plain_text}")

cipher_text = cbc.encrypt(plain_text, block_size, key)
plain_text = cbc.decrypt(cipher_text, block_size, key)
print(f"cbc: {plain_text}")

cipher_text = ofb.encrypt(plain_text, block_size, key, init_vector)
plain_text = ofb.decrypt(cipher_text, block_size, key, init_vector)
print(f"ofb: {plain_text}")

cipher_text = ctr.encrypt(plain_text, block_size, key)
plain_text = ctr.decrypt(cipher_text, block_size, key)
print(f"ctr: {plain_text}")
