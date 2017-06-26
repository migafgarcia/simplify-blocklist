#! /usr/bin/python

import sys

from optparse import OptionParser

# TODO: user optparse to parse options

class Node(object):

	def __init__(self, auth):
		self.auth = auth
		self.children = None;

	def add_children(self, auth):
		if self.children is None:
			self.children = dict()

		if self.children.get(auth) is None:
			self.children[auth] = Node(auth)

		return self.children[auth]


def add_url(root, url):
	url = url.split('.')

	current = root

	for auth in reversed(url):
		current = current.add_children(auth)

		if current.children is not None and len(current.children) == 0:
			break

	current.children = dict()

def print_list(current, path):

	if len(current.children) == 0:
		return path 

	p = str()


	for i in current.children.values():

		p += print_list(i, i.auth + '.' + path if path != '\n' else i.auth + path)

	return p

if __name__ == "__main__":
	root = Node('.')

	with open(sys.argv[1]) as f:
		lines = f.readlines()

	lines = [x.strip() for x in lines]


	for i in lines:
		add_url(root, i)

	print print_list(root, '\n')


