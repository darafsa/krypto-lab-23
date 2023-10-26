import sys
import additive_cypher

if len(sys.argv) < 4:
	print("Zu wenige Argumente übergeben.")
	exit()

alphabet = [chr(65 + i) for i in range(26)]

input_data = additive_cypher.read(sys.argv[1])
encrypted_data = additive_cypher.encrypt(input_data, alphabet, int(sys.argv[2]))
additive_cypher.write(sys.argv[3], encrypted_data)