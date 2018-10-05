import textwrap
import collections


test_case = '''\
	7 5 3 2
	#######
	#.#.#.#
	#.#...#
	#...#.#
	#######\
'''
test_case_lines = textwrap.dedent(test_case).split('\n')
width, height, start_x, start_y = tuple(map(int, test_case_lines[0].split()))


def map_parser(width, height, map_lines):
	points = [(i, j) for i in range(width) for j in range(height)
								if map_lines[j][i] == '.']
	neighbours = {}
	for p in points:
		neighbours[p] = [(p[0] + offset[0], p[1] + offset[1])
												for offset in [(0, 1), (0, -1), (-1, 0), (1, 0)]
												if (p[0] + offset[0], p[1] + offset[1]) in points]
	return points, neighbours


def simpleBFS(points, neighbours, start_x, start_y):
	is_point_visited = {p: False for p in points}
	points_to_visit = collections.deque([{'coordinates': (start_x, start_y), 																									'came_from': (None, None)}])
	distance_chart = {(start_x, start_y): {'came_from': (None, None), 'distance': 0}}
	while points_to_visit:
		point = points_to_visit.popleft()
		if is_point_visited[point['coordinates']]:
			continue
		is_point_visited[point['coordinates']] = True
		if point['came_from'] != (None, None):
			distance_chart[point['coordinates']] = {'came_from': point['came_from'], 								'distance': distance_chart[point['came_from']]['distance'] + 1}
		for neighbour in neighbours[point['coordinates']]:
			if not is_point_visited[neighbour]:
				points_to_visit.append({'coordinates': neighbour,
																'came_from': point['coordinates']})
	return distance_chart
				
	
map_maze = map_parser(width, height, test_case_lines[1:])
result = simpleBFS(*map_maze, start_x, start_y)
print(result)
