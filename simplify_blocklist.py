#! /usr/bin/python

import sys

from optparse import OptionParser

parser = OptionParser()

parser.add_option('-f', action = 'store_true', help = 'One or more blocklist files to simplify')
parser.add_option('-u', action = 'store_true', help = 'One or more blocklist urls to simplify')

(options, args) = parser.parse_args()


class Node(object):
	""" Node

	Attributes:
		auth (str): The authority of this Node.
		children (dict of Node): The children of this Node.
	"""

	def __init__(self, auth):
		""" Constructor

		Args:
			auth (str): The authority of the current node.

		"""
		self.auth = auth
		self.children = None;


	def add_children(self, auth):
		""" Adds a new node for auth if none already exists

		Args:
			auth (str): The authority of the child node

		Returns:
			Node: The node added or the previously existing node
		"""

		if self.children is None:
			self.children = dict()

		if self.children.get(auth) is None:
			self.children[auth] = Node(auth)

		return self.children[auth]


def add_url(root, url):
	""" Adds a new url to the tree with root root

	Args:
		root (Node): The root of the hosts tree.
		url (str): The URL to be added.

	"""

	url = url.split('.')

	current = root

	for auth in reversed(url):
		current = current.add_children(auth)

		if current.children is not None and len(current.children) == 0:
			break

	current.children = dict()



def tree_as_host_list(current, path):
	"""

	Args:
		current (Node): The root of the subtree.
		path (str): path from the root to the current Node.

	Returns:
		str: The list representation of the hosts in current

	"""

	if len(current.children) == 0:
		return path 

	p = str()

	for i in current.children.values():

		p += tree_as_host_list(i, i.auth + '.' + path if path != '\n' else i.auth + path)

	return p

def tree_as_tree(root):
	"""

	Args:
		root (Node): The root of the tree.

	Returns:
		str: The tree representation of the hosts in root

	"""
	stack = list()

	stack.append((root, 0))

	p = str()

	while len(stack) > 0:
		current, depth = stack.pop()

		for _ in range(depth):
			p += '# '

		p += current.auth + '\n'

		stack.extend([(x, depth + 1) for x in current.children.values()])

	return p


def from_files():
	"""

	Reads filenames from stdin, opens them and builds the tree
		
	"""
	root = Node('.')

	for file in sys.stdin:
		with open(file.strip()) as f:
			lines = f.readlines()
		lines = [x.strip() for x in lines]
		for i in lines:
			add_url(root, i)

	print tree_as_host_list(root, '\n')

def from_urls():
	"""

	Reads urls from stdin, opens them and builds the tree
		
	"""
	print("Read from urls not yet implemented")

def from_input():
	"""

	Reads blocklist from stdin and builds the tree
		
	"""
	root = Node('.')

	for url in sys.stdin:
		add_url(root, url.strip())

	print tree_as_host_list(root, '\n')


def main():

	if options.f and options.u:
	    parser.error("options -f and -u are mutually exclusive")

	if options.f:
		from_files()
	elif options.u:
		from_urls()
	else:
		from_input()



if __name__ == "__main__":
	main()




