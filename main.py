# Don't Get Volunteered https://foobar.withgoogle.com/
# A class Node that represents a Vertex (node) in a graph.
class Vertex:
    def __init__(self, id: int, ) -> None:
        self._id = id  # the id of the vertex
        self._con_ver = []  # connected edges of the current vertex (a tuple)

    def get_id(self) -> int:
        return self._id

    def add_node(self, vert_id) -> None:
        self._con_ver.append(vert_id)

    def get_edges(self) -> tuple: # returns the connected vertices
        return tuple(self._con_ver)

    #def get_cord(self) -> tuple: # returns the x,y coordinates


def main():
    x = []
    for i in range(1, 65):
        x.append(Vertex(i))
    for item in x:
        print(item.get_id(), item.get_edges())


if __name__ == '__main__':
    main()
