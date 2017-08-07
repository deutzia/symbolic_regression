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

def do_crossover(expr_1, expr_2, node_1, node_2):
	index_child_1 = random.randint(0, len(node_1.args)-1)
	index_child_2 = random.randint(0, len(node_2.args)-1)

	child_1 = node_1.args[index_child_1]
	child_2 = node_2.args[index_child_2]

	node_1_list = list(node_1.args)
	node_2_list = list(node_2.args)
	node_1_list[index_child_1] = child_2
	node_2_list[index_child_2] = child_1

	node_1_cross = node_1.func(*node_1_list)
	node_2_cross = node_2.func(*node_2_list)

	expr_1 = expr_1.subs(node_1, node_1_cross)
	expr_2 = expr_2.subs(node_2, node_2_cross)


	return expr_1, expr_2

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

		nodes_1 = get_nodes(expr1)
		nodes_2 = get_nodes(expr2)

		if nodes_1 and nodes_2:
			node_1 = random.choice(nodes_1)
			node_2 = random.choice(nodes_2)

			expr1, expr2 = do_crossover(expressions[index1], expressions[index2], node_1, node_2)

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
