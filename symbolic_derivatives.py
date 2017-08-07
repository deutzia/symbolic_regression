import sympy as sp
import numpy as np

# def get_deriviatives(expressions, data, timestep, symbols_used):
# 	sol = []
# 	for exp in expressions:
# 		deriviativex = sp.diff(exp, symbols_used[0], 1)
# 		derxoflamb = np.vectorize(sp.lambdify(tuple(symbols_used),deriviativex
# 			,"numpy"))
# 		deriviativeax = sp.diff(exp, symbols_used[1], 1)
# 		deraxoflamb = np.vectorize(sp.lambdify(tuple(symbols_used),
# 			deriviativeax, "numpy"))
# 		# deriviativey = sp.diff(exp, symbols_used[3], 1)
# 		# deryoflamb = np.vectorize(sp.lambdify(tuple(symbols_used),deriviativey
# 		# 	,"numpy"))
# 		# deriviativevy = sp.diff(exp, symbols_used[5], 1)
# 		# dervyoflamb = np.vectorize(sp.lambdify(tuple(symbols_used),
# 		# 	deriviativevy, "numpy"))
# 		data = [data[0], data[1], data[2]]
# 		with np.errstate(divide='ignore', invalid='ignore'):
# 			arrx = derxoflamb(*data)
# 			arrxa = deraxoflamb(*data)
# 			# arry = deryoflamb(*data)
# 			# arryv = dervyoflamb(*data)
# 		divx = []
# 		divy = []
# 		for i in range(0, len(arrx)):
# 			if arrxa[i] != 0:
# 				divx.append(np.divide(arrx[i], arrxa[i]))
# 			else:
# 				divx.append(None)
# 			# if(arryv[i] != 0):
# 			# 	divy.append(np.divide(arry[i], arryv[i]))
# 			# else:
# 			# 	divy.append(1024.0**100)
# 		sol.append([divx, divy])
# 	return(sol)

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
