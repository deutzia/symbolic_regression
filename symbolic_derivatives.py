import numpy as np
import sympy as sp

import lib.expressions as Expressions


def get_symbols_from_expr(expr, symbols_used):
	result = []
	for node in expr.get_nodes():
		if node in symbols_used:
			result.append(arg)
	return result

def get_deriviatives(expressions, data, symbols_used):
	result_for_all_expressions = []
	length = len(data[0])

	for exp in expressions:
		result = []
		deriviatives = []
		what_to_derive = get_symbols_from_expr(exp, symbols_used)

		# for variable in range(len(data)):
		# 	if symbols_used[variable] in what_to_derive:
		# 		deri_expression = exp.deriviative(symbols_used[variable].name)
		# 		deriviatives.append(deri_func(*data))
		# 	else:
		# 		deriviatives.append(np.zeros(length))

		for index in range(len(data)):
			if symbols_used[index] in what_to_derive:
				deriviative_function = exp.deriviative(symbols_used[index])
				for data_point in length:
					values = {}
					for i, variable in enumerate(symbols_used):
						values[symbols_used.name] = data[i][data_point]
					deriviatives.append(deriviative_function.get_value(values))
			else:
				deriviatives.append([0 for _ in range(length)])


		for sym1 in range(len(data)):
			for sym2 in range(sym1+1, len(data)):
				for index in range(length):
					val1 = deriviatives[sym1][index]
					val2 = deriviatives[sym2][index]
					if val1 == 0 or val2 == 0:
						result.append(0)
					elif not val1 or not val2:
						result.append(None)
					else:
						result.append(-val1 / val2)

		result_for_all_expressions.append(result)

	return result_for_all_expressions
