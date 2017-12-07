
import re
from collections import defaultdict

'''
Build a tree that looks like
 {
	node: {
		weight: int,
		children: list,
	}
 }
'''
def BuildTree(lst):
	tree = defaultdict(dict)
	p = re.compile('([a-z]*)\((\d*)\)(?:->(.*))?')
	for line in lst:
		m = p.match(line)
		node, weight, children = m.groups()
		if children:
			children = children.split(',')
			for child in children:
				tree[child]['parent'] = node
		else:
			children = []
		tree[node]['weight'] = int(weight)
		tree[node]['children'] = children
	return tree

'''
Find the root of the tree
'''
def FindRoot(tree):
	node = next(iter(tree))
	while 'parent' in tree[node]:
		node = tree[node]['parent']
	return node

'''
Find the total weight of this node (and all progeny) where total weight is defined as
sum of weight of the node and total weight of all children
'''
def FindTotalWeight(tree, node):
	for child in tree[node]['children']:
		if not 'total_weight' in tree[child]:
			FindTotalWeight(tree, child)
	tree[node]['total_weight'] = tree[node]['weight'] + sum([tree[child]['total_weight'] for child in tree[node]['children']])
	return

'''
Find which node needs it's weight fixed so the tree is 'balance' and what it should
be fix to
'''
def FixWeight(tree, node):
	child_weights = [tree[child]['total_weight'] for child in tree[node]['children']]
	while not all(x == child_weights[0] for x in child_weights):
		print node, tree[node], child_weights

		different_weight = [w for w in child_weights if child_weights.count(w) == 1][0]
		target_weight = [w for w in child_weights if child_weights.count(w) > 1][0]

		node = tree[node]['children'][child_weights.index(different_weight)]
		child_weights = [tree[child]['total_weight'] for child in tree[node]['children']]

	print node, tree[node], child_weights
	print "Node", node, "should have weight changed from", tree[node]['weight'], "by", target_weight - tree[node]['total_weight'], "to", tree[node]['weight'] + (target_weight - tree[node]['total_weight'])
	return


if __name__ == "__main__":
	with open('Dec-07.dat') as f:
		lst = [line.replace(" ", "") for line in f.read().splitlines()]
		tree = BuildTree(lst)
		root = FindRoot(tree)
		FindTotalWeight(tree, root)
		print root
		FixWeight(tree, root)

