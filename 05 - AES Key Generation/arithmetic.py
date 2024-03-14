
# doubles a number by cycling to the left; stays in mod 8
def byte_double(a: int):
	bits = format(a, 'b').zfill(8)
	bits = bits[len(bits) - 8:len(bits)]
	t = (a << 1) % 2**8
	if bits[0] != '0':
		return t ^ int("1b", 16)
	return t


# multiplicates two numbers by using russian pawn multiplication
def mult(a: int, b: int):
	start_sum = b if a % 2 != 0 else 0
	return mult_rek(a, b, start_sum)


# recursive implementation of russion pawn multiplication
def mult_rek(a: int, b: int, sum: int):
	if a <= 1:
		return sum
	a //= 2
	b = byte_double(b)

	if a % 2 != 0:
		sum = sum ^ b

	return mult_rek(a, b, sum)


# matrix multiplication in galois field
def matrix_mult(matrix: list, vector: list):
	output_vec = [0] * 4
	for i in range(4):
		row = matrix[i * 4:(i + 1) * 4]
		output_vec[i] ^= mult(row[0], vector[0])
		output_vec[i] ^= mult(row[1], vector[1])
		output_vec[i] ^= mult(row[2], vector[2])
		output_vec[i] ^= mult(row[3], vector[3])
	return output_vec
