# demonstrate the usage of the magic method that implemented in python
class FooBar:
	def __init__(self):
		self.somevar = 42

f = FooBar()
print "the variables that defined by the constructor of FooBar are : ", f.somevar

class FooBar_2:
	def __init__(self, value = 45):
		self.somevar =  value

f = FooBar_2()
print f.somevar
f = FooBar_2("guoshichao") # give a string value to the value parameter
print f.somevar

# the class hierarchy and method override operations
class A:
	def hello(self):
		print "I am A: ", self
class B(A):
	# pass
	def hello(self):
		print "I am B"

class C(B):
	# def hello(shit):
		# print "I am guoshichao"
		pass

# test it
a = A()
b = B()
c = C()
a.hello()
b.hello()
c.hello()

# Override the constructor of the parent class
class Bird:
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry: 
			print "I am hungry, and I need some meat"
			# change the state of this sucking bird
			self.hungry = False
		else:
			print "then, fuck you off, sucker!"

# test
b = Bird()
b.eat()
print "I have eat the food"
b.eat()

# the bird's sub class
class SongBird:
	def __init__(self): # here, we have override the constructor of the Bird, and we need to invoke the super() method, otherwise, we cannot get the attribute of the Bird
		# Bird.__init__(self)	
		# super(SongBird, self).__init__()
		self.sound = "I am your little apple, and I am your litte apple"
	def singing(self):
		for i in range(3):
			print self.sound,
		print "fuck off"

sb = SongBird()
sb.singing()
# sb.eat()
# sb.eat()














































