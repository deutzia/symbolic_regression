from __future__ import print_function
import sympy as sp
import time

import simulate
import numerical_derivatives
import generate_expressions
import symbolic_derivative
import compare
import crossover
import mutate

def main():
	timestep = 1.0/20
	number_of_seconds = 20
	number_of_expressions = 100
	operations_binary = [sp.Add, sp.Mul]
	operations_unary =  [sp.sin, sp.cos]
	dimensions = 1
	data = simulate.simulate(timestep, number_of_seconds)
	expressions, symbols_used = generate_expressions.generate_expressions(
		number_of_expressions, dimensions)
	num_devs = numerical_derivatives.get_deriviatives(data, timestep)
	for i in range(10):
		print("{} iteratrion {}: ".format(time.clock(), i))
		sym_devs = symbolic_derivative.get_deriviatives(expressions, data,
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
	main()
