# TimeIt Module
# =============

import timeit

print(timeit.timeit('1+3', number=20000000))
# this tells us how long in seconds it took the computer to do 1+3 20000000 times

# You can use timeit to see which method of code is more efficient for your computer

# Generators are hugely more efficient until you convert them into lists, then they are only a bit faster

# Long story short use generators