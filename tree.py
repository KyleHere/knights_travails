class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, one_node):
        if one_node not in self._children:
            self._parent = self._value
            self._children.append(one_node)

    def remove_child(self, del_node):
        self._children.remove(del_node)
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, some_node):
        self._parent = some_node
        some_node.add_child(self)
