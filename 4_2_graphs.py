# Eusebius N.

# 4.2
# Find out if a route exists between two nodes in a directed graph

# a dictionary with keys matching nodes, and 
# each value is a list of nodes on a key node's outgoing edges
# this requires unique, hashable node identifiers

g = {9: [98, 96, 90], 0: [0],
 1: [19, 12], 2: [2, 20], 12: [123, 1], 20: [200], 123: []}

# Make sure all nodes are in graph as a key
nodes = set([])
for n, adjacents in g.items():
	nodes = nodes.union(set(adjacents))

for n in nodes:
	if n not in g:
		g[n] = []

print g

def nodesAreConnected(graph, start, end, visited=[]):
	"""Returns True if a route exists between two nodes in a directed graph,
	False otherwise.

	Return False if at least one of the nodes doesn't exist."""
	
	visited.append(start)

	if start not in graph or end not in graph:
		return False
	
	if start == end:
		return True

	if end in graph[start]:
		return True

	for adjacent in graph[start]:
		if adjacent in visited:
			continue
		
		result = nodesAreConnected(graph, adjacent, end, visited)
		if result == True:
			return result

	return False


def testOutput(observed, expected=None, printPasses=True):
	if isinstance(observed, type(expected)) and observed == expected:
		if printPasses:
			print "Pass"
		return True
	
	else:
		print "Fail:", observed, "instead of", expected
		return False

testInput = [(1, 19), (1, 123), (1, 2), (19, 1)]
expecting = [True, True, False, False]

assert len(testInput) == len(expecting)

for testDatum, expectedResult in zip(testInput, expecting):
	if not testOutput(nodesAreConnected(g, *testDatum), expectedResult, printPasses=True):
		print "^", testDatum
