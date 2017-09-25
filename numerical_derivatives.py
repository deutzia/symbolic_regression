import numpy as np

def get_derivatives(data, timestep):
	result = []
	derivatives = []
	length = len(data[0])

	for variable in range(len(data)):
		derivatives.append([None])
		for index in range(1, length):
			derivatives[variable].append(
				(data[variable][index] - data[variable][index-1]) / timestep)

	for sym1 in range(len(data)):
		for sym2 in range(sym1+1, len(data)):
			for index in range(length):
				val1 = derivatives[sym1][index]
				val2 = derivatives[sym2][index]
				if val1 == 0 or val2 == 0:
					result.append(0)
				elif val1 == None or val2 == None:
					result.append(None)
				else:
					result.append(val1 / val2)
	return result
