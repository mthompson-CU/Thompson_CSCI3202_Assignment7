# Author: Matthew Thompson
# Date: 11/5/15
# Assignment 7 

import sys
import BayesNet
import Prior
import random

def readProbabilities(inputFile):
	probFile = open(inputFile, 'rb')
	probabilities = []
	for line in probFile:
		lineProbabilities = line.split(',')
		for probability in lineProbabilities:
			probabilities.append(float(probability))

	return probabilities

def createBayesNet():
 	distributions = {'cloudy': {'true': 0.5, 'false': 0.5}, 'sprinkler': {'true': 0.1, 'false': 0.5}, 'rain': {'true': 0.8, 'false': 0.2}, 'wet': {'tt': 0.99, 'tf': 0.9, 'ft': 0.9, 'ff': 0.0}}
		
	bayesNet = BayesNet.BayesNet(distributions)

	bayesNet.addDirectedEdge('cloudy', 'sprinkler')
	bayesNet.addDirectedEdge('cloudy', 'rain')
	bayesNet.addDirectedEdge('sprinkler', 'wet')
	bayesNet.addDirectedEdge('rain', 'wet')

	return bayesNet

def main (argv):
	probabilities = readProbabilities(argv[1])

	# probabilities = []
	# for x in range(100):
	# 	probabilities.append(random.random())

	bayesNet = createBayesNet()

	prior = Prior.Prior(bayesNet)
	prior.calculatePriors(probabilities)

	return

if __name__ == '__main__':
	main(sys.argv)