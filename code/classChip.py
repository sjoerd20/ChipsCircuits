# class chips & circuits
class Node():
	def __init__(self, id, coordinates, is_free):
		self.id = id                        # id xyz
		self.coordinates = coordinates      # tuple with x, y, z coordinates
		self.is_free = is_free              # free means not used
		self.is_gate = False
		self.L_neighbours = []				# list w/ id's of neighbours

	def add_neighbours_to_list(self, neighbour_id):
		self.L_neighbours.append(neighbour_id)

class Chip():
	def __init__(self, circuit, horiz_length, vert_length):
		self.lower_levels = 0
		self.higher_levels = 0
		self.horiz_length = horiz_length
		self.vert_length = vert_length
		self.circuit = circuit
		self.dict_nodes = {}                # contains all nodes with coord. as keys
		self.L_gates = []                   # contains all gates coord.

		# initiate all levels of the chip
		for z in range(8):
			self.init_nodes(z)


	# init nodes at level z and store them in dict_nodes
	def init_nodes(self, z):
		if z < 0:
			self.lower_levels -= 1
		elif z > 0:
			self.higher_levels += 1
		for x in range(self.horiz_length):
			for y in range(self.vert_length):
				# TODO make a dict instead of list with tuple? coordinates as keys
				id = str(x) + ", " + str(y) + ", " + str(z)
				node = Node(id, (x, y, z), True)
				self.dict_nodes[id] = node

		# add neighbours for all nodes
		for id, node in self.dict_nodes.items():
			self.add_neighbours(node)

	# add the neighbour_id to each node instance
	def add_neighbours(self, node):
		coordinates = node.coordinates
		temp_x, temp_y, temp_z = coordinates[0], coordinates[1], coordinates[2]

		# TODO make function who does this efficiently
		neighbour_id = str(temp_x + 1) + ", " + str(temp_y) + ", " + str(temp_z)
		if self.dict_nodes.get(neighbour_id) != None:
			node.add_neighbours_to_list(neighbour_id)
		neighbour_id = str(temp_x - 1) + ", " + str(temp_y) + ", " + str(temp_z)
		if self.dict_nodes.get(neighbour_id) != None:
			node.add_neighbours_to_list(neighbour_id)
		neighbour_id = str(temp_x) + ", " + str(temp_y + 1) + ", " + str(temp_z)
		if self.dict_nodes.get(neighbour_id) != None:
			node.add_neighbours_to_list(neighbour_id)
		neighbour_id = str(temp_x) + ", " + str(temp_y - 1) + ", " + str(temp_z)
		if self.dict_nodes.get(neighbour_id) != None:
			node.add_neighbours_to_list(neighbour_id)
		neighbour_id = str(temp_x) + ", " + str(temp_y) + ", " + str(temp_z + 1)
		if self.dict_nodes.get(neighbour_id) != None:
			node.add_neighbours_to_list(neighbour_id)
		neighbour_id = str(temp_x) + ", " + str(temp_y) + ", " + str(temp_z - 1)
		if self.dict_nodes.get(neighbour_id) != None:
			node.add_neighbours_to_list(neighbour_id)

	# loads the chip
	def load_chip(self):
		cur_coordinates = []    # temp list for current gate
		for gate in self.circuit:
			for coordinate in gate:
				cur_coordinates.append(coordinate)
			id = str(cur_coordinates[0]) + ", " + str(cur_coordinates[1]) + ", " + "0"
			self.dict_nodes.get(id).is_free = False
			self.dict_nodes.get(id).is_gate = True
			self.L_gates.append(id)
			cur_coordinates = []
