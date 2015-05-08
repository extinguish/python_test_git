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


