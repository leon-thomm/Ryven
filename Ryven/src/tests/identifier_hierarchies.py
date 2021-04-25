class Node:
    __identifier__ = None

    def __init__(self):
        self.build_identifier()

    @classmethod
    def custom_identifier(cls):
        return cls.__name__

    def build_identifier(self):
        ids = []
        for cls in self.__class__.__mro__:
            if issubclass(cls, Node):
                c_i = cls.custom_identifier()
                if c_i:
                    ids.append(c_i)
        self.__identifier__ = '.'.join(reversed(ids))
        return self.__identifier__

class NodeBase(Node):

    def __custom_id__():
        return None

class Node1(NodeBase):
    pass

class Node2(NodeBase):
    pass

if __name__ == '__main__':
    n1 = Node1()
    n2 = Node2()
    nb = NodeBase()

    print(n1.__identifier__)
    print(n2.__identifier__)
    print(nb.__identifier__)

# class A:
#     x = 42
#
#     def __init__(self, y=None):
#         if y:
#             self.x = y
#
#     def asdf(self):
#         return self.x

a = 1
b = 2