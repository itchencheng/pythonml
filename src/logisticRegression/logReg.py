# @author: chencheng
# @title : logReg.py
# @data  : 20180326

import numpy as np

''' activation function '''
def sigmoid(x):
	result = 1 / (1 + np.exp(-x))
	return result


''' batch gradient descent '''
def batch_GD(dataSetX, dataSetY, alpha=0.001, iteration=500):
	example_num = dataSetX.shape[0]
	feature_num = dataSetX.shape[1]
	
	weights = np.ones((feature_num,1))
	dataSetY = dataSetY.reshape((example_num, 1))
	''' iterations '''
	for i in range(iteration):
		tmpY = sigmoid( np.dot(dataSetX, weights) )
		delta = tmpY - dataSetY
		weights = weights - alpha * np.dot(dataSetX.T, delta)
	return weights


''' stochastic gradient descent '''
def stochastic_GD():
	return 0


''' mini-batch gradient descent '''
def mini_batch_GD():
	return 0