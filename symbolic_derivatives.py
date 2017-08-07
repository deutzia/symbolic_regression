import numpy as np
import sympy as sp

def get_symbols_from_expr(expr, symbols_used):
	result = []
	for arg in sp.preorder_traversal(expr):
		if arg in symbols_used:
			result.append(arg)
	return result

def get_deriviatives(expressions, data, symbols_used):
	result_for_all_expressions = []
	length = len(data[0])
	for exp in expressions:
		result = []
		deriviatives = []
		what_to_derive = get_symbols_from_expr(exp, symbols_used)
		for variable in range(len(data)):
			if symbols_used[variable] in what_to_derive:
				deri_expression = sp.diff(exp, symbols_used[variable], 1)
				deri_func = np.vectorize(sp.lambdify(tuple(symbols_used),
					deri_expression, "numpy"))
				deriviatives.append(deri_func(*data))
			else:
				der = []
				for i in range(len(data[0])):
					der.append(None)
				deriviatives.append(der)
		for sym1 in range(len(data)):
			for sym2 in range(sym1+1, len(data)):
				for index in range(length):
					val1 = deriviatives[sym1][index]
					val2 = deriviatives[sym2][index]
					if not val1 or not val2:
						result.append(None)
					elif val1 == 0 or val2 == 0:
						result.append(0)
					else:
						result.append(val1 / val2)
		result_for_all_expressions.append(result)
	return result_for_all_expressions
