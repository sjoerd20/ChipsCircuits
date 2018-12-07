import heapq
from shared_functions import *
import classChip
from random import *

# implements a priority queue using heapq
class PriorityQueue():
	def __init__(self):
		self.elements = []

	def empty(self):
		return len(self.elements) == 0

	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))

	def get(self):
		return heapq.heappop(self.elements)[1]


def a_star(chip, net, random_layer = 0):
	start_layer = 0
	if distance(chip.circuit[net[0]], chip.circuit[net[1]]) > 6:
		start_layer = random_layer
	# for i in range(start_layer):
	# 	chip.walls.append(chip.circuit[net[0]] + (i,))
	# 	chip.walls.append(chip.circuit[net[1]] + (i,))
	start, goal = chip.circuit[net[0]] + (start_layer,), chip.circuit[net[1]] + (start_layer,)
	queue = PriorityQueue()
	queue.put(start, 0)
	came_from, cost_so_far = {}, {}
	came_from[start], cost_so_far[start] = None, 2 * start_layer
	shortest_path = []

	while not queue.empty():
		current = queue.get()
		if current == goal:
			break
		for next in chip.neighbors(current, goal):
			new_cost = cost_so_far[current] + 1
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost + heuristic(goal, next)
				queue.put(next, priority)
				came_from[next] = current

	prev = goal
	shortest_path.append(goal)
	for i in range(0, start_layer + 1):
		shortest_path.append(chip.circuit[net[1]] + (i,))
	while came_from[prev] is not None:
		shortest_path.append(came_from[prev])
		prev = came_from[prev]
	chip.walls += shortest_path
	for i in range(start_layer, 0, -1):
		shortest_path.append(chip.circuit[net[0]] + (i,))
	chip.walls += shortest_path

	# store path for this net in new Path object and append to chip object
	chip.paths.append(classChip.Path(net, shortest_path))
	return cost_so_far[goal]
