# Eusebius N.

import time as t

class Node(object):

	def __init__(self, d):
		self.data = d
		self.next = None

	def appendToTail(self, d):
		n = self
		while (n.next is not None):
			n = n.next

		n.next = Node(d)
		#return n.next

	def printNode(self):
		print self.data

	def printAll(self):
		n = self
		while n is not None:
			print n.data
			n = n.next

	def delete(self):
		# effectively deleting in Python
		return self.next


# 2.1
def removeDups(head):
	'''
	O(n) space and time
	'''
	buff = set([])
	n = head
	while n is not None:
		d = n.data
		if d in buff:	# never true with n = head
			prev.next = n.delete()
			n = prev.next
		else:
			buff.add(d)
			prev = n 	# important! to be inside else
			n = n.next

def removeDups2(head):
	''' no buffer
	O(1) space
	O(n^2) time
	'''
	n = head
	while (n is not None):
		ahead = n.next	# will be advanced at start of inner while-loop
		prev = n
		d = n.data
		
		while(ahead is not None):			
			if ahead.data is d:
				prev.next = ahead.delete()
				ahead = prev.next
			else:
				prev = ahead
				ahead = ahead.next
		n = n.next

ll = Node(-1)
for d in [3, 3, -5.1, -1]:
	ll.appendToTail(d)

#removeDups(ll)
#ll.printAll()


# 2.7
def reverse_list(head):
	def reverse_list_helper(old_head, new_head):
		''' returns head of reversed list'''

		# end of forward list reached, reversing is complete
		if old_head is None:
			return new_head

		# make first node safe to break off
		next = old_head.next
		
		# current (forward) node prepended to reverse list
		old_head.next = new_head

		# reverse remaining forward list
		return reverse_list_helper(next, old_head)


	return reverse_list_helper(head, None)

reverse_list(ll).printAll()
