import vigenere_cypher
import vigenere_cypher_auto


def read(path: str):
	with open(path, "r", encoding="utf-8") as f:
		return f.read()


alphabet = [chr(65 + i) for i in range(26)]

tests = [
	vigenere_cypher.convert_letter_to_number('G') == 6,
	vigenere_cypher.convert_number_to_letter(6) == 'G',

	vigenere_cypher.add_n_to_char('Y', 3, 26) == 'B',
	vigenere_cypher.add_n_to_char('B', -3, 26) == 'Y',

	vigenere_cypher.negate_key("FGADB") == "VUAXZ",

	vigenere_cypher.encrypt_additive('G', alphabet, 7) == 'N',
	vigenere_cypher.decrypt_additive('N', alphabet, 7) == 'G',

	vigenere_cypher.encrypt(read("res/Klartext_1.txt"),
	                        alphabet, "TAG") == read("res/Kryptotext_TAG.txt"),
	vigenere_cypher.decrypt(read("res/Kryptotext_TAG.txt"),
	                        alphabet, "TAG") == read("res/Klartext_1.txt"),


	vigenere_cypher_auto.convert_number_to_letter(6) == 'G',
	vigenere_cypher_auto.get_letter_frequency(
		"ABBCAB") == {'A': 2, 'B': 3, 'C': 1},

	round(vigenere_cypher_auto.calculate_partitionated_coincidence_index(
		"AISNLFPOIOWSD"), 5) == 0.03846,
	round(vigenere_cypher_auto.calculate_partitionated_coincidence_index(
		read("res/Klartext_1.txt")), 5) == 0.06996,

	vigenere_cypher_auto.calculate_key_length(
		read("res/Kryptotext_TAG.txt"), alphabet, 0.07) == 3,
	vigenere_cypher_auto.calculate_key(
		read("res/Kryptotext_TAG.txt"), 'E', 3, alphabet) == "TAG"
]

for (i, test) in enumerate(tests):
	assert test, f"Test {i+1} failed."

print(f"All {len(tests)} tests have passed. (Vigenere Cypher)")
