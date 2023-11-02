def convert_letter_to_number(char:str):
	return ord(char) - 65

def add_n_to_char(char:str, n:int, m:int):
	return chr(65 + (ord(char) - 65 + n) % m)

def encrypt_additive(data:str, alphabet:list, key:int):
	return "".join([add_n_to_char(char, key, len(alphabet)) if char in alphabet else char for char in data])

def decrypt_additive(data:str, alphabet:list, key:int):
	return encrypt_additive(data, alphabet, -key)

def encrypt(data:str, alphabet:list, key:str):
	encrypted_str = ""
	i = 0
	for char in data:
		if char == " ":
			encrypted_str += " "
		else:
			encrypted_str += encrypt_additive(char, alphabet, convert_letter_to_number(key[i % len(key)]))
			i += 1
	return encrypted_str

def decrypt(data:str, alphabet:list, key:str):
	decrypted_str = ""
	i = 0
	for char in data:
		if char == " ":
			decrypted_str += " "
		else:
			decrypted_str += encrypt_additive(char, alphabet, -convert_letter_to_number(key[i % len(key)]))
			i += 1
	return decrypted_str