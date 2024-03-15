import random
from input_handler import *


def get_m_k(n: int):
	m = (n - 1) // 2
	k = 1
	while m % 2 == 0:
		m //= 2
		k += 1

	return int(m), k


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


def is_prime(n: int, rounds: int):
	for i in range(rounds):
		if not miller_rabin(n):
			return False
	return True


def extended_euclidean_algorithm(a, b):
	k = 0
	r = [a, b]
	s = [1, 0]
	t = [0, 1]

	while r[k + 1] != 0:
		k += 1
		q = r[k - 1] // r[k]
		r.append(r[k - 1] - q * r[k])
		s.append(s[k - 1] - q * s[k])
		t.append(t[k - 1] - q * t[k])
	return r[k], s[k], t[k]


def generate_prime(bits: int):
	z = random.randrange(pow(2, bits - 1), pow(2, bits))
	x = 30 * z
	offsets = [1, 7, 11, 13, 17, 19, 23, 29]
	offset_i = 0

	# w(false-postive) <= 1 * 10^-20
	while not is_prime(x, 33):
		x = x + offsets[offset_i % len(offsets)] + 30 * (offset_i // len(offsets))
		offset_i += 1

	return x


def phi(p: int, q: int):
    return (p - 1) * (q - 1)


def generate_keys(p: int, q: int):
	n = p * q
	phi_n = phi(p, q)
	e = random.randrange(pow(2, 15), pow(2, 16))

	while extended_euclidean_algorithm(e, phi_n)[0] != 1:
		e = random.randrange(pow(2, 15), pow(2, 16))

	d = extended_euclidean_algorithm(e, phi_n)[1] % phi_n

	return (e, n), (d, n)
