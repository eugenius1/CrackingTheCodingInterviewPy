# Eusebius N.

# 4.1
# Check if a binary (search) tree is balanced

class BSTreeNode(object):
	"""Binary Search Tree (BST) Node with ascending order, left to right."""

	def __init__(self, data):
		super(BSTreeNode, self).__init__()
		self.data = data
		self.left = None
		self.right = None

	def insert(self, newData):
		"""Insert new data while maintaining ascending order in the binary search tree"""

		if newData < self.data:
			if self.left == None:
				self.left = BSTreeNode(newData)
			else:
				self.left.insert(newData)
		else:
			if self.right == None:
				self.right = BSTreeNode(newData)
			else:
				self.right.insert(newData)

	
	def isBalanced(self):
		"""Check if the tree is balanced or not and return boolean.
		Tree is balanced if for each subtree, left and right heights don't differ by more than one"""

		return abs(self._height(self.left) - self._height(self.right)) <= 1

	def _height(self, subtree):
		"""Returns the height of a subtree.
		Empty tree has a height of 0. Leaf nodes are at a height of 1."""
		if subtree == None:
			return 0
		leftHeight = self._height(subtree.left)
		rightHeight = self._height(subtree.right)
		return 1 + max(leftHeight, rightHeight)

	def printNode(self, mode=0):
		"""Print node data followed by a new line (default mode 0).
		Mode 1 does not print a new line"""
		if mode == 0:
			print self.data
		else:
			print self.data, ",",

	def printTree(self):
		"""Print tree in order, from left to right.
		Each node is in a new line."""
		
		if self.left != None:
			self.left.printTree()
		self.printNode()
		if self.right != None:
			self.right.printTree()

	def printTreeLayers(self):
		"""Print tree by depth, from top root to bottom leaves.
		Each layer is in a new line."""

		layer = [self]

		while layer:
			nextLayer = []
			for node in layer:
				if node != None:
					node.printNode(mode=1)
					nextLayer.append(node.left)
					nextLayer.append(node.right)
				else:
					print ",",

			print   # new line
			layer = nextLayer
	

	def findPathsWithSum(self, value, forceRoot=False):
		"""4.9
		Return all paths in a binary (search) tree that sum to a value.
		
		Return a list of lists.
		This represents a list of paths, with each path being a list of node data.

		Path does not have to start at root node or end at a leaf node,
		but has to be a single continous sequence of nodes.
		"""

		if self.data == value:
			return [[self.data]] # one path
		
		# Left subtree
		if self.left == None: 
			lSolutions = []
		else:
			# paths including current node
			lSolutions = self.left.findPathsWithSum(value-self.data, forceRoot=True)
		
			for path in lSolutions:
				# prepend current node to all sub paths
				path.insert(0, self.data)
		
			if not forceRoot:
				# paths that start later on
				lSolutions += self.left.findPathsWithSum(value)
		
		# Right subtree
		if self.right == None: 
			rSolutions = []
		else:
			rSolutions = self.right.findPathsWithSum(value-self.data, forceRoot=True)
		
			for path in rSolutions:
				# prepend current node to all sub paths
				path.insert(0, self.data)
		
			if not forceRoot:
				rSolutions += self.right.findPathsWithSum(value)
		
		return (lSolutions + rSolutions) # remove empty paths
		#return filter(bool, lSolutions + rSolutions) # remove empty paths


## Testing
def testOutput(observed, expected=None, printPasses=True):
	if isinstance(observed, type(expected)) and observed == expected:
		if printPasses:
			print "Pass"
	else:
		print "Fail:", observed, "instead of", expected

t = BSTreeNode(0)
testOutput(t.isBalanced(), True)

testInput = [1, 2, -1, 0.5, 0.9, 0.6]
expectedBal = [1, 0, 1, 1, 0, 0]
expectedBal = map(bool, expectedBal)
assert len(testInput) == len(expectedBal)

for testDatum, expectedResult in zip(testInput, expectedBal):
	t.insert(testDatum)
	testOutput(t.isBalanced(), expectedResult, printPasses=False)



def findPathsWithSum2(tree, value, currSolutions=[]):
	"""4.9 alternative solution
	Return all paths in a binary (search) tree that sum to a value"""

	def appendCurrNode(solution):
		"""Return new list with current node appended to given solution path"""

		s=solution[:]       # a copy of the list
		s.append(tree.data)
		return s

	if tree == None:
		return []

	extendSolutions = currSolutions[:]
	if currSolutions: # if not empty list
		extendSolutions = map(appendCurrNode, currSolutions)
	else:
		extendSolutions = [[tree.data]]
	###print "extendS", extendSolutions

	if tree.data == value:
		return extendSolutions
	
	# Left subtree
	# paths including current node
	lSolutions = findPathsWithSum2(tree.left, value-tree.data, extendSolutions)
	
	if not currSolutions:
		# paths that start later on
		lSolutions += findPathsWithSum2(tree.left, value, [])
	
	# Right subtree
	rSolutions = findPathsWithSum2(tree.right, value-tree.data, extendSolutions)
	
	if not currSolutions:
		rSolutions += findPathsWithSum2(tree.right, value, [])
	
	return (lSolutions + rSolutions) # remove empty paths

t.printTreeLayers()

testSums = [0, -1, 1.5, 3]
for testSum in testSums:
	print t.findPathsWithSum(testSum)
	print findPathsWithSum2(t, testSum)
