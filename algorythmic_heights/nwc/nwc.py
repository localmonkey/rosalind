import queue
import numpy as np


class myGrph:
    def __init__(self, vertex_quant, edges_quant):
        self.V_quant = vertex_quant + 1
        self.E_quant = edges_quant
        # additional edges for fictive vertex
        # fictive vertex needs to connect to all other vertexes to check all different
        # connected components
        self.edges_list = np.zeros((edges_quant + vertex_quant, 3), dtype=np.int64)

    def fill_connections(self, file_descriptor):
        counter = 0
        #for line in file_descriptor:
        for i in range(0, self.E_quant):
            line = file_descriptor.readline() 
            vertex, connected_vertex, weight = map(lambda x: int(x),
                                                   line.strip().split())
            self.edges_list[counter] = [vertex - 1, connected_vertex - 1, weight]
            counter = counter + 1
        # add fictive vertex
        for i in range(0, self.V_quant - 1):
            self.edges_list[counter] = [self.V_quant - 1, i, 1]
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

    def find_neg_cycles(self, src_vertex):
        distance = np.full((1, self.V_quant), np.Inf).flatten()
        distance[src_vertex - 1] = 0
        for _ in range(0, self.V_quant - 1):
            for uu, vv, weight in self.edges_list:
                if (
                    distance[uu] != np.Inf and
                    (distance[vv] > (distance[uu] + weight))
                   ):
                    distance[vv] = distance[uu] + weight

        for uu, vv, weight in self.edges_list:
            if (
                distance[uu] != np.Inf and
                (distance[vv] > (distance[uu] + weight))
               ):
                return 1
        return -1 


if __name__ == "__main__":
    with open("rosalind_nwc.txt", "r") as f:
        graph_quantity = int(f.readline().strip())
        res = []
        for i in range(0, graph_quantity):
            #tst = f.readline()
            vertexes_quant, edges_quant = map(lambda x: int(x),
                    f.readline().strip().split())
            tst_grph = myGrph(vertexes_quant, edges_quant)
            tst_grph.fill_connections(f)
            res.append(tst_grph.find_neg_cycles(vertexes_quant + 1))

    with open("nwc_output.txt", "w") as f:
        for i in res:
            f.write(f"{int(i)} ")
