import random
import sympy as sp
from sympy.physics.mechanics import dynamicsymbols
import copy

def choose_expression(expressions, operations_unary, symbols_used):
	index = random.randint(0, len(expressions)-1)
	expr1 = expressions.pop(index)
	if random.random() > 0.5 and expr1 in symbols_used:
		return random.choice(operations_unary)(expr1)
	return expr1
	
def create_expression(expressions, operations_binary, operations_unary, symbols_used):
	while (len(expressions) > 1):
		expr1 = choose_expression(expressions, operations_unary, symbols_used)
		expr2 = choose_expression(expressions, operations_unary, symbols_used)
		operation = random.choice(operations_binary)
		if operation == sp.Pow:
			expressions.append(sp.Mul(expr1, sp.Pow(expr2, -1),))
		else:
			expressions.append(operation(expr1, expr2))
	return expressions[0]

def init(dimensions):
	x, v_x, a_x = sp.symbols("x v_x a_x")
	symbols = [x, v_x, a_x]
	if dimensions > 1:
		y, v_y, a_y = sp.symbols("y v_y a_y")
		symbols = [x, v_x, a_x, y, v_y, a_y]
	symbols_used = copy.deepcopy(symbols)
	operations_binary = [sp.Add, sp.Mul]
	operations_unary =  [sp.sin, sp.cos]
	added_constants = random.randint(0, len(symbols)+1)
	for i in range(added_constants):
		symbols.append(random.uniform(-100, 100))
	return symbols, operations_binary, operations_unary, symbols_used

def get_a_single_expression(dimensions):
	symbols, operations_binary, operations_unary, symbols_used = init(1)
	expr = create_expression(symbols, operations_binary, operations_unary, symbols_used)
	return expr

def generate_expressions(num_of_expressions, dimensions):
	res = []
	symbols, operations_binary, operations_unary, symbols_used = init(1)
	for i in range(num_of_expressions):
		expr = get_a_single_expression(dimensions)
		res.append(expr)
	return res, symbols_used

if __name__ == '__main__':
	expr = get_a_single_expression(1)
	print(expr)
