import time

x2 = int(input())
p = 4000000007
repeated_squares = [x2]
for _ in range(29):
	repeated_squares.append((repeated_squares[-1] ** 2) % p)
	
result = 1
b = bin((p + 1) >> 2)[:1:-1]
for i in range(len(b)):
	if b[i] == '1':
		result = (result * repeated_squares[i]) % p
result = min(result, p - result)
print(time.strftime('%a %b %d %H:%M:%S %Y', time.gmtime(result)))
