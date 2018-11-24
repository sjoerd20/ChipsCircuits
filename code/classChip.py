# class chips & circuits
class Node():
	def __init__(self, id, coordinates, is_free):
		self.id = id                        # id xyz
		self.coordinates = coordinates      # tuple with x, y, z coordinates
		self.is_free = is_free              # free means not used
		self.is_gate = False
		self.L_neighbours = {}				# contains all neighbours (id, node)

# holds a single path
class Path():
	def __init__(self, net):
		self.net = net		# the net from the path
		self.path = path 	# holds the nodes of the path

class Chip():
	def __init__(self, circuit, width, height):
		self.levels = 0
		self.width = width
		self.height = height
		self.circuit = circuit
		self.nodes = {}                	# contains all nodes with coord. as keys
		self.walls = []                 # contains all gates coord.
		self.path = []					# list of all paths
		self.gates = []					# list of all gates

		# initiate all levels of the chip
		for z in range(8):
			self.init_nodes(z)

		# store all neighbours of each nodes
		for id, node in self.nodes.items():
			self.find_neighbours(id, node)

	# init nodes at level z and store them in nodes
	def init_nodes(self, z):
		self.levels += 1
		for x in range(self.width):
			for y in range(self.height):
				id = str(x) + ", " + str(y) + ", " + str(z)
				node = Node(id, (x, y, z), True)
				self.nodes[id] = node

	# stores all neighbours of each node
	def find_neighbours(self, id, node):
		x, y, z = node.coordinates
		possible_neighbours = [(x+1, y, z), (x, y-1, z), (x-1, y, z),
								(x, y+1, z), (x, y, z-1), (x, y, z+1)]
		for neighbour in possible_neighbours:

			# check for each neighbour if they exist
			id = str(neighbour[0]) + ", " + str(neighbour[1]) + ", " + str(neighbour[2])
			if id in self.nodes:
				node.L_neighbours[id] = self.nodes[id]

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
			self.gates.append(self.nodes.get(id))
			cur_coordinates = []

	# returns a list of coordinates of all gates
	def get_gates_coordinates(self):
		L_x, L_y = [], []
		for gate in self.gates:
			L_x.append(gate.coordinates[0])
			L_y.append(gate.coordinates[1])
		return L_x, L_y

	def in_bounds(self, id):
		(x, y, z) = id
		return 0 <= x < self.width and 0 <= y < self.height and 0 <= z <= self.levels

	def passable(self, id):
		return id not in self.walls

	def neighbors(self, id, goal):
		(x, y, z) = id
		results = [(x+1, y, z), (x, y-1, z), (x-1, y, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]
		if goal not in results:
			results = filter(self.in_bounds, results)
			results = filter(self.passable, results)
		return results
