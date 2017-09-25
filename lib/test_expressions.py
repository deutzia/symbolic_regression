import math
import pytest
import types

from expressions import *


def test_constant_init():
	c = Constant(2)

def test_constant_deriviative():
	c = Constant(2)
	assert c.deriviative(Variable("x")) == Constant(0)

def test_constant_get_value():
	c = Constant(2)
	assert c.get_value() == 2

def test_constant_get_tree_size():
	c = Constant(2)
	assert c.get_tree_size() == 1

def test_constant_get_sons():
	c = Constant(2)
	assert c.sons == []

def test_constant_father():
	c = Constant(2)
	assert c.father == None

def test_constant_str():
	c = Constant(2)
	assert str(c) == "2"


def test_variable_init():
	a = Variable("a")

def test_variable_deriviative():
	v = Variable("v")
	assert v.deriviative(v) == Constant(1)
	assert v.deriviative(Variable("x")) == Constant(0)

def test_variable_get_value():
	v = Variable("v")
	d = {"v": 3}
	assert v.get_value(d) == 3

def test_variable_get_value_missing_info():
	v = Variable("v")
	d = {"x": 4}
	with pytest.raises(ValueError):
		v.get_value(d)

def test_variable_get_tree_size():
	v = Variable("v")
	assert v.get_tree_size() == 1

def test_variable_get_sons():
	v = Variable("v")
	assert v.sons == []

def test_variable_father():
	c = Variable("x")
	assert c.father == None

def test_variable_str():
	c = Variable("x")
	assert str(c) == "x"


def test_sin_init():
	x = Variable("x")
	s = Sin(x)

def test_sin_deriviative():
	x = Variable("x")
	s = Sin(x)
	d = {"x": 1}
	assert s.deriviative(x).get_value(d) == Cos(x).get_value(d)
	d = {"x": 2}
	assert s.deriviative(x).get_value(d) == Cos(x).get_value(d)
	d = {"x": math.pi}
	assert s.deriviative(x).get_value(d) == Cos(x).get_value(d)

def test_sin_get_value():
	x = Variable("x")
	s = Sin(x)
	d = {"x": 1}
	assert s.get_value(d) == math.sin(1)

def test_sin_get_tree_size():
	x = Variable("x")
	s = Sin(x)
	assert s.get_tree_size() == 2
	t = Sin(s)
	assert t.get_tree_size() == 3

def test_sin_get_sons():
	x = Variable("x")
	s = Sin(x)
	assert s.sons == [x]

def test_sin_father():
	x = Variable("x")
	s = Sin(x)
	assert s.father == None
	assert x.father == s

def test_sin_str():
	x = Variable("x")
	s = Sin(x)
	assert str(s) == "sin(x)"


def test_cos_init():
	x = Variable("x")
	s = Cos(x)

def test_cos_deriviative():
	x = Variable("x")
	s = Cos(x)
	d = {"x": 1}
	assert s.deriviative(x).get_value(d) == -Sin(x).get_value(d)
	d = {"x": 2}
	assert s.deriviative(x).get_value(d) == -Sin(x).get_value(d)
	d = {"x": math.pi}
	assert s.deriviative(x).get_value(d) == -Sin(x).get_value(d)

def test_cos_get_value():
	x = Variable("x")
	s = Cos(x)
	d = {"x": 1}
	assert s.get_value(d) == math.cos(1)

def test_cos_get_tree_size():
	x = Variable("x")
	s = Cos(x)
	assert s.get_tree_size() == 2
	t = Cos(s)
	assert t.get_tree_size() == 3

def test_cos_get_sons():
	x = Variable("x")
	s = Cos(x)
	assert s.sons == [x]

def test_cos_father():
	x = Variable("x")
	s = Cos(x)
	assert s.father == None
	assert x.father == s

def test_cos_str():
	x = Variable("x")
	s = Cos(x)
	assert str(s) == "cos(x)"


def test_multiply_init():
	c = Constant(5)
	x = Variable("x")
	m = Multiply(c, x)

def test_multiply_deriviative():
	c = Constant(5)
	x = Variable("x")
	m = Multiply(c, x)
	d = {"x": 1}
	assert m.deriviative(x).get_value(d) == 5

def test_multiply_get_value():
	n = Constant(3)
	m = Constant(4)
	assert Multiply(n, m).get_value() == 12

def test_multiply_get_tree_size():
	c = Constant(5)
	x = Variable("x")
	m = Multiply(c, x)
	assert m.get_tree_size() == 3

def test_multiply_get_sons():
	c = Constant(5)
	x = Variable("x")
	m = Multiply(c, x)
	assert m.sons == [c, x] or m.sons == [x, c]

def test_multiply_father():
	c = Constant(5)
	x = Variable("x")
	m = Multiply(c, x)
	assert m.father == None
	assert x.father == m
	assert c.father == m

def test_multiply_str():
	c = Constant(5)
	x = Variable("x")
	m = Multiply(c, x)
	assert str(m) == "(5)*(x)"


def test_add_init():
	c = Constant(5)
	x = Variable("x")
	m = Add(c, x)

def test_add_deriviative():
	c = Constant(5)
	x = Variable("x")
	m = Add(c, x)
	d = {"x": 1}
	assert m.deriviative(x).get_value(d) == 1

def test_add_get_value():
	n = Constant(3)
	m = Constant(4)
	assert Add(n, m).get_value() == 7

def test_add_get_tree_size():
	c = Constant(5)
	x = Variable("x")
	m = Add(c, x)
	assert m.get_tree_size() == 3

def test_add_get_sons():
	c = Constant(5)
	x = Variable("x")
	m = Add(c, x)
	assert m.sons == [c, x] or m.sons == [x, c]

def test_add_father():
	c = Constant(5)
	x = Variable("x")
	m = Add(c, x)
	assert m.father == None
	assert x.father == m
	assert c.father == m

def test_add_str():
	c = Constant(5)
	x = Variable("x")
	m = Add(c, x)
	assert str(m) == "(5)+(x)"


def test_subtract_init():
	c = Constant(5)
	x = Variable("x")
	m = Subtract(c, x)

def test_subtract_deriviative():
	c = Constant(5)
	x = Variable("x")
	m = Subtract(c, x)
	d = {"x": 1}
	assert m.deriviative(x).get_value(d) == -1

def test_subtract_get_value():
	n = Constant(11)
	m = Constant(4)
	assert Subtract(n, m).get_value() == 7

def test_subtract_get_tree_size():
	c = Constant(5)
	x = Variable("x")
	m = Subtract(c, x)
	assert m.get_tree_size() == 3

def test_subtract_get_sons():
	c = Constant(5)
	x = Variable("x")
	m = Subtract(c, x)
	assert m.sons == [c, x]

def test_subtract_father():
	c = Constant(5)
	x = Variable("x")
	m = Subtract(c, x)
	assert m.father == None
	assert x.father == m
	assert c.father == m

def test_subtract_str():
	c = Constant(5)
	x = Variable("x")
	m = Subtract(c, x)
	assert str(m) == "(5)-(x)"


def test_divide_init():
	c = Constant(5)
	x = Variable("x")
	m = Divide(c, x)

def test_divide_deriviative():
	c = Constant(1)
	x = Variable("x")
	m = Divide(c, x)
	d = {"x": 1}
	assert m.deriviative(x).get_value(d) == -1
	d = {"x": 2}
	assert m.deriviative(x).get_value(d) == -0.25
	d = {"x": -1}
	assert m.deriviative(x).get_value(d) == -1
	d = {"x": -2}
	assert m.deriviative(x).get_value(d) == -0.25

def test_divide_get_value():
	n = Constant(10)
	m = Constant(5)
	assert Divide(n, m).get_value() == 2
	n = Constant(10)
	m = Constant(2)
	assert Divide(n, m).get_value() == 5
	n = Constant(17)
	m = Constant(5)
	assert Divide(n, m).get_value() == 3.4

def test_divide_get_tree_size():
	c = Constant(5)
	x = Variable("x")
	m = Divide(c, x)
	assert m.get_tree_size() == 3

def test_divide_get_sons():
	c = Constant(5)
	x = Variable("x")
	m = Divide(c, x)
	assert m.sons == [c, x]

def test_divide_father():
	c = Constant(5)
	x = Variable("x")
	m = Divide(c, x)
	assert m.father == None
	assert x.father == m
	assert c.father == m

def test_divide_str():
	c = Constant(5)
	x = Variable("x")
	m = Divide(c, x)
	assert str(m) == "(5)/(x)"


def test_function_composition_1():

	def get_correct_value(x):
		return math.cos(x)*math.cos(math.sin(x))

	x = Variable("x")
	expression = Sin(Sin(x))
	deriviative = expression.deriviative(x)
	values = [1, 2, math.pi, -1, 2*math.pi, -math.pi]
	for value in values:
		variables = {"x": value}
		assert (deriviative.get_value(variables)) == math.cos(value)*math.cos(math.sin(value))

def test_function_composition_2():

	def get_correct_value(x, y):
		return math.cos(x)*math.cos(y) + 5*y

	x = Variable("x")
	y = Variable("y")
	expression = Add(Multiply(Sin(x), Cos(y)), Multiply(Multiply(x, y), Constant(5)))
	deriviative = expression.deriviative(x)
	values = [[1, 1], [1, 2], [2, 1], [-1, 1], [1, -1], [math.pi, 1], [1, math.pi]]
	for value in values:
		x_val = value[0]
		y_val = value[1]
		variables = {"x": x_val, "y": y_val}
		assert (deriviative.get_value(variables)) == get_correct_value(x_val, y_val)


def test_get_nodes():
	c = Constant(5)
	x = Variable("x")
	m = Multiply(c, x)
	nodes = m.get_nodes()
	nodes_list = [node for node in nodes]
	assert len(nodes_list) == 3
	assert c in nodes_list
	assert x in nodes_list
	assert m in nodes_list
