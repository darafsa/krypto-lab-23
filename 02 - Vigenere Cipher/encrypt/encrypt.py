import sys
import vigenere_cypher
import read_write

if len(sys.argv) < 4:
	print("Zu wenige Argumente übergeben.")
	exit()

alphabet = [chr(65 + i) for i in range(26)]

input_data = read_write.read(sys.argv[1])
encrypted_data = vigenere_cypher.encrypt(input_data, alphabet, sys.argv[2])
read_write.write(sys.argv[3], encrypted_data)
