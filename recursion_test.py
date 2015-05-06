# the base usage of the Python recursion
# the first version are iterator version
def listSum(numList):
	theSum = 0
	for i in numList:
		theSum = theSum + i
	return theSum

print listSum(range(100))

# implement the recursion version
def listSum_r(numList):
	if len(numList) == 1:
		return numList[0]
	else:
		return numList[0] + listSum_r(numList[1:])

print "The recursive version are : ", listSum_r(range(100))

# calculate the fibonacci number
# we use arrray to store the fibonacci calculating results
# the following method use array to implement it in iterative way
# not in recursive way
fibs = [0, 1]
def fibNum(num):
	for i in range(num - 2):
		fibs.append(fibs[-2] + fibs[-1])
	return fibs # return the result array of which contains all of the fibonacci number we calculated

print "calulating the fibonacci number are :", fibNum(10)

# another way
def fibas(num):
	result = [0, 1]
	for i in range(num - 2):
		result.append(result[-2] + result[-1])
	return result

print "calculating : ", fibas(10)

# demonstrate the usage of document commenting.
def square(x) :
	'calculating out the square of the number x'
	return x * x

print "the square of x are : ", square(98)


# result_1 = [0, 1] # we need to store the initial result of fibonacci number first to act 
				# as the break point of this recursive function
# def fibonacciNumCal(num) :
# 	for i in range(num - 2):
# 		result_1.append(result_1[-2] + result_1[-1])
# 	return result_1

# print "the result of fibonacci are : ", fibonacciNumCal(10)

# implement the fibonacci in recursive way
def fibRecu(num):
	if num == 0 or num == 1 or num == 2:
		return 1
	else:
		return fibRecu(num - 1) + fibRecu(num - 2)

print "the recursive way to calcualte the fibonacci are : ", fibRecu(9)

# one even more wonderful way to implement the fibonacci number
# the following way to implement the Fibonacci number use 
# the generator, and the generator could use yield to return the middle
# calculating result of the Fibonacci
def fibonacciWonderful():
	a, b = 0, 1
	while True:
		yield b # here, we could generate any variant we want
		a, b = b, a + b

fibTest = fibonacciWonderful() # we cannot require next() attribute from the fibonacciWonderful() 
							   # directly, as the console would hint that the method in python has 
							   # no feature of next(), only the primitive variants has this feature
							   # Even with that, we could only use the fibTest.next() in python 2.7
							   # not in python 3(python 3 has removed this feature, and add it in
							   # some other place, but for now, I dont know where???)
print "the fibonacci number are : ", fibTest.next()

for i in range(100):
	# result = 0
	"""calculate the fibonacci number from 0 to 100"""
	result = fibTest.next()
	print result,

# calculate the power, version 1
# the following method do not depends on the usage of return
# but with yield, these methods can still return some value to
# the invoker.
def power(values):
	for value in values:
		print "powering %s " % value
		yield value

def adder(values):
	for value in values:
		print "adding number to %s " % value
		if value % 2 == 0:
			yield value + 3
		else:
			yield value + 100

elements = [1, 4, 7, 9, 12, 14, 19]
res = adder(power(elements))

for i in range(6):
	print "the power and the adder: ", res.next()


# another usage of the generator
def psychologist():
	print "Please tell me your problems : "
	while True:
		answer = (yield)
		if answer is not None:
			if answer.endswith('?'):
				print "I am asking you, give me the answer!!!"
			elif 'good' in answer:
				print "that's good, let's go on"
			elif 'bad' in answer:
				print "fuck you off!!!"

free = psychologist()

for i in range(3):
	free.next()

import os
print os.getcwd()
print (os.getcwd()) # while we working in python 2.7, this format of print() function are still supported.

# if we execute the following python code via the terminal. but not the 
# IDLE, the working directory will not changed, we need to execute this line 
# of code in IDLE, or python console in terminal, only in that way,
# the working directory can change to the place we want.
os.chdir('/Users/scguo/python_work_dir/python_data_test/') # change to the absolute directory we defined.

# Converting an Integer to a String in any base
# we implement this function in recursive way
def convertInt2Str(num):






























