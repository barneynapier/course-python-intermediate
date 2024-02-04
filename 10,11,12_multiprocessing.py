# Multiprocessing
# ===============

# multiprocessing is the same as running multiple python scripts at the same time
# CPUs = cores

import multiprocessing

def spawn():
	print('Spawned')

if __name__ == '__main__': # Checks if this script is the main module being run in python
	for i in range(5):
		p = multiprocessing.Process(target=spawn)
		p.start()
		p.join()

# note the if __name__ is every needed, its during multiprocessing



# Getting Values From Multiprocessing
# ===================================

from multiprocessing import Pool # Pool allows us to create a pool of worker processes

def job(num):
	return num*2

if __name__ = '__main__':
	p = Pool(processes=20)
	data = p.map(job, [i for i in range(20)]) # map function --> map(a Function, a Sequence), applies the function to the sequence
	p.close()
	print(data)


# Building a spider
# =================

from multiprocessing import Pool
import random
import requests
import string
import bs4 as bs

# This didnt seem to be too meaningful, but I was also a little drunk





