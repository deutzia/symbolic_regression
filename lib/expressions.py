import abc
import math


class Node(metaclass=abc.ABCMeta):
	"""This is a basic class for node, all other node classes should inherit 
	from it. The interface should be """

	@abc.abstractmethod
	def deriviative(self, variable):
		"""Return deriviative of the expression.

		Argument should be a variable with respect to which to derive"""
		pass

	@abc.abstractmethod
	def get_value(self, variables = {}):
		"""Calculate value of expression.

		Argument should provide values of variables in the expression.
		Returns normal numeric type."""
		pass

	@abc.abstractmethod
	def get_tree_size(self):
		pass

	@abc.abstractmethod
	def get_sons(self):
		pass


class Constant(Node):
	"""This is a class for representing constants"""

	def __init__(self, value):
		self.value = value

	def __eq__(self, other):
		return self.value == other.value

	def deriviative(self, variable):
		return Constant(0)

	def get_value(self, variables = {}):
		return self.value

	def get_tree_size(self):
		return 1

	def get_sons(self):
		return []


class Variable(Node):
	"""This is a class for variables of the equation"""

	def __init__(self, name):
		self.name = name

	def deriviative(self, variable):
		if self == variable:
			return Constant(1)
		else:
			return Constant(0)

	def get_value(self, variables = {}):
		try:
			return variables[self.name]
		except KeyError:
			raise ValueError(
				"missing variable {} in given values of variables".format(self.name))

	def get_tree_size(self):
		return 1

	def get_sons(self):
		return []


class OneArgFunction(Node):
	"""This is an abstract class for all one-argument functions"""

	def __init__(self, son):
		self.son = son

	@abc.abstractmethod
	def own_deriviative(self, variable):
		pass

	def deriviative(self, variable):
		return Multiply(self.own_deriviative(variable), self.son.deriviative(variable))

	def get_tree_size(self):
		return self.son.get_tree_size() + 1

	def get_sons(self):
		return [self.son]


class Sin(OneArgFunction):

	def own_deriviative(self, variable):
		return Cos(self.son)

	def get_value(self, variables = {}):
		return math.sin(self.son.get_value(variables))


class Cos(OneArgFunction):

	def own_deriviative(self, variable):
		return Multiply(Sin(self.son), Constant(-1))

	def get_value(self, variables = {}):
		return math.cos(self.son.get_value(variables))


class TwoArgFunction(Node):

	def __init__(self, one, two):
		self.sons = [one, two]

	def get_tree_size(self):
		return self.sons[0].get_tree_size() + self.sons[1].get_tree_size() + 1

	def get_sons(self):
		return self.sons

class Multiply(TwoArgFunction):

	def deriviative(self, variable):
		return Add(
			Multiply(self.sons[0].deriviative(variable), self.sons[1]),
			Multiply(self.sons[0], self.sons[1].deriviative(variable)))

	def get_value(self, variables = {}):
		return self.sons[0].get_value(variables) * self.sons[1].get_value(variables)


class Add(TwoArgFunction):

	def deriviative(self, variable):
		return Add(self.sons[0].deriviative(variable), self.sons[1].deriviative(variable))

	def get_value(self, variables = {}):
		return self.sons[0].get_value(variables) + self.sons[1].get_value(variables)


class Subtract(TwoArgFunction):

	def deriviative(self, variable):
		return Subtract(self.sons[0].deriviative(variable), self.sons[1].deriviative(variable))

	def get_value(self, variables = {}):
		return self.sons[0].get_value(variables) - self.sons[1].get_value(variables)


class Divide(TwoArgFunction):

	def deriviative(self, variable):
		return Divide(
			Subtract(
				Multiply(self.sons[0].deriviative(variable), self.sons[1]),
				Multiply(self.sons[0], self.sons[1].deriviative(variable))),
			Multiply(self.sons[1], self.sons[1]))

	def get_value(self, variables = {}):
		return self.sons[0].get_value(variables) / self.sons[1].get_value(variables)
