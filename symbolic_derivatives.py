import numpy as np
import sympy as sp

import lib.expressions as Expressions


def get_symbols_from_expr(expr, symbols_used):
	result = []
	for node in expr.get_nodes():
		if node in symbols_used:
			result.append(node)
	return result

def get_derivatives(expressions, data, symbols_used):
	result_for_all_expressions = []
	length = len(data[0])

	for exp in expressions:
		result = []
		derivatives = []
		what_to_derive = get_symbols_from_expr(exp, symbols_used)

		for index in range(len(data)):
			if symbols_used[index] in what_to_derive:
				derivatives.append([])
				derivative_function = exp.derivative(symbols_used[index])
				for data_point in range(length):
					values = {}
					for i, variable in enumerate(symbols_used):
						values[symbols_used[i].name] = data[i][data_point]
					try:
						derivatives[-1].append(derivative_function.get_value(values))
					except ValueError: # this means division by zero
						derivatives[-1].append(None)
			else:
				derivatives.append([0 for _ in range(length)])


		for sym1 in range(len(data)):
			for sym2 in range(sym1+1, len(data)):
				for index in range(length):
					val1 = derivatives[sym1][index]
					val2 = derivatives[sym2][index]
					if val1 == 0 or val2 == 0:
						result.append(0)
					elif not val1 or not val2:
						result.append(None)
					else:
						result.append(-val1 / val2)

		result_for_all_expressions.append(result)

	return result_for_all_expressions
