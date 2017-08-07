import random
import sympy as sp

def get_integers(expression):
	result = []
	for arg in sp.preorder_traversal(expression):
		if isinstance(arg, sp.Integer):
			result.append(arg)
	return result

def get_floats(expression):
	result = []
	for arg in sp.preorder_traversal(expression):
		if isinstance(arg, sp.Float) and not isinstance(arg, sp.Integer):
			result.append(arg)
	return result

def get_binaries(expression, operations_binary):
	result = []
	for arg in sp.preorder_traversal(expression):
		if isinstance(arg, tuple(operations_binary)):
			result.append(arg)
	return result

def get_variables(expression, symbols_used):
	result = []
	for arg in sp.preorder_traversal(expression):
		if arg in symbols_used:
			result.append(arg)
	return result

def get_the_other(thing, dict_of_things):
	result = random.choice(dict_of_things)
	while result == thing:
		result = random.choice(dict_of_things)
	return result

def mutate(expressions, operations_binary, operations_unary, symbols_used):
	for index in range(len(expressions)):
		if random.random() > 0.1:
			ints = get_integers(expressions[index])
			floats = get_floats(expressions[index])
			binaries = get_binaries(expressions[index], operations_binary)
			variables = get_variables(expressions[index], symbols_used)
			if random.random() > 0.6 and len(ints) > 0:
				chosen = random.choice(ints)
				new_int = random.randint(-chosen, chosen)
				while new_int == 0 or new_int == chosen:
					new_int = random.randint(-chosen, chosen)
				expressions[index].subs(chosen, new_int)
			elif len(floats) > 0:
				chosen = random.choice(floats)
				expressions[index].subs(chosen, random.uniform(-100, 100))
			elif len(binaries) > 0:
				chosen = random.choice(binaries)
				new_node = get_the_other(chosen.func, operations_binary) \
					(*chosen.args)
				expressions[index].subs(chosen, new_node)
			elif len(variables) > 0:
				chosen = random.choice(variables)
				new_node = get_the_other(chosen.func, symbols_used)
				expressions[index].subs(chosen, new_node)
