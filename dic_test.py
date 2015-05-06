a = ["Hello, world", "Guoshichao", "!", "@#$%^", "", "iterator"]
for i, x in enumerate(a):
	print '{} : {}'.format(i, x)


x = range(49, 149)
for i, j in enumerate(x):
	print '{} # {}'.format(i, j) # in python, the {} are the one use to refer to the element

# demonstrate the Permutations
import itertools
import time
start = time.time()
for p in itertools.permutations(range(10)):
	print ','.join(str(x) for x in p)
elapse = time.time() - start
print("time elapsed are : ", str(elapse), " seconds")
