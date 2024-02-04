# Enumerate
# =========

# Returns a number from the count, then the corresponding value from an iterable form (EG list, dict)

lst = ['one', 'two', 'three']

for i in range(len(lst)):
	print(i, lst[i])

# above is the same as:

for i,j in enumerate(lst):		# way faster
	print(i,j)