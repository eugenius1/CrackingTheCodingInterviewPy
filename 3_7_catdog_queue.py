# Eusebius N.

from collections import deque

# 3.7
# Implement a system for an animal shelter with cats and dogs,
# operating under a strict 'first in, first out' basis

# Current implementation can be improved (look-up time)
# by keeping track of the first of each type of animal.
# Code complexity increases in enqueuing and deqeuing

class Animal(object):
	verbose = False

	def __init__(self, name = None, ID = None):
		super(Animal, self).__init__()
		if ID == None:
			self.ID = id(self)
		else:
			self.ID = ID
		
		self.name = name

	def __str__(self):
		s=str(self.__class__.__name__)+' id#'+str(self.ID)
		if self.name != None:
			s += ' called ' + str(self.name)
		return s

	def __repr__(self):
		if self.verbose:
			s='Animal(type='+str(self.__class__.__name__)+\
				', id='+str(self.ID)+', name='+str(self.name)+')'
		else:
			s='('+str(self.__class__.__name__)+', '+\
				str(self.ID)+', '+str(self.name)+')'

		return s


class Dog(Animal):
	def __init__(self, *args, **kwargs):
		super(Dog, self).__init__(*args, **kwargs)


class Cat(Animal):
	def __init__(self, *args, **kwargs):
		super(Cat, self).__init__(*args, **kwargs)


class Queue(object):
	"""Queue data structure, implemented using collections.deque"""
	def __init__(self):
		super(Queue, self).__init__()
		self._q = deque([])
		
	def enqueue(self, animal):
		self._q.append(animal)

	def dequeueAny(self):
		return self._q.popleft()

	def dequeueDog(self):
		'''Returns None if no dogs in queue'''
		return self._dequeue_animal(Dog)

	def dequeueCat(self):
		return self._dequeue_animal(Cat)

	def _dequeue_animal(self, AnimalType):
		first_match = None
		for a in self._q:
			if isinstance(a, AnimalType):
				first_match = a

		if first_match != None:
			self._q.remove(first_match)
		return first_match

	def __print_all(self):
		print self._q


####### Testing
q = Queue()
q.enqueue(Dog())
q.enqueue(Dog('Shaggy'))
q.enqueue(Cat('Pussy', 314159265358979))

q._Queue__print_all() # name mangling of private method

print q.dequeueAny()
print q.dequeueCat()
print q.dequeueDog()

# Empty queue
print q.dequeueCat()
