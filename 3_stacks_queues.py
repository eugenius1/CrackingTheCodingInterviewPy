# Eusebius N.

# Stack = LIFO = Last In First Out
# Queue = FIFO = First In First Out

# 3.1
# Array implementing 3 stacks:
## Split the array into 3 fixed stacks
## or more complex: stacks with varying starting positions

## or grow first downwards, third upwards,
## and the middle stack has a varying starting position



# 3.2
# Stack with push, pop and min; all in O(1) time

class Stack(object):
	"""Stack data structure, implemented using a list"""
	def __init__(self):
		super(Stack, self).__init__()
		self._list = []
		self._min = None
		self._min_count = 0

	def push(self, data):
		self._list.append(data)

		# data is the only element
		if self._min == None:
			self._min = data
			self._min_count = 1
		
		# data value is same as min
		elif data == self._min:
			self._min_count += 1
		
		# new min
		elif data < self._min:
			self._min = data

	def pop(self):
		try:
			to_pop = self._list.pop()
		except IndexError:
			raise LookupError('pop from empty stack')

		# data to be popped is min
		if to_pop == self._min:
			# last element
			if len(self._list) == 0:
				self._min = None
				self._min_count = 0
			
			# find new min if this is the last min
			elif self._min_count <= 1:
				self._find_min()
			
			else:
				self._min_count -= 1

		return to_pop

	def peek(self):
		try:
			return self._list[-1]
		except IndexError:
			raise LookupError('peek from empty stack')
	
	def min(self):
		return self._min
		
	def _find_min(self):
		self._min = min(self._list)
		self._min_count = self._list.count(self._min)
		return 'Naughty indeed'

### Test 3.2
s = Stack()

test_data = [0, 3.14, -2.7]
for n in test_data:
	s.push(n)

print 'min', s.min()
print 'popped', s.pop()
print 'peek', s.peek()
print 'new min', s.min()
print 'popped', s.pop()
print 'popped', s.pop()

# empty stack errors
print s.pop()
#print s.min()
#print s.peek()
