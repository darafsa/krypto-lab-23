
# adds n to a character and remains within the limits of the alphabet
def add_n_to_char(char: str, n: int, m: int):
	return chr(65 + (ord(char) - 65 + n) % m)


# encrypts each letter of the input data and writes it to a new output string
# letters that are not contained in the alphabet remain unchanged
def encrypt(data: str, alphabet: list, key: int):
	return "".join([add_n_to_char(char, key, len(alphabet))
                 if char in alphabet else char for char in data])


# decrypts the input data using encryption with a negated key
def decrypt(data: str, alphabet: list, key: int):
	return encrypt(data, alphabet, -key)
