import random


def quick_sort(lst: list) -> list:
	if len(lst) < 2:
		return lst
	else:
		main = lst[0]
		less = [i for i in lst[1:] if i <= main]
		greater = [i for i in lst[1:] if i > main]
		return quick_sort(less) + [main] + quick_sort(greater)


test_lst = [random.randint(-100,100) for i in range(10)]
print(quick_sort(test_lst))
