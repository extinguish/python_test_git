#!/usr/bin/env python
# the line that up here are using for the command line to 
# detect that the current script file are python file
# and then we could execute it from the command line 
# directly
# test the variable scope usage
x = 1
scope = vars()
print scope['x']

# change the local variables to the global variable
x = 1
def change_global() :
	global x
	x += 1
	return x

print "After changed the global variable are :" + str(change_global())

# nested function definition
def foo(shit):
	def bar(shit_another):
		print "guoshichao" + "hello world" + str(shit_another) + str(shit)
	# bar

def test_nested_foo():
	test = foo('guoshichao')
	test('guoshichao')

# print "the result of the nested foo() are : " + str(test_nested_foo())



# another way to define the nested function, 
# this way may be even more funny
def multiplier(factor) :
	def multiplyByFactor(num) :
		return num * factor
	return multiplyByFactor

def test_nested_multi():
	double = multiplier(2)
	return double(14) # the double(14) are the special way to incoke the nested function.

print "the multiple function result are : " + str(test_nested_multi())
print "another way of using the nested function : " + str(multiplier(89)(32))


# use the recursion in python to re-implement the factorial
# the first one are the normal iterate way to implement this
def factorial_iterate(n):
	result = n # as the range(1, n) are output (0, 1, 2, .... , n-1), not to n, so we need to define the result init value as n
			   # if we define the init value of result as 1, that is result = 1, the final result will be not correct.
	for i in range(1, n):
		result *= i
	return result

print " the factorial of 2 are : " + str(factorial_iterate(3))
print " the factorial of 10 are : " + str(factorial_iterate(10))

# now, we re-implement the factorial number in recursive way
def factorial_recursive(n):
	if n <= 1:
		return n
	else:
		return n * factorial_recursive(n - 1)

print " the factorial recursion of 10 result are : " + str(factorial_recursive(10))

# implement the power function
def power(x, n):
	result = 1
	for i in range(n):
		result *= x
	return result

print "12^ 3 are : ", power(12, 4)

# implement the factorial number in recursive way
def power_recursive(x, n):
	if n == 0:
		return 1
	elif n == 1:
		return x
	else:
		return x * power_recursive(x, n - 1)

print "12^3 are : ", power_recursive(12, 4)


# implement the search function(use divide and conqure)
def search(sequence, number, lower, upper):
	if lower == upper:
		assert number == sequence[lower] or number == sequence[upper]
		return lower
	else:
		middle = (lower + upper) // 2
		if number > sequence[middle]:
			return search(sequence, number, middle + 1, upper)
		else:
			return search(sequence, number, lower, middle)

seq = [20, 65, 98, 5467, 4787, 2, 3, 9, 70, 30]
seq.sort()
print seq
print "we have find the 5 ? ", search(seq, 5, 0, 10)


# define the class to encapsulate the relative attributes into one class
# we need to add the __metaclass__ = type to declare the type, this is the
# new usage since Python 3.0
__metaclass__ = type
class Person:
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def greeting(self):
		print "Hello, the class world \! I am the %s " % self.name













































