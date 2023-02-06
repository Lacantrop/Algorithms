def insertion_sort(lst: list):
	j = 0
	for i in range(len(lst)):
		j = i
		while j > 0 and (lst[j] < lst[j - 1]):
			lst[j], lst[j - 1] = lst[j - 1], lst[j]
			j = j - 1
		print(f'number iteration: {i} {lst}')
	return lst


print(insertion_sort([10, 8, 2, 1, 0]))