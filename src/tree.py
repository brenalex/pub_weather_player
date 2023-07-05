import numpy as np
from numpy import any

class NonBinTree:

    def __init__(self, val):
        self.val = val
        self.nodes = []

    def add_node(self, val):
        self.nodes.append(NonBinTree(val))

    def has_nodes(self):
        if len(self.nodes) > 0:
            return True
        else:
            return False

    def these_nodes(self):
        node_list = []
        if self.has_nodes:
            for node in self.nodes:
                node_list.append(node.val)
        return node_list
    
    def is_leaf(self):
        flag = not np.any(self.nodes)
        return flag

    def __repr__(self):
        return f"NonBinTree({self.val}): {self.nodes}"
