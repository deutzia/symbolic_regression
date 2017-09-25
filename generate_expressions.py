import random
import sympy as sp
from sympy.physics.mechanics import dynamicsymbols
import copy

import lib.expressions as Expressions

def choose_expression(expressions, operations_unary, symbols_used):
	index = random.randint(0, len(expressions)-1)
	expr1 = expressions.pop(index)
	# trigonometry
	# if random.random() > 0.5 and expr1 in symbols_used:
	# 	return random.choice(operations_unary)(expr1)
	return expr1
	
def create_expression(expressions, operations_binary, operations_unary,
	symbols_used):
	while (len(expressions) > 1):
		expr1 = choose_expression(expressions, operations_unary, symbols_used)
		expr2 = choose_expression(expressions, operations_unary, symbols_used)
		operation = random.choice(operations_binary)
		expressions.append(operation(expr1, expr2))
	return expressions[0]

def init(dimensions):
	x = Expressions.Variable("x")
	v_x = Expressions.Variable("v_x")
	a_x = Expressions.Variable("a_x")
	symbols = [x, v_x, a_x]
	if dimensions > 1:
		y = Expressions.Variable("y")
		v_y = Expressions.Variable("v_y")
		a_y = Expressions.Variable("a_y")
		symbols = [x, v_x, a_x, y, v_y, a_y]
	symbols_used = copy.deepcopy(symbols)
	operations_binary = [Expressions.Add, Expressions.Multiply,
		Expressions.Subtract, Expressions.Divide]
	operations_unary =  [Expressions.Sin, Expressions.Cos]
	added_constants = random.randint(0, len(symbols)+1)
	for i in range(added_constants):
		symbols.append(Expressions.Constant(random.uniform(-10, 10)))
	return symbols, operations_binary, operations_unary, symbols_used

def get_a_single_expression(dimensions):
	symbols, operations_binary, operations_unary, symbols_used = init(
		dimensions)
	expr = create_expression(symbols, operations_binary,
		operations_unary, symbols_used)
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
