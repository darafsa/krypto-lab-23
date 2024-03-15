
# converts a number to an ASCII character, where 0=A and 25=Z
def convert_number_to_letter(char: str):
	return chr(65 + char)


# counts the characters in the input data and returns them in a dictionary
def get_letter_frequency(data: str):
	frequency = {}
	for char in data:
		frequency[char] = frequency[char] + 1 if char in frequency else 1
	return frequency


# calculates the coincidence index of a partitioned text by using the given formula
def calculate_partitionated_coincidence_index(data: str):
	n = len(data)
	if n <= 1:
		return 0
	letter_frequencies = get_letter_frequency(data)
	frequency_sum = sum([letter_frequency * (letter_frequency - 1)
                      for letter_frequency in letter_frequencies.values()])
	return (1 / (n * (n - 1))) * frequency_sum


# calculates the length of the most probable key by calculating the coincidence indices for each key length
# and selecting the smallest key length whose coincidence index is above the given delta
def calculate_key_length(data: str, alphabet: list, delta: float):
	filtered_data = "".join(char for char in data if char in alphabet)
	coincidence_indices = []

	for i in range(1, 101):
		text_partitions = [filtered_data[partition::i] for partition in range(i)]

		partitionated_coincidence_indices = []
		for text_partition in text_partitions:
			partitionated_coincidence_indices.append(calculate_partitionated_coincidence_index(
				text_partition))

		avg_coincidence_index = sum(
			partitionated_coincidence_indices) / len(partitionated_coincidence_indices)
		if avg_coincidence_index > delta:
			coincidence_indices.append(i)

	return coincidence_indices[0]


# matches the most frequent character of each cryptotext partition with the
# most frequent character of the language to calculate the key used
def calculate_key(data: str, most_common_char: str, key_length: int, alphabet: list):
	filtered_data = "".join(char for char in data if char in alphabet)

	key = ""
	for i in range(key_length):
		text_partition = filtered_data[i::key_length]
		char_count = get_letter_frequency(text_partition)
		encrypted_char = max(char_count, key=char_count.get)
		key += convert_number_to_letter((ord(encrypted_char) -
		                                ord(most_common_char)) % 26)

	return key
