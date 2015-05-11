#!/usr/bin/env python
# test the partial function ability
# test the python partial function
from functools import partial

def mode(n, m):
	return n % m

mode_by_100 = partial(mode, 100)

print mode(100, 7)
print mode_by_100(7)

def slice(n, m):
	return n - m

slice_by_200 = partial(slice, 1000)

print slice(1000, 300)
print slice_by_200(300)

def multi(x, y, z):
	return x * y * z

# the partial function can hold some arguments, and then modify 
# the part of which we want to change dynamically
multi_by_20 = partial(multi, 2, z = 9)

print multi(2, 10, 9)
print multi_by_20(10)





