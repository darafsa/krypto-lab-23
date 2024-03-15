import random


# decomposes n into m and k, where n - 1 = 2^k * m
def get_m_k(n: int):
	m = (n - 1) // 2
	k = 1
	while m % 2 == 0:
		m //= 2
		k += 1

	return int(m), k


# Miller-Rabin prime number test, checks whether a given number n is a prime number
# has false-positive results with p <= 1/4
def miller_rabin(n: int):
	if n <= 2:
		return n == 2
	if n % 2 == 0:
		return False

	m, k = get_m_k(n)
	a = random.randrange(2, n)
	b = pow(a, m, n)

	if b == 1 % n:
		return True
	for i in range(k):
		if b == -1 % n:
			return True
		b = pow(b, 2, n)
	return False


# runs prime number tests in several rounds to reduce the probability of false positives
def is_prime(n: int, rounds: int):
	for i in range(rounds):
		if not miller_rabin(n):
			return False
	return True


# generates a prime number with the approximate length of the specified bits
def generate_prime(bits: int):
	z = random.randrange(pow(2, bits - 1), pow(2, bits))
	x = 0
	offsets = [1, 7, 11, 13, 17, 19, 23, 29]
	offset_i = 0

	# p(false-postive) <= 10^-20
	while not is_prime(x, 34):
		x = 30 * (z + offset_i // len(offsets)) + offsets[offset_i % len(offsets)]
		offset_i += 1

	return x


# generates p and q, where p = 2 * q + 1
def generate_primes(bits: int):
	p = 1
	while not is_prime(p, 34):
		q = generate_prime(bits - 1)
		p = 2 * q + 1
	return p, q


# generates sufficient generator
def generate_generator(p: int, q: int):
	m = p - 1  # = 2 * q
	a = 1

	while pow(a, m // 2, p) == 1 or pow(a, m // q, p) == 1:
		a = random.randrange(2, m + 1)
	return a


# generates Alice and Bob's secrets and the Shared secret (key)
def generate_secrets(g: int, p: int):
	a = random.randrange(2, p - 1)
	b = random.randrange(2, p - 1)

	A = pow(g, a, p)
	B = pow(g, b, p)
	S = pow(A, b, p)
	return A, B, S
