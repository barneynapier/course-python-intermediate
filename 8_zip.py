# zip
# ===

# Iterates through multiple iterables and aggregates them

x = [1,2,3,4]
y = [7,8,3,2]
z = ['a', 'b', 'c', 'd']

for a,b,c in zip(x,y,z):
	print(a,b,c)

print(zip(x,y,z)) # prints the name of the zip object
