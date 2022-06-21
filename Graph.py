import collections

from Vertex import Vertex


class Graph:

    def __init__(self):
        self._vertices = {}

    def get_vertex_object(self, vertex_data):
        try:
            vertex = self._vertices[vertex_data]
            return vertex
        except KeyError:
            Vertex.push_sort_type(Vertex.SortType.DATA)
            new_vertex = Vertex(vertex_data)
            self._vertices[vertex_data] = new_vertex
            Vertex.pop_sort_type()
            return new_vertex

    def add_edge(self, src, dest, cost=None):
        src_vertex = self.get_vertex_object(src)
        dest_vertex = self.get_vertex_object(dest)
        src_vertex.add_adj(dest_vertex, cost)

    def show_adj_table(self):
        print("------------------------ \n")
        for vertex in self._vertices:
            self._vertices[vertex].show_adj_list()

    def clear(self):
        self._vertices = {}

    def dijkstra(self, src):
        Infinity = float("inf")
        src_vertex = self._vertices[src]
        partially_processed = collections.deque()
        for vdata, vobj in self._vertices.items():
            vobj.dist = Infinity
        src_vertex.dist = 0
        partially_processed.append(src_vertex)
        while len(partially_processed) > 0:
            current_vertex = partially_processed.popleft()
            for vobj in current_vertex.edge_pairs:
                if current_vertex.dist + current_vertex.edge_pairs[vobj] < vobj.dist:
                    vobj.dist = current_vertex.dist + current_vertex.edge_pairs[vobj]
                    partially_processed.append(vobj)
                    vobj.prev_in_path = current_vertex

    def show_distance_to(self, src):
        self.dijkstra(src)
        print(f"Distance from {src} to:")
        for vdata, vobj in self._vertices.items():
            print(f"{vdata}: {vobj.dist}")

    def show_shortest_path(self, start, stop):

        start_vert = self._vertices[start]
        stop_vert = self._vertices[stop]

        self.dijkstra(start)

        print(f"Cost of shortest path from {start} to {stop}: {stop_vert.dist}")
        if stop_vert.dist < float("inf"):
            path_stack = collections.deque()
            current_vert = stop_vert
            while current_vert is not start_vert:
                path_stack.append(current_vert)
                current_vert = current_vert.prev_in_path

            print(start_vert.data, end="")
            while len(path_stack) > 0:
                print(f"--->{path_stack.pop().data}", end="")
        print("")