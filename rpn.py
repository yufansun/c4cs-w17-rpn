#!/usr/bin/env python3

import operator
import readline
from termcolor import cprint
import types

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod,
}

def hello():
	print("Hello world")


def color_print(operand):
	if type(operand) is float:
		if operand < 0:
			cprint(operand, 'red', attrs=['bold'], end=" ")
		elif operand == 0:
			cprint(operand, 'green', end=" ")
		else:
			cprint(operand, 'yellow', end=" ")
	else:
		cprint(operand, 'blue', end=" ")

def color_print2(operand):
	if type(operand) is float:
		if operand < 0:
			cprint(operand, 'red', attrs=['bold'])
		elif operand == 0:
			cprint(operand, 'green')
		else:
			cprint(operand, 'yellow')
	else:
		cprint(operand, 'blue')

def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			stack.append(result)
		color_print(operand)
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		print("=",end=" ")
		color_print2(result)

if __name__ == '__main__':
	main()