# Author: Matthew Thompson
# Date: 11/5/15
# Implements a sample generator for use in Prior and Rejection sampling

class SampleGenerator():
	def __init__(self, bayesNet):
		self.bayesNet = bayesNet
		self.samples = []

	def generateSamples(self, probabilities):
		currentProbabilityIndex = -1
		while (currentProbabilityIndex < len(probabilities) - 1):
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

		print '\nSamples:'
		print '--------'
		for sample in self.samples:
			print sample

		print 'Number of samples: ' + str(len(self.samples)) + '\n'
		return self.samples