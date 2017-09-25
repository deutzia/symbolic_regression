import copy
import random

import generate_expressions


def substitute(node1, node2):
	if node1.father.sons[0] == node1:
		node1.father.sons[0] = copy.deepcopy(node2)
	else:
		node1.father.sons[1] = copy.deepcopy(node2)


def crossover(expressions, number_of_expressions, dimensions):
	initial_size = len(expressions)
	number_of_changes = number_of_expressions - initial_size
	for i in range(0, number_of_changes, 2):
		# get two different expressions		
		index1 = random.randint(0, initial_size-1)
		index2 = random.randint(0, initial_size-1)
		while index1 == index2:
			index1 = random.randint(0, initial_size-1)

		expr1 = expressions[index1]
		expr2 = expressions[index2]

		expressions[index1] = copy.deepcopy(expr1)
		expressions[index2] = copy.deepcopy(expr2)

		nodes1 = [node for node in expr1.get_nodes()]
		nodes2 = [node for node in expr2.get_nodes()]

		if nodes1 and nodes2:
			node1 = random.choice(nodes1)
			node2 = random.choice(nodes2)
			if node1.father == None:
				expr1 = copy.deepcopy(node2)
			else:
				substitute(node1, node2)
			if node2.father == None:
				expr2 = copy.deepcopy(node1)
			else:
				substitute(node2, node1)
			expressions.append(expr1)
			expressions.append(expr2)
		else:
			expressions.append(generate_expressions.get_a_single_expression(dimensions))
			expressions.append(generate_expressions.get_a_single_expression(dimensions))


if __name__ == '__main__':
	expr1 = generate_expressions.get_a_single_expression(1)
	expr2 = generate_expressions.get_a_single_expression(1)
	l = [expr1, expr2]
	s = crossover(l, 4, 1)
	for e in l:
		print(e)
