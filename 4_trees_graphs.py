# Eusebius N.

# 4.1
# Check if a binary tree is balanced

class BTreeNode(object):
	"""Binary Tree Node"""
	def __init__(self, data):
		super(BTreeNode, self).__init__()
		self.data = data
		self.left = None
		self.right = None

	def insert(self, newData):
		if newData < self.data:
			if self.left == None:
				self.left = BTreeNode(newData)
			else:
				self.left.insert(newData)
		else:
			if self.right == None:
				self.right = BTreeNode(newData)
			else:
				self.right.insert(newData)

	def isBalanced(self):
		return abs(self._height(self.left) - self._height(self.right)) <= 1

	def _height(self, subtree):
		if subtree == None:
			return 0
		leftHeight = self._height(subtree.left)
		rightHeight = self._height(subtree.right)
		return 1 + max(leftHeight, rightHeight)

	def printNode(self):
		print self.data

	def printTree(self):
		printTree(self.left)
		self.printNode()
		printTree(self.right)

## Testing
def testOutput(observed, expected=None):
	if isinstance(observed, type(expected)) and observed == expected:
		print "Pass"
	else:
		print "Fail:", observed, "instead of", expected

t = BTreeNode(0)
testOutput(t.isBalanced(), True)

testData = [1, 2, -1, 0.5]
expecting = [True,False,True,True,True]

for testDatum, expectedResult in zip(testData, expecting):
	t.insert(testDatum)
	testOutput(t.isBalanced(), expectedResult)


# 4.9
# All paths in a binary tree that sum to a value

def findPathsWithSum(tree, value):
	if tree == None:
		return [] #########

	if tree.data == value:
		return [tree.data]
	
	lSolutions = findPathsWithSum(tree.left, value)
	if lSolutions:
		lSolutions = [tree.data] + lSolutions
	
	rSolutions = findPathsWithSum(tree.right, value)
	if rSolutions:
		rSolutions = [tree.data] + rSolutions
	
	return lSolutions + rSolutions

print findPathsWithSum(t, 1.5)