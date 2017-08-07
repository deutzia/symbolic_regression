from __future__ import print_function
import sympy as sp
import sys
import time

import numerical_derivatives
import generate_expressions
import symbolic_derivatives
import compare
import crossover
import mutate

def get_data(file):
	data = []
	data_raw = file.read().split("\n")[:-1]
	for record in data_raw:
		data.append([])
		record_raw = record.split(" ")
		for number in record_raw:
			try:
				data[-1].append(float(number))
			except:
				import pdb
				pdb.set_trace()
	return data

def main(file):
	"""Data should consist of records separated by linux newline characters.
	Each record should consist of data (numbers) for consecutive steps fo time.
	There should be records for: position, velocity, acceleration.
	Example data (for oscilator with equation of motion a = -x) can be found in
	data.txt file"""
	timestep = 1/20
	number_of_expressions = 100
	operations_binary = [sp.Add, sp.Mul]
	operations_unary =  [sp.sin, sp.cos]
	# Only one dimension is supported now
	dimensions = 1
	number_of_iterations = 100

	data_file = open(file, "r")
	data = get_data(data_file)
	data_file.close()
	expressions, symbols_used = generate_expressions.generate_expressions(
		number_of_expressions, dimensions)
	num_devs = numerical_derivatives.get_deriviatives(data, timestep)

	for i in range(number_of_iterations):
		print("{} iteratrion {}: ".format(time.clock(), i))

		sym_devs = symbolic_derivatives.get_deriviatives(expressions, data,
			symbols_used)
		compare.compare(expressions, num_devs, sym_devs, symbols_used)
		expressions = expressions[len(expressions)//2:]

		crossover.crossover(expressions, number_of_expressions, dimensions)
		mutate.mutate(expressions,operations_binary,operations_unary,
			symbols_used)

	expressions = expressions[len(expressions)//10:]
	for exp in expressions:
		print(exp)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1])
