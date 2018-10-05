def fibonaaci_sequences(n):
	result = [0, 1]
	while len(result) <= n:
		result.append(result[-2] + result[-1])
	return result

n_precalculated_terms = 10000
first_n_fibonacci = fibonaaci_sequences(n_precalculated_terms)
num_cases = 1000
memorizer = {}

def fibo_n_mod_m(n, m):
	if n <= n_precalculated_terms:
		return first_n_fibonacci[n] % m
	if n in memorizer:
		return memorizer[n]
	k, r = n // 3, n % 3
	f_k = memorizer.get(k, fibo_n_mod_m(k, m))
	if r == 0:
		result = (f_k * (5 * f_k * f_k - 3)) % m
		memorizer[n] = result
		return result
	f_k_1 = memorizer.get(k + 1, fibo_n_mod_m(k + 1, m))
	if r == 1:
		result = (f_k_1 * (5 * f_k * f_k - 3) + f_k) % m
		memorizer[n] = result
		return result
	if r == 2:
		result = (f_k * (5 * f_k_1 * f_k_1 - 3) - f_k_1) % m
		memorizer[n] = result
		return result
						
for _ in range(num_cases):
	n_str, m_str = input().split()
	memorizer = {}
	print(fibo_n_mod_m(int(n_str), int(m_str)))



