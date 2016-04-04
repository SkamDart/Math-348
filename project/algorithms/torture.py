#!/usr/bin/python

def main():
	list = [[4,390],[9,580],[10,650],[14,730],[4,410],[7,530],[12,600],[22,790],[1,350],[3,400],[8,590],[11,640],[5,450],[6,520],[10,690],[11,690],[16,770],[13,700],[13,730],[10,64]]

	sum_x = 0
	sum_y = 0
	for i in list:
		sum_x += i[0]
		sum_y += i[1]

	print len(list)
	print sum_x
	print sum_y
	print float(sum_x)/len(list)
	print float(sum_y)/len(list)
if __name__ == '__main__':
	main()