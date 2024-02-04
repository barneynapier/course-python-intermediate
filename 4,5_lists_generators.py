# LIST COMPREHENSIONS
# ===================


xyz = (for i in range(10000000))    # Can generate a list
print(list(xyz)[:5])                # this generates a list of xyz for the first 5 numbers

xyz = [i for i in range(10000000)]  # IS a list
print(xyz[:5])                      # this actually commits the list to memory

# List comprehensions commit a whole list to memory and so are less useful for large lists like above   

for i in range(5):
	for ii in range(3):
		print(i,ii)

[[print(i,ii) for ii in range(3)] for i in range(5)] # work back from bottom up of the above version

# the two above are identical