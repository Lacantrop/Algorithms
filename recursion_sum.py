import random


def recursion_sum(x: list):
	a = 0
	print(f'list: {x}')
	if len(x) == 0:
		return 0
	else:
		return x[0] + recursion_sum(x[1:])


lst = [random.randint(-100, 100) for _ in range(10)]
print(recursion_sum(lst))
