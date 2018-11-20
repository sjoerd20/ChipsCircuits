import heapq
from shared_functions import *

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

# TODO explanation of a_star algorithm
def a_star(chip, net):
	start = chip.circuit[net[0]] + (0,)
	goal = chip.circuit[net[1]] + (0,)
	queue = PriorityQueue()
	queue.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0
	shortest_path = []

	while not queue.empty():
		current = queue.get()
		if current == goal:
			break
		for next in chip.neighbors(current, start, goal):

			# TODO klopt het dat voor elke neighbor de current node wordt toegevoegd?
			if current not in shortest_path:
				shortest_path.append(current)
			new_cost = cost_so_far[current] + 1
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost + heuristic(goal, next)
				queue.put(next, priority)
				came_from[next] = current
				shortest_path.remove(current)

	# TODO What is chip.walls??
	chip.walls += shortest_path
	return cost_so_far[goal]
