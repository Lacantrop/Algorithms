def binary_search(lst: list, item: int):
	low = 0
	high = len(lst) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = lst[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None


def main():
	my_list = [i for i in range(2, 51)]
	find_in_my_list = 3
	print(f'In list {my_list}\n'
		  f'We should find number {find_in_my_list} in list.\n'
		  f'Result of this script is position in list:'
		  f' {binary_search(my_list, find_in_my_list)}')


if __name__ == '__main__':
	main()
