class foo():
	def  __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	
	def __repr__(self):
		return str(self.a)

bar = foo(1, 2, 3)
s = {}
s[bar] = bar.b
print(s)
