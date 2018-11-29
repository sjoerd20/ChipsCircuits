import heapq
from shared_functions import *
import classChip

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

	try:
		while not queue.empty():
			current = queue.get()
			if current == goal:
				break
			for next in chip.neighbors(current, goal):
				new_cost = cost_so_far[current] + 1
				if next not in cost_so_far or new_cost < cost_so_far[next]:
					cost_so_far[next] = new_cost
					priority = new_cost + heuristic(goal, next) + gate_density(chip, next)
					queue.put(next, priority)
					came_from[next] = current

		prev = goal
		shortest_path.append(goal)
		while came_from[prev] is not None:
			shortest_path.append(came_from[prev])
			prev = came_from[prev]
		chip.walls += shortest_path

		# store path for this net in new Path object and append to chip object
		chip.paths.append(classChip.Path(net, shortest_path))
		return cost_so_far[goal]

	except KeyError:
		return net