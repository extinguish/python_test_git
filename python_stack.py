# Using the python to implement the basic stack data structure
class Stack :
	def __init__(self) :
		self.items = []

	def isEmpty(self) :
		return self.items == []

	def push(self, item) :
		self.items.append(item)

	def pop(self) :
		return self.items.pop()

	def peek(self) :
		return self.items[len(self.items) - 1]

	def size(self) :
		return len(self.items)

# test the stack we created
# s = Stack()

# # print s.isEmpty()
# s.push(str(100))
# s.push('guoshichao')
# s.push('guoshichao_shendan')
# s.push('guoshichao_lover')

# for i in range(0, 2) :
# 	s.pop()
# 	print s.peek()

# print s.size()

print "+++++++++++++++++++++++use stack to test the parentheses+++++++++++++++++++++++++++++++++"
# in the following part, we will using python to implement a balanced parentheses
# to calculate the (5 + 6) * (7 + 8) / (4 + 3)
from python_stack import Stack
def parChecker(symbolStr) :
	print "the parentheses we need to check are : ", symbolStr
	s = Stack()
	# print Stack()
	balanced = True
	index = 0
	while index < len(symbolStr) and balanced:
		symbol = symbolStr[index]
		if symbol == "(" :
			s.push(symbol)
		else : # the symbol is not "(", it could be ")", or something else, of which we do not care
			if s.isEmpty():
				balanced = False
			else :
				s.pop()
		
		index = index + 1

	if balanced and s.isEmpty :
		return True
	else :
		return False

# print parChecker("()()()()()()()()()(")
# print parChecker("(((((((()))")


print "======================the new version=============================="

from python_stack import Stack
def parChecker_1(symbolString):
    s = Stack()
    # print Stack()
    print "the symbol collection we need to check are : %s " % symbolString
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print parChecker_1("(((((()")
print parChecker_1("()()()()()()()()()(")
print parChecker_1("()()()()()")

print "-------------------------the end----------------------------------"












































