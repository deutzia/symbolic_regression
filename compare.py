import math
import numpy as np

import lib.expressions as Expressions

def get_stuff(expr, symbols_used):
	num_of_trigo_functions = 0
	variables = set()

	for arg in expr.get_nodes():
		if isinstance(arg, (Expressions.Sin, Expressions.Cos)):
			num_of_trigo_functions += 1
		if isinstance(arg, Expressions.Variable):
			variables.add(arg.name)

	return num_of_trigo_functions, variables

def mean_log_error(expressions, num_devs, sym_devs, symbols_used):
	exps_with_values = []

	for expr in expressions:
		exps_with_values.append([expr, 0])

	for index in range(len(expressions)):
		cost = 0
		for i in range(1, len(num_devs)):
			val1 = num_devs[i]
			val2 = sym_devs[index][i]
			if val1 != None and val2 != None and val1 != 0 and val2 != 0:
				cost += math.log10(1+abs(val1 - val2))
			elif val1 == None or val2 == None:
				cost += 10

		size = expressions[index].get_tree_size()
		trigo, variables = get_stuff(expressions[index], symbols_used)
		size -= trigo/2
		cost += size*size
		cost += (len(symbols_used) - len(variables)) * 100
		exps_with_values[index][1] = cost

	exps_with_values.sort(key = lambda x: x[1])

	for index in range(len(expressions)):
		expressions[index] = exps_with_values[index][0]

def compare(expressions, num_devs, sym_devs, symbols_used):
	mean_log_error(expressions, num_devs, sym_devs, symbols_used)
