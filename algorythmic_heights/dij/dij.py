import queue
import numpy as np


class myGrph:
    def __init__(self, vertex_quant):
        self.V_quant = vertex_quant
        self.V_mat = np.identity(self.V_quant) - 1

    def fill_connections(self, file_descriptor):
        for line in file_descriptor:
            vertex, connected_vertex, weight = map(lambda x: int(x),
                                                   line.strip().split())
            self.V_mat[vertex - 1][connected_vertex - 1] = weight

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
        al_chk = np.invert(np.array(self.f_con_comp(src_vertex)))
        while(not al_chk.all()):
            min_dst = np.Inf
            for i in range(0, self.V_quant):
                if distance[i] < min_dst and al_chk[i] == False:
                    min_dst = distance[i]
                    uu = i
            al_chk[uu] = True
            for vv in range(0, self.V_quant):
                if (
                    self.V_mat[uu][vv] != -1 and
                    (distance[vv] > (distance[uu] + self.V_mat[uu][vv])) and
                    al_chk[vv] == False
                   ):
                    distance[vv] = distance[uu] + self.V_mat[uu][vv]
        return distance


if __name__ == "__main__":
    with open("rosalind_dij.txt", "r") as f:
        vertexes_quant, edges_quant = map(lambda x: int(x),
                                          f.readline().strip().split())
        tst_grph = myGrph(vertexes_quant)
        tst_grph.fill_connections(f)
    res = tst_grph.find_shortest_paths(1)
    res[res == np.Inf] = -1

    with open("dij_output.txt", "w") as f:
        for i in res:
            f.write(f"{int(i)} ")
