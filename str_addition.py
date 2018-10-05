import time
import random
import decimal

	
num_digits = 400000
a = random.choice('123456789') + \
			''.join(random.choices('0123456789', k = num_digits - 1))
b = random.choice('123456789') + \
			''.join(random.choices('0123456789', k = num_digits - 1))
decimal.getcontext().prec = num_digits + 1
start_time = time.time()
print(str(decimal.Decimal(a) + decimal.Decimal(b)))
time_for_convert_int_first = time.time() - start_time
print('{} seconds for converting to int before addition'.format(
			time_for_convert_int_first))
