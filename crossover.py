import random
import numpy as np
import sympy as sp
import generate_expressions

def get_nodes(expr):
	nodes = []
	for e in sp.postorder_traversal(expr):
		if e.func in [sp.Add, sp.Mul]:
			nodes.append(e)
	return nodes

def do_crossover(expr1, expr2, node1, node2):
	index_child1 = random.randint(0, len(node1.args)-1)
	index_child2 = random.randint(0, len(node2.args)-1)

	child1 = node1.args[index_child1]
	child2 = node2.args[index_child2]

	node1_list = list(node1.args)
	node2_list = list(node2.args)
	node1_list[index_child1] = child2
	node2_list[index_child2] = child1

	node1_cross = node1.func(*node1_list)
	node2_cross = node2.func(*node2_list)

	expr1 = expr1.subs(node1, node1_cross)
	expr2 = expr2.subs(node2, node2_cross)

	return expr1, expr2

def crossover(expressions, number_of_expressions, dimensions):
	number_of_changes = number_of_expressions - len(expressions)
	initial_size = len(expressions)
	for i in range(0, number_of_changes, 2):
		index1 = random.randint(0, initial_size-1)
		index2 = random.randint(0, initial_size-1)
		while index1 == index2:
			index1 = random.randint(0, initial_size-1)

		expr1 = expressions[index1]
		expr2 = expressions[index2]

		nodes1 = get_nodes(expr1)
		nodes2 = get_nodes(expr2)

		if nodes1 and nodes2:
			node1 = random.choice(nodes1)
			node2 = random.choice(nodes2)
			expr1, expr2 = do_crossover(expressions[index1], expressions[index2], node1, node2)
			expressions.append(expr1)
			expressions.append(expr2)
		else:
			expressions.append(generate_expressions.get_a_single_expression(dimensions))
			expressions.append(generate_expressions.get_a_single_expression(dimensions))

if __name__ == '__main__':
	import generate_expressions
	expr1 = generate_expressions.get_a_single_expression(1)
	expr2 = generate_expressions.get_a_single_expression(1)
	l = [expr1, expr2]
	s =crossover(l, 4, 1)
	for e in l:
		print(e)
