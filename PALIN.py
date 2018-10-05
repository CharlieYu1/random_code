def add1(num_str):
	num_digit = len(num_str)
	if num_str.count('9') == num_digit:
		return '1' + '0' * num_digit
	last_non_9_index = num_digit
	while last_non_9_index:
		last_non_9_index -= 1
		if num_str[last_non_9_index] != '9':
			return num_str[:last_non_9_index] + chr(ord(num_str[last_non_9_index]) + 1) + '0' * (num_digit - last_non_9_index - 1)

n = int(input())
for _ in range(n):
	num_str = input()
	num_digit = len(num_str)
	if num_str.count('9') == num_digit:
		print('1' + '0' * (num_digit - 1) + '1')
		continue
	half_num_length = int((num_digit + 1) / 2)
	first_half = num_str[:half_num_length]
	second_half = num_str[(num_digit - half_num_length):]
	if first_half[::-1] <= second_half:
		first_half = add1(first_half)
	if num_digit % 2 == 1:
		print(first_half + first_half[-2::-1]) 
	else:
		print(first_half + first_half[::-1])
