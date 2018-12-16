class Node():
    """ Represents a single node
    """
    def __init__(self, id, coordinates, is_free):
        self.id = id                        # id string xyz
        self.coordinates = coordinates      # tuple with x, y, z coordinates
        self.is_free = is_free              # if node is used
        self.is_gate = False				# true if node is gate, else false
        self.L_neighbours = {}				# contains all neighbours (id, node)
