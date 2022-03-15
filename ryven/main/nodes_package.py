from os.path import basename, dirname, splitext, normpath, join


class NodesPackage:
    """
    A small container to store meta data about imported node packages.
    """

    def __init__(self, directory: str):

        self.name = basename(normpath(directory))
        self.directory = directory

        self.file_path = normpath(join(directory, 'nodes.py'))

    def __str__(self):
        return f'{self.__class__.__name__}({self.name})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.directory})'

    def __eq__(self, other):
#         print('==', self, other)
        if isinstance(other, NodesPackage):
            return self.name == other.name
        else:
            return self.name == str(other)

    def __hash__(self):
        return hash(self.name)

    def config_data(self):
        return {
            'name': self.name,
            'dir': self.directory,
        }
