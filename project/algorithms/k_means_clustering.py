#!/usr/bin/python
import numpy as np # scientific computing library
import matplotlib.pyplot as plt # plotting
import random # used to generate random centroids

class KMeansClustering:

	def __init__(self, data_set, k):
		self.data_set = data_set
		self.k = k

	# for each point in data set,
	# find new subset it belongs too.
	def generate_clusters(self, mu):
	    clusters  = {}
	    for pt in self.data_set:
    		# for each pt in our data set 
    		# find best fitting val
				best_mu = min([(array[0], np.linalg.norm(pt - mu[array[0]])) \
									for array in enumerate(mu)], key = lambda t:t[1])[0]
				try:
					clusters[best_mu].append(pt)
				except KeyError:
					clusters[best_mu] = [pt]
	    return clusters
	 
	# calcuate new mu values
	def reevaluate_centers(self, mu, clusters):
	    new_mu = []
	    keys = sorted(clusters.keys())
	    for k in keys:
	        new_mu.append(np.mean(clusters[k], axis = 0))
	    return new_mu
	 
	def has_converged(self, mu, old_mu):
			# we know we have converged if our old and new mu values are the same
	    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in old_mu]))
	 
	def k_means(self):
	  # at first, randomize centroids 
		old_mu = random.sample(self.data_set, self.k)
		mu = random.sample(self.data_set, self.k)

		while not self.has_converged(mu, old_mu):
			old_mu = mu
	    
	    # assign pts in data_set to clusters
			clusters = self.generate_clusters(mu)
	    
	    # recalculate centers
			mu = self.reevaluate_centers(old_mu, clusters)

 		return(mu, clusters)



def main():
	# Notice this the same as the last dataset 
	# Instead of predictive modeling we'll use this data to split into
	# distinct ranges (think A, B, C, D, F) in this case
	sample_data_1 = np.array([[4, 390],[9, 580],[10, 650],[14, 730],[4, 410],[7, 530],[12, 600],[1, 350],[3, 400],[8, 590],[11, 640],[5, 450],[6, 520],[10, 690],[11, 690],[16, 770],[13, 700],[13, 730]])
	k = 5 # how many different clusters do we want?
	clustered = KMeansClustering(sample_data_1, k) # initialize object
	data = clustered.k_means()
	
	# parse data to plot
	centroids = data[0]
	clusters = data[1]
	i = 0
	for centroid in centroids:
		c = np.random.rand(3,1)
		s = 70, 
		plt.scatter(centroid[0],centroid[1], s, c, marker = '*')
		data = clusters[i]
		for pt in data:
			plt.scatter(pt[0],pt[1], s ,c)
		i += 1
	plt.xlabel('Time Studied')
	plt.ylabel('Test Score')
	plt.title('Clustered Time Studied - Test Score')
	plt.show()

if __name__ == '__main__':
	main()
