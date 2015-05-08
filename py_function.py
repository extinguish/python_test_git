#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the following are the basic part of python function invocation
# example
abs(-1000)

abs(1000)

print "please input the number you want to calculate : "
num = raw_input()
print "and the abs value of the number you input are : "
# we need to first convert the user input value we hold into integer
# the raw_input() value are default string type that python built-in
print abs(int(num))

print "convert the string we input into float number : " 
float_num = raw_input()

print "the convertd value we get are : "
print float(float_num)


# and then all of the following block are the function that defined by ourseleves
def my_abs_impl(x) :
	if x > 0:
		return x
	else:
		return -x


# then we invoke the function we defined up here
print "calculate the abs value that defined by ourseleves : "
print my_abs_impl(int(raw_input()))

# the followin module are using to calculate the two-dimentional coordinate 
# calculations
import math

def move(x, y, step, angle = 0) :
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny
print "and then the test part comes here"
x, y = move(10, 20, 34, 30)
print " the x value are : %d ", x , " and the y value are : %d ", y

print " another test comes here : "
x, y = move(10, 20, 34, math.pi / 6)
print "the x value are : ", x, " and the y value are : ", y

print "we are then going to implement power calculation functions here "
# def power(x, n) :
# 	if n <= 0:
# 		return 1
# 	elif n == 1:
# 		return x
# 	else:
# 		x = x * x
# 		n = n - 1
# 		return x
def power(x, n) :
	s = 1
	while n >= 0:
		n = n - 1
		s = s * x
	return s

# the test comes here
print " input the original number you want to calculate : "
basic_num = int(raw_input())
print " input the power value you want to calculate : "
power_num = int(raw_input())
print " and the final value we get are : ", power(basic_num, power_num)

# and then the following are the function that implement the default variants value
def enroll(name, grades, age = 100, score = 69, city = "beijing") :
 	print "name are ", name
 	print "age are : ", age
 	print "score are : ", score
 	print " and finally the city are : ", city

# tes the enroll function
enroll("guoshichao", 3, 30, 79)
enroll("guoshichao", 2, city = "hebei")


# test the default parameter
def add_end(L = []):
	L.append('END')
	return L

print "the range value we get are : "
for i in range(10):
	add_end()

print add_end()

# the following is another version of add_end() implementations
def add_end_1(L = None) :
	if L is None:
		L = []
	L.append('END')
	return L

for i in range(12):
	add_end_1()

print add_end_1()

# calculate any number of variants value
def cal(*numbers) :
	sum = 0
	for num in numbers:
		sum += num
	return sum

print "calculate the value:"

print cal(1, 20, 30, 40)
































































