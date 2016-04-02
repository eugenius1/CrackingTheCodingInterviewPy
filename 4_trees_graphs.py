# Eusebius N.

# 4.1
# Check if a binary tree is balanced

class TreeNode(object):
	"""Binary Tree Node"""
	def __init__(self, data):
		super(TreeNode, self).__init__()
		self.data = data
		self.left = None
		self.right = None

	def isBalanced(self):
		return abs(self._height(self.left) - self._height(self.right)) <= 1

	def _height(self, subtree):
		if subtree == None:
			return 0
		leftHeight = _height(subtree.left)
		rightHeight = _height(subtree.right)
		return 1 + max(leftHeight, rightHeight)

	def printNode(self):
		print self.data

	def printTree(self):
		printTree(self.left)
		self.printNode()
		printTree(self.right)

## Testing
print TreeNode(0).isBalanced()