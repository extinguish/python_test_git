# the python tricks collections
def foo(x=[]):
	x.append(1)
	print x


for i in range(10) :
	foo()

def foo_1(x=None):
	x = x or []
	x.append(1)
	print x

for i in range(10):
	print('another way of append() methods'),
	foo_1()

# demonstrate the usage of the List opreations
print(list(reversed(range(100))))
print("use the tuple feature to reverse the array elements")
print([range(100)][::-1])
print([1, 2, 3, 4][::-1])
a = range(100)
print(a[::-1])
print(tuple(reversed(range(10))))
print(range(6))
teams = ['guosic', str(range(10)), "shit"]
print("We are going to join the string array elements into one array", ",".join(teams))



































