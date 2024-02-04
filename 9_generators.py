# More on Generators
# ==================

correct_combo = (3, 6, 1)

# instead of:
for c1 in range(10):
	for c2 in range(10):
		for c3 in range(10):
			if (c1, c2, c3) == correct_combo:
				print('found the combo: {}'.format((c1, c2, c3)))


# it is faster and more pythonic to do this:
def combo_gen():
	for c1 in range(10):
		for c2 in range(10):
			for c3 in range(10):
				yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
	print(c1, c2, c3)
	if (c1, c2, c3) == correct_combo:
		print('found the correct combo: {}'.format((c1, c2, c3)))


