# class chips & circuits

class Chiplayer(self):
    def __init__(self, level, length, width):
        self.level = level
        self.length = length
        self.width = width

class Node(self):
    def __init__(self, id, is_gate=False):
        self.id = id
        self.is_gate = is_gate
        self.used = False
        self.id_previous_node = None
