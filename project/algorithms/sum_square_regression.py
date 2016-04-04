#!/usr/bin/python

class SumSquareRegression:
	
	def __init__(self,data_set):

		avg = data_avg(data_set)
		self.x_bar = avg[0]
		self.y_bar = avg[1]
		self.data_size = len(data_set)
		self.data_set = data_set
		self.xx = 
		self.yy = 

	# O(n) time
	# O(1) space
	def data_avg(vector):
		
		sum_x = 0
		sum_y = 0

		for i in range(0, vector):
			sum_x += vector[i]
			sum_y += vector[i]

	return [(sum_x/self.data_size, sum_y/self.data_size)]

	def calculate_xx():
		xx_sum = 0
		for i in range(0, self.data_size):
			xx_sum += (vector[i], self.x_bar)

		return xx_sum

main():
	

if __name__ == '__main__':
	main()