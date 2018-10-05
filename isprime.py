import itertools

def isPrime(n):
	if n < 4:
		return {1: False, 2: True, 3: True}[n]
	if n % 2 == 0:
		return False
	return all(n % i for i in range(3, int(n**.5), 2))
	
start = 6138978829
MAX_PRIMES = 10

print('The first {} primes since {}:'.format(MAX_PRIMES, start))
num_primes = 0
for n in itertools.count(start):
	if isPrime(n):
		print(n)
		num_primes += 1
		if num_primes == MAX_PRIMES:
			break

