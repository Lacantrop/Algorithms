from collections import deque

"""We have fiends, and friends our friends. Need find nearest seller in our friends. """

graph = {'you': ['alice', 'bob', 'claire'], 'bob': ['anuj', 'peggy'], 'alice': ['peggy'], 'claire': ['thom', 'jonny'],
		 'anuj': [], 'peggy': [], 'thom': [], 'jonny': []}
print(graph)


def person_is_seller(name):
	return name[-1] == 'm'


def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []  # Add friends which already have been searched
	while search_queue:
		person = search_queue.popleft()
		if person not in searched:
			if person_is_seller(person):
				print(person + ' is a mango seller!')
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False


print(search('you'))
