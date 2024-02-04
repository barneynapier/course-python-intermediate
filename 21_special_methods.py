# Special Methods
# ===============

next(x) # moves the iterator forward one space
x.__next__() # does the same thing as next, look in dir(x) for all the methods

x = range(5) # generator, cannot use next!
x = (i for i in range(5)) # generator expression, can use next

class range_example:

	def __init__(self, end, step=1):
		self.current = 0
		self.end = end
		self.step = step
	
	def __iter__(self):
		return self

	def __next__(self):
		if self.current >= self.end:
			raise StopIteration()
		else:
			return_val = self.current
			self.current += self.step
			return return_val







