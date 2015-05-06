# the test of the else function
name = raw_input("So, what is you name :")
if name.endswith("chao"):
	print "is you guoshichao"
else:
	print "who are fucking you ???"


# another test
name_1 = raw_input("input you name here : ")
if "guoshichao" in name_1:
	print "fuck you again"
else:
	print "who the fuck are you?"

# test the while loop
i = 0
while i < 100:
	print "guoshichao : " 
	i += 1
	print i

name = "" # if we declare name as " ", not "", then the while loop will not execute, as the condition is
		  # not false
while not name :
	name = raw_input("input you name : ")
print "Hello %s !" % name

words = ["fuck ", 'the ', 'world', range(100)]
for word in words:
	print word, # add "," in the end of this line to make the print out in the same line.


# iterate over the dict
# the following are just using techniques
# the python should have provide some built-feature to support this
# operation directly --> we could use zip() to accomplish this
names = ['guoshichao', 'guoshihua', 'guoshiping']
ages = [12, 13, 14]
for i in range(len(names)):
	print names[i], "is : ", ages[i], 'years old'

# the following code accomplish the same function as the 
# one above here.
zip(names, ages)

for name, age in zip(names, ages):
	print name, " are : ", age, " years old",

# break the infinite loop
from math import sqrt
for n in range(99, 0, 1):
	root = sqrt(n)
	if root == int(root):
		print n
		break























































