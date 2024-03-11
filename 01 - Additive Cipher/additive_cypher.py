
def add_n_to_char(char:str, n:int, m:int):
	return chr(65 + (ord(char) - 65 + n) % m)

def encrypt(data:str, alphabet:list, key:int):
	return "".join([add_n_to_char(char, key, len(alphabet)) if char in alphabet else char for char in data])

def decrypt(data:str, alphabet:list, key:int):
	return encrypt(data, alphabet, -key)
