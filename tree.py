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
            self._children.append(one_node)
            one_node.parent = self

    def remove_child(self, del_node):
        if del_node in self._children:
            self._children.remove(del_node)
            del_node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, some_node):
        if some_node is self._parent:
            return
        if self._parent is not None:
            self._parent.remove_child(self)
        self._parent = some_node
        if some_node is not None:
            some_node.add_child(self)


# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)
