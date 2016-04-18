#!/usr/bin/python
import time # get start and end time of function
import numpy as np # scientific computing library
import matplotlib.pyplot as plt # plotting

class SumSquareRegression:
	
	def __init__(self, data_set):

		self.data_set = data_set
		self.avg = self.data_avg(self.data_set)
		self.x_bar = self.avg[0]
		self.y_bar = self.avg[1]
		self.sxxy = self.calculate_sxxy(data_set, self.x_bar, self.y_bar)
		self.sxx = self.sxxy[0]
		self.sxy = self.sxxy[1]
		self.beta_1 = (self.sxy / self.sxx)
		self.beta_0 = (self.y_bar - self.beta_1 * self.x_bar)

	# O(n) time complexity
	# O(1) space complexity
	# Returns an array containing avg x and avg y values
	def data_avg(self, vector):
		start = time.clock()
		sum_x = 0
		sum_y = 0
		size = len(vector) 

		for i in range(0, len(vector) ):
			sum_x += vector[i][0]
			sum_y += vector[i][1]

		print "sum_x ", sum_x
		print "sum_y ", sum_y
		# type casting to return a decimal
		end = time.clock()
		print "Averaging Data took %f ms" % (end - start)
		return [float(sum_x)/size, float(sum_y)/size]

	# O(n) time complexity
	# O(1) space complexity
	# Returns S_xx and S_yy in an array respectively
	def calculate_sxxy(self, vector, x_bar, y_bar):
		start = time.clock()
		sxx_sum = 0
		sxy_sum = 0

		for i in range(0, len(vector) - 1):
			sxx_sum += (vector[i][0] - self.x_bar) ** 2
			sxy_sum += (vector[i][0] - self.x_bar) * (vector[i][1] - self.y_bar)

		end = time.clock()
		print "Calculating Sxx and Sxy took %f ms" % (end - start)
		return [sxx_sum, sxy_sum]

	# Prints stats related to regression
	def print_regression_stats(self):
		print "x_bar: %.2f" % self.x_bar
		print "y_bar: %.2f" % self.y_bar
		print "s_xx: %.2f" % self.sxx
		print "s_xy: %.2f" % self.sxy
		print "beta_0: %.2f" % self.beta_0
		print "beta_1: %.2f" % self.beta_1
		print "Regression Line: y = %.2fx + %.2f" % (self.beta_1, self.beta_0)

	def plot_data(self, data):
		x_list = [x for [x, y] in data]
		y_list = [y for [x, y] in data]
		plt.scatter(x_list, y_list)
		plt.ylabel('Test Scores')
		plt.xlabel('Time Spent Studying')
		plt.title('Test Scores vs Time Spent Studying')
		# plt.show()

	def plot_with_regression(self, data):
		# plot data
		x_list = [x for [x, y] in data]
		y_list = [y for [x, y] in data]
		plt.scatter(x_list, y_list)
		plt.ylabel('Test Scores')
		plt.xlabel('Time Spent Studying')
		# plot regression
		# uses python list comprehension
		y = [self.regression_approximation(x) for [x, y] in data]
		plt.plot(x_list, y)
		# print plot
		plt.title('Test Scores vs Time Spent Studying with Regression')
		# plt.show()		

	def regression_approximation(self, x):
		return (self.beta_1 * x) + (self.beta_0)

# Test Data
def main():
	sample_data_1 = [[4, 390],[9, 580],[10, 650],[14, 730],[4, 410],[7, 530],[12, 600],[1, 350],[3, 400],[8, 590],[11, 640],[5, 450],[6, 520],[10, 690],[11, 690],[16, 770],[13, 700],[13, 730]]
	regression_1 = SumSquareRegression(sample_data_1)
	regression_1.print_regression_stats()
	regression_1.plot_data(sample_data_1)
	regression_1.plot_with_regression(sample_data_1)

# Runs program automatically
if __name__ == '__main__':
	main()