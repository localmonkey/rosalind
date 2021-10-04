import queue
import numpy as np


class myGrph:
    def __init__(self, vertex_quant, edges_quant):
        self.V_quant = vertex_quant
        self.E_quant = edges_quant
        self.edges_list = np.zeros((edges_quant, 3), dtype=np.int64)
        #self.edge_list = []

    def fill_connections(self, file_descriptor):
        counter = 0
        for line in file_descriptor:
            vertex, connected_vertex, weight = map(lambda x: int(x),
                                                   line.strip().split())
            self.edges_list[counter] = [vertex - 1, connected_vertex - 1, weight]
            counter = counter + 1

    def f_con_comp(self, src_vertex):
        q = queue.Queue()
        q.put(src_vertex - 1)
        visited = [False]*self.V_quant
        while(not q.empty()):
            vrtxf = q.get()
            visited[vrtxf] = True
            for i in range(0, self.V_quant):
                if ((self.V_mat[vrtxf][i] != - 1) and visited[i] == False):
                    q.put(i)
        return visited

    def find_shortest_paths(self, src_vertex):
        distance = np.full((1, self.V_quant), np.Inf).flatten()
        distance[src_vertex - 1] = 0
        for _ in range(0, self.V_quant - 1):
            for uu, vv, weight in self.edges_list:
                if (
                    distance[uu] != np.Inf and
                    (distance[vv] > (distance[uu] + weight))
                   ):
                    distance[vv] = distance[uu] + weight
        return distance


if __name__ == "__main__":
    with open("rosalind_bf.txt", "r") as f:
        vertexes_quant, edges_quant = map(lambda x: int(x),
                                          f.readline().strip().split())
        tst_grph = myGrph(vertexes_quant, edges_quant)
        tst_grph.fill_connections(f)
    res = tst_grph.find_shortest_paths(1)

    with open("bf_output.txt", "w") as f:
        for i in res:
            if i == np.Inf:
                i = 'x'
            else:
                i = int(i)
            f.write(f"{i} ")
