# Author: Matthew Thompson
# Date: 11/5/15
# Prints the estimates of the probabilites assignment in Assignment 7 writeup using Prior Sampling

class Prior():
	def __init__(self, bayesNet):
		self.bayesNet = bayesNet
		self.samples = []

	def generateSamples(self, probabilities):
		currentProbabilityIndex = -1
		while (currentProbabilityIndex < len(probabilities) - 4):
			currentProbabilityIndex += 1
			# Cloudy true
			if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['cloudy']['true']):
				currentProbabilityIndex += 1
				# Sprinkler true
				if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['sprinkler']['true']):
					currentProbabilityIndex += 1
					# Rain true
					if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['rain']['true']):
						currentProbabilityIndex += 1
						# Wet true
						if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['wet']['tt']):
							self.samples.append('+c, +s, +r, +w')
						# Wet false
						elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['wet']['tt']):
							self.samples.append('+c, +s, +r, -w')
					# Rain false
					elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['rain']['true']):
						currentProbabilityIndex += 1
						# Wet true
						if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['wet']['tf']):
							self.samples.append('+c, +s, -r, +w')
						# Wet false
						elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['wet']['tf']):
							self.samples.append('+c, +s, -r, -w')
				# Sprinkler false
				elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['sprinkler']['true']):
					currentProbabilityIndex += 1
					# Rain true
					if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['rain']['true']):
						currentProbabilityIndex += 1
						# Wet true
						if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['wet']['ft']):
							self.samples.append('+c, -s, +r, +w')
						# Wet false
						elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['wet']['ft']):
							self.samples.append('+c, -s, +r, -w')
					# Rain false
					elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['rain']['true']):
						currentProbabilityIndex += 1
						# Wet true
						if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['wet']['ff']):
							self.samples.append('+c, -s, -r, +w')
						# Wet false
						elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['wet']['ff']):
							self.samples.append('+c, -s, -r, -w')
			# Cloudy false
			elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['cloudy']['true']):
				currentProbabilityIndex += 1
				# Sprinkler true
				if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['sprinkler']['false']):
					currentProbabilityIndex += 1
					# Rain true
					if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['rain']['false']):
						currentProbabilityIndex += 1
						# Wet true
						if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['wet']['tt']):
							self.samples.append('-c, +s, +r, +w')
						# Wet false
						elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['wet']['tt']):
							self.samples.append('-c, +s, +r, -w')
					# Rain false
					elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['rain']['false']):
						currentProbabilityIndex += 1
						# Wet true
						if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['wet']['tf']):
							self.samples.append('-c, +s, -r, +w')
						# Wet false
						elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['wet']['tf']):
							self.samples.append('-c, +s, -r, -w')
				# Sprinkler false
				elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['sprinkler']['false']):
					currentProbabilityIndex += 1
					# Rain true
					if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['rain']['false']):
						currentProbabilityIndex += 1
						# Wet true
						if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['wet']['ft']):
							self.samples.append('-c, -s, +r, +w')
						# Wet false
						elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['wet']['ft']):
							self.samples.append('-c, -s, +r, -w')
					# Rain false
					elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['rain']['false']):
						currentProbabilityIndex += 1
						# Wet true
						if (probabilities[currentProbabilityIndex] < self.bayesNet.graph.node['wet']['ff']):
							self.samples.append('-c, -s, -r, +w')
						# Wet false
						elif (probabilities[currentProbabilityIndex] >= self.bayesNet.graph.node['wet']['ff']):
							self.samples.append('-c, -s, -r, -w')

		return

	def calculatePriors(self, probabilities):
		self.generateSamples(probabilities)

		print 'Prior Sampling:'
		print '---------------'
		for sample in self.samples:
			print sample

		print 'Number of samples: ' + str(len(self.samples)) + '\n'

		# P(cloudy  = true)
		cloudySamples = 0.0
		for sample in self.samples:
			if ('c' in sample and not '-c' in sample):
				cloudySamples += 1
		print 'P(cloudy = true): ' + str(cloudySamples / len(self.samples))

		# P(cloudy = true | rain = true)
		cloudyGivenRainSamples  = 0.0
		for sample in self.samples:
			if ('r' in sample and not '-r' in sample):
				if ('c' in sample and not '-c' in sample):
					cloudyGivenRainSamples += 1
		print 'P(cloudy = true | rain = true): ' + str(cloudyGivenRainSamples / len(self.samples))

		# P(sprinkler  = true | wet = true)
		sprinklerGivenWetSamples  = 0.0
		for sample in self.samples:
			if ('w' in sample and not '-w' in sample):
				if ('s' in sample and not '-s' in sample):
					sprinklerGivenWetSamples += 1
		print 'P(sprinkler = true | wet = true): ' + str(sprinklerGivenWetSamples / len(self.samples))

		# P(sprinkler = true | cloudy = true, wet = true)
		sprinklerGivenCloudyWetSamples = 0.0
		for sample in self.samples:
			if ('c' in sample and not '-c' in sample):
				if ('w' in sample and not '-w' in sample):
					if ('s' in sample and not '-s' in sample):
						sprinklerGivenCloudyWetSamples += 1
		print 'P(sprinkler = true | cloudy = true, wet = true): ' + str(sprinklerGivenCloudyWetSamples / len(self.samples))

		return
