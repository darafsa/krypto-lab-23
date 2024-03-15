
# converts an ASCII character to a number, where A=0 and Z=25
def convert_letter_to_number(char: str):
	return ord(char) - 65


# converts a number to an ASCII character, where 0=A and 25=Z
def convert_number_to_letter(char: int):
	return chr(65 + char)


# adds a number n to the character, respecting  the limits of the alphabet
def add_n_to_char(char: str, n: int, m: int):
	return convert_number_to_letter((convert_letter_to_number(char) + n) % m)


# encrypts a character
def encrypt_additive(char: str, alphabet: list, key: int):
	return add_n_to_char(char, key, len(alphabet))


# decrypts a character using encryption with a negated key
def decrypt_additive(char: str, alphabet: list, key: int):
	return encrypt_additive(char, alphabet, -key)


# encrypts each letter of the input data and writes it to a new output string
# letters that are not contained in the alphabet remain unchanged
def encrypt(data: str, alphabet: list, key: str):
	encrypted_str = ""
	key_idx = 0
	for char in data:
		if char not in alphabet:
			encrypted_str += char
		else:
			encrypted_str += encrypt_additive(char, alphabet,
			                                  convert_letter_to_number(key[key_idx % len(key)]))
			key_idx += 1
	return encrypted_str


# calculates a negated key for decryption
def negate_key(key: str):
	negated_key = ""
	for char in key:
		negated_key += convert_number_to_letter(-convert_letter_to_number(char))

	return negated_key


# decrypts the input data using encryption with a negated key
def decrypt(data: str, alphabet: list, key: str):
	return encrypt(data, alphabet, negate_key(key))
