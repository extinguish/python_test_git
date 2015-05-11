#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test the recursive function
# the following are iterative way to calculate the fibonacci number
def fabonacci() :
	a, b = 0, 1
	while True:
		yield b
		a, b = b, a + b

fib = fabonacci()

print " please input the number you want to calculate : "
num = int(raw_input())
for i in range(num) :
	print fib.next()


# the following are the recursive way to calculate the fibonacci number
def fibonacci_r(n):
	if n == 1:
		return 1
	return n * fibonacci_r(n - 1)

print "the fibonacci recursive calculate result are : ", fibonacci_r(200)


L = [i for i in range(200) if i % 2 == 0]
print " the vlaue of the list are : ", L


# test the iterative function in the Python environments
d = {"a" : 1, "b" : 100}
for key in d:
	print key


for c in "guoshichao love shendan":
	print c, " --> really"


# we need to convert the following list into the dic via the 
# enumerate function
for i, value in enumerate(['s', 'h', 'e', 'd']) :
	print i, value

# the following are the normal one
for i, vlaue in [(1, 2), (2, 300), (300, 900)]:
	print i, value

# and we are goint to test the list generator function
print " the even number that between 1 and 100 are : "
l = [x * x for x in range(100) if x % 2 == 0]
print l
l_1 = [m + n for m in "guoshichao" for n in "shendan"]
print l_1

# we are goint to list all of the files that located in the current directory
import os
l_2 = [d for d in os.listdir(".")]
print l_2 

def fib(max) :
	n, a, b = 0, 0, 1
	while n < max:
		print b
		a, b = b, a + b
		n = n + 1


print " the following are the value of fibonacci number : "
fib(100)


# the following are the high-level function that we could using in Python environments
def add(x, y, f):
	return f(x) + f(y)


print " the value we calculate are : ", add(100, -100, abs)

# the following are another way to calculate the high-level function(高阶函数)
def f(x):
	return x * x
print " the value are calculate are : ", add(100, -100, f)

print " test the filter functions here "
def filter_out_prime_num(n):
	if n < 2:
		return False

	for i in range(2, n):
		if n % i == 0:
			return False

	return True


def print_l(l):
	for i in l:
		print i


# print_l(filter(filter_out_prime_num, [i for i in range(100)]))
# the filter() function are the high-level function(高阶函数)
L = filter(filter_out_prime_num, [i for i in range(100)])
print "the filtered result we get are : ", L

# another way to print the filtered result here 
print_l(filter(filter_out_prime_num, [i for i in range(100)]))

def reversed_cmp(x, y):
	if x > y:
		return -1

	if x < y:
		return 1
	return 0

# calculate the sum of one given array
def calc_sum(*args):
	ax = 0
	for i in args:
		ax += i
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for i in args:
			ax += n
		return ax
	return sum































