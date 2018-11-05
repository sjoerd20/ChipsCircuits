# class chips & circuits

class Chip(self):
    def __init__(self, data_file, length, width):
        self.count_levels = 1
        self.length = length
        self.width = width

class Node(self):
    def __init__(self, id, is_gate=False):
        self.id = id
        self.is_gate = is_gate
        self.used = False
        self.id_previous_node = None
