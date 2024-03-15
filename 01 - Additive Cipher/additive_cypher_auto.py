
# counts the characters in the input string and returns them in a dictionary
def count_chars(data: str):
	char_count = {}
	for char in data:
		char_count[char] = char_count[char] + 1 if char in char_count else 1
	return char_count


# matches the most frequent character from the cryptotext with the most
# frequent character of the language to calculate the key used
def calculate_key(data: str, most_common_char: str):
	char_count = count_chars(data)
	encrypted_char = max(char_count, key=char_count.get)
	return (ord(encrypted_char) - ord(most_common_char)) % 26
