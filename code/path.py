class Path():
    """ Represents a single path between 2 node
    """
    def __init__(self, net, nodes):
        self.net = net						# the net from the path
        self.nodes = nodes 					# holds the nodes of the path
