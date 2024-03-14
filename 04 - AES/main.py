import aes
from input_handler import *


assert_arguments(2)

key = read_data(0)
input_data = read_data(1)
sbox = read_file("res/SBox.txt")
sbox_inv = read_file("res/SBoxInvers.txt")

encrypted_data = aes.encrypt(input_data, key, sbox)
decrypted_data = aes.decrypt(encrypted_data, key, sbox_inv)

# print(f"key: {key}")
print(f"input:     {input_data}")

print(f"encrypted: {encrypted_data}")
print(f"decrypted: {decrypted_data}")

# input_data = read(0)
# encrypted_data = aes.encrypt(input_data, get_key(1))
# write(2, encrypted_data)
