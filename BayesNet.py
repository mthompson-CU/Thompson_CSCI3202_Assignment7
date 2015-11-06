# Author: Matthew Thompson
# Date: 11/5/15
# Implements a Bayesian Network

import networkx as nx

class BayesNet():
	def __init__(self, distributions={}):
		self.graph = nx.DiGraph()
		for key in distributions:
			self.graph.add_node(str(key), distributions[key])

	def addDirectedEdge(self, source, destination):
		self.graph.add_edge(source, destination)