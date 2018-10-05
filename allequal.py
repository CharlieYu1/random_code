def allequal(iterable):
	iterator = iter(iterable)
	try:
		first = next(iterator)
	except StopIteration:
		return True
	return all(first == rest for rest in iterator)
