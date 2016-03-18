# Eusebius N.

# 1.1
# Optimal: O(n) time and O(1) space		Hint: bool
def all_unique1(string):
	''' for better time
		O(n) space
		O(n.log n) time
	'''

	string = sorted(string)

	for i in xrange(len(string -1)):
		if string[i] == string[i+1]:
			return False
	return True


def all_unique2(string):
	''' for better space
		O(1) additional space
		O(n^2) time
	'''

	n = len(string)
	for i in xrange(n-1):
		for j in xrange(i+1, n):
			if string[i] == string[j]:
				return False
	return True


# 1.8
# Should be isRotation(s1, s2)
def isSubstring(s1, s2): # s2 is substring of s1
	if len(s2) > len(s1):
		return False

	if s1.find(s2) != -1:
		return True

	# check for rotation
	for i in xrange(1, len(s2)):
		
		if (s1[-i:] != s2[:i]) and (s1[:i] != s2[-i:]):
			return True

