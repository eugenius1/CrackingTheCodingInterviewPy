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

	def printNode(self, mode=0):
		if mode == 0:
			print self.data
		else:
			print self.data,

	def printTree(self):
		if self.left != None:
			self.left.printTree()
		self.printNode()
		if self.right != None:
			self.right.printTree()

	def printTreeLayers(self):
		self.printNode(mode=1)
		
		if self.left == None:
			printLeft = False
		else:
			printLeft = True
		if self.right == None:
			printRight = False
		else:
			printRight = True

		if printLeft:
			self.left.printNode()
		if printRight:
			self.right.printNode()

		if printLeft:
			self.left.printTreeLayers()
		if printRight:
			self.right.printTreeLayers()

## Testing
def testOutput(observed, expected=None):
	if isinstance(observed, type(expected)) and observed == expected:
		print "Pass"
	else:
		print "Fail:", observed, "instead of", expected

t = BTreeNode(0)
testOutput(t.isBalanced(), True)

testInput = [1, 2, -1, 0.5]
expectedBal = [True,False,True,True,True]


for testDatum, expectedResult in zip(testInput, expectedBal):
	t.insert(testDatum)
	#testOutput(t.isBalanced(), expectedResult)


# 4.9
# All paths in a binary tree that sum to a value

def findPathsWithSum(tree, value, curr_solutions=[]):
	if tree == None:
		return [] # no paths

	if tree.data == value:
		return [[tree.data]] # one path
	
	# Left subtree
	# paths including current node
	lSolutions = findPathsWithSum(tree.left, value-tree.data)
	for path in lSolutions:
		# prepend current node to all sub paths
		path.insert(0, tree.data)
	
	# paths that start later on
	lSolutions += findPathsWithSum(tree.left, value)
	
	# Right subtree
	rSolutions = findPathsWithSum(tree.right, value-tree.data)
	for path in rSolutions:
		# prepend current node to all sub paths
		path.insert(0, tree.data)
	rSolutions += findPathsWithSum(tree.right, value)
	
	return (lSolutions + rSolutions) # remove empty paths
	#return filter(bool, lSolutions + rSolutions) # remove empty paths

#t.printTree()

testSums = [0, -1, 1.5, 3]
for testSum in testSums:
	print findPathsWithSum(t, testSum)
