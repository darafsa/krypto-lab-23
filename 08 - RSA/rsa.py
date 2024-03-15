
# x**m mod n
def potentiate(x: int, m: int, n: int):
	m_bin = format(m, 'b')[::-1]
	r = len(m_bin)
	y = 1
	for i in range(r):
		if m_bin[i] == '1':
			y = (y * x) % n
		x = (x * x) % n
	return y


def encrypt(data: int, key: int, n: int):
	return potentiate(data, key, n)
