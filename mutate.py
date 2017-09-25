import random

import lib.expressions as Expressions


def get_floats(expression):
	result = []
	for arg in expression.get_nodes():
		if isinstance(arg, Expressions.Constant):
			result.append(arg)
	return result

def get_binaries(expression, operations_binary):
	result = []
	for arg in expression.get_nodes():
		if isinstance(arg, tuple(operations_binary)):
			result.append(arg)
	return result

def get_variables(expression, symbols_used):
	result = []
	for arg in expression.get_nodes():
		if arg in symbols_used:
			result.append(arg)
	return result

def get_the_other(thing, dict_of_things):
	result = random.choice(dict_of_things)
	while result == thing:
		result = random.choice(dict_of_things)
	return result

def substitute(node1, node2):
	if node1.father.sons[0] == node1:
		node1.father.sons[0] = node2
	else:
		node1.father.sons[1] = node2

def mutate(expressions, operations_binary, operations_unary, symbols_used, probability = 0.1):
	for index in range(len(expressions)):
		if random.random() < probability:
			floats = get_floats(expressions[index])
			binaries = get_binaries(expressions[index], operations_binary)
			variables = get_variables(expressions[index], symbols_used)

			if random.random() > 0.5 and len(floats) > 0:
				chosen = random.choice(floats)
				if chosen.father == None:
					expressions[index] = Expressions.Constant(random.uniform(-100, 100))
				else:
					substitute(chosen, Expressions.Constant(random.uniform(-100, 100)))

			elif len(binaries) > 0:
				chosen = random.choice(binaries)
				new_node = get_the_other(chosen.__class__, operations_binary) \
					(*chosen.sons)
				if chosen.father == None:
					expressions[index] = new_node
				else:
					substitute(chosen, new_node)

			elif len(variables) > 0:
				chosen = random.choice(variables)
				new_node = get_the_other(chosen.__class__, symbols_used)
				if chosen.father == None:
					expressions[index] = new_node
				else:
					substitute(chosen, new_node)


if __name__ == '__main__':
	import generate_expressions
	operations_binary = [Expressions.Add, Expressions.Multiply,
		Expressions.Subtract, Expressions.Divide]
	operations_unary =  [Expressions.Sin, Expressions.Cos]
	x = Expressions.Variable("x")
	v_x = Expressions.Variable("v_x")
	a_x = Expressions.Variable("a_x")
	symbols_used = [x, v_x, a_x]
	expr1 = generate_expressions.get_a_single_expression(1)
	print(expr1)
	l = [expr1]
	mutate(l, operations_binary, operations_unary, symbols_used, 1)
	print(l[0])	
