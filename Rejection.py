# Author: Matthew Thompson
# Date: 11/5/15
# Prints the estimates of the probabilites assignment in Assignment 7 writeup using Rejection Sampling

import SampleGenerator

class Rejection():
	def __init__(self, bayesNet):
		self.bayesNet = bayesNet
		return

	def calculateRejections(self, probabilities):
		sampleGenerator = SampleGenerator.SampleGenerator(self.bayesNet)
		samples = sampleGenerator.generateSamples(probabilities)

		print '\nRejection Sampling:'
		print '-------------------'	

		# P(cloudy  = true)
		cloudySamples = 0.0
		for sample in samples:
			if ('c' in sample and not '-c' in sample):
				cloudySamples += 1.0
		print 'P(cloudy = true): ' + str(cloudySamples / len(samples))

		# P(cloudy = true | rain = true)
		cloudyGivenRainSamples  = 0.0
		rainSamples = 0.0
		for sample in samples:
			if ('r' in sample and not '-r' in sample):
				rainSamples += 1.0
				if ('c' in sample  and not '-c' in sample):
					cloudyGivenRainSamples += 1.0
		print 'P(cloudy = true | rain = true): ' + str(cloudyGivenRainSamples / rainSamples)

		# P(sprinkler  = true | wet = true)
		sprinklerGivenWetSamples = 0.0
		wetSamples = 0.0
		for sample in samples:
			if ('w' in sample and not '-w' in sample):
				wetSamples += 1.0
				if ('s' in sample and not '-s' in sample):
					sprinklerGivenWetSamples += 1.0
		print 'P(sprinkler = true | wet = true): ' + str(sprinklerGivenWetSamples / wetSamples)

		# P(sprinkler = true | cloudy = true, wet = true)
		sprinklerGivenCloudyWetSamples = 0.0
		cloudySamples = 0.0
		wetSamples = 0.0
		for sample in samples:
			if ('c' in sample and not '-c' in sample and 'w' in sample and not '-w' in sample):
				cloudySamples += 1.0
				wetSamples += 1.0
				if ('s' in sample and not '-s' in sample):
					sprinklerGivenCloudyWetSamples += 1.0
		print 'P(sprinkler = true | cloudy = true, wet = true): ' + str(sprinklerGivenCloudyWetSamples / (cloudySamples + wetSamples))

		return
