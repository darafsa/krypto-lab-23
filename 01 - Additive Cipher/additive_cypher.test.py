import additive_cypher
import additive_cypher_auto


def read(path: str):
	with open(path, "r", encoding="utf-8") as f:
		return f.read()


alphabet = [chr(65 + i) for i in range(26)]

tests = [
	additive_cypher.add_n_to_char('Y', 3, 26) == 'B',
	additive_cypher.add_n_to_char('B', -3, 26) == 'Y',

	additive_cypher.encrypt("INFORMATIK", alphabet, 7) == "PUMVYTHAPR",
	additive_cypher.decrypt("PUMVYTHAPR", alphabet, 7) == "INFORMATIK",

	additive_cypher_auto.count_chars("ABBCAB") == {'A': 2, 'B': 3, 'C': 1},
	additive_cypher_auto.calculate_key(read("res/sampleEncrypted.txt"), 'E') == 10
]

for (i, test) in enumerate(tests):
	assert test, f"Test {i+1} failed."

print(f"All {len(tests)} tests have passed. (Additive Cypher)")
