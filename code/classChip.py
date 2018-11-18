# class chips & circuits
class Node():
	def __init__(self, id, coordinates, is_free):
		self.id = id                        # id xyz
		self.coordinates = coordinates      # tuple with x, y, z coordinates
		self.is_free = is_free              # free means not used
		self.is_gate = False


class Chip():
	def __init__(self, circuit, width, height):
		self.levels = 0
		self.width = width
		self.height = height
		self.circuit = circuit
		self.nodes = {}                		# contains all nodes with coord. as keys
		self.walls = []                   	# contains all gates coord.

		# initiate first level of chip
		self.init_nodes(0)


	# init nodes at level z and store them in nodes
	def init_nodes(self, z):
		self.levels += 1
		for x in range(self.width):
			for y in range(self.height):
				# TODO make a dict instead of list with tuple? coordinates as keys
				id = str(x) + ", " + str(y) + ", " + str(z)
				node = Node(id, (x, y, z), True)
				self.nodes[id] = node


	# loads the chip
	def load_chip(self):
		cur_coordinates = []    # temp list for current gate
		for gate in self.circuit:
			for coordinate in gate:
				cur_coordinates.append(coordinate)
			id = str(cur_coordinates[0]) + ", " + str(cur_coordinates[1]) + ", " + "0"
			self.nodes.get(id).is_free = False
			self.nodes.get(id).is_gate = True
			self.walls.append((cur_coordinates[0], cur_coordinates[1], 0))
			cur_coordinates = []

	def in_bounds(self, id):
		(x, y, z) = id
		return 0 <= x < self.width and 0 <= y < self.height and 0 <= z <= self.levels

	def passable(self, id):
		return id not in self.walls

	def neighbors(self, id, start, goal):
		(x, y, z) = id
		results = [(x+1, y, z), (x, y-1, z), (x-1, y, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]
		if goal not in results:
			results = filter(self.in_bounds, results)
			results = filter(self.passable, results)
		return results