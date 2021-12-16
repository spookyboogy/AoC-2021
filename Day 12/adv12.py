def day12pt1(graph):

	def traverse(node, small_visited):

		sub_tree = []
		if node.islower():
			small_visited += [node]
		for n in graph[node]:
			if n == 'end':
				sub_tree += [[node, 'end']]
				continue
			elif n in small_visited:
				continue
			elif (node + n).islower() and len(graph[n]) == 1:
				continue
			else:
				tails = traverse(n, list(small_visited))
				sub_tree += [[node, *i] for i in tails]
		return sub_tree

	paths = []
	for path in graph['start']:
		tree = traverse(path, [])
		paths += [['start', *branch] for branch in tree]
	return len(paths)


def day12pt2(graph):

	def traverse(node, small_visited, NoTime):

		sub_tree = []
		if node.islower():
			small_visited += [node]
		for n in graph[node]:
			if n == 'end':
				sub_tree += [[node, 'end']]
				continue
			elif n in small_visited:
				if NoTime:
					continue
				else:
					if node.isupper():
						tails = traverse(n, list(small_visited), True)
						sub_tree += [[node, *i] for i in tails if i]
			elif (node + n).islower() and len(graph[n]) == 1:
				if NoTime:
					continue
				else: #####
					tails = traverse(n, list(small_visited), False)
					sub_tree += [[node, *i] for i in tails if i]
					
			else:
				tails = traverse(n, list(small_visited), False)
				sub_tree += [[node, *i] for i in tails]
		return sub_tree

	paths = []
	for path in graph['start']:
		tree = traverse(path, [], False)
		paths += [['start', *branch] for branch in tree]
	return len(paths)




def cave_to_graph(cave):
	
	graph = {}
	for edge in cave:
		u, v = edge[0], edge[1]
		if u in graph:
			if v not in graph[u] and v != 'start':
				graph[u] += [v]
			if u != 'start':
				if v not in graph:
					graph[v] = [u]
				else:
					graph[v] += [u]
		else:
			if v != 'start':
				graph[u] = [v]
			if u != 'start':
				if v not in graph:
					graph[v] = [u]
				else:
					graph[v] += [u]
	return graph


with open('easyinput0.txt', 'r') as f:
	f = f.read().splitlines()
	cave = [tuple(i for i in line.split('-')) for line in f]

print(day12pt1(cave_to_graph(cave)))
#print(day12pt2(cave_to_graph(cave)))
