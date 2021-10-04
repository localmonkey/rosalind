import numpy as np

class myGrph:
    def __init__(self, V_quant, E_quant):
        self.V = V_quant
        self.E = E_quant
        self.edges_list = [[]] * (self.V)
        # self.edges_list = [[]] * (self.V + 1)

    def build_graph(self, f):
        for i in range(0, self.E):
            vertex1, vertex2 = map(int, f.readline().strip().split())
            self.edges_list[vertex1 - 1] = self.edges_list[vertex1 - 1] + [vertex2 - 1]
            #self.edges_list[vertex2 - 1] = self.edges_list[vertex2 - 1] + [vertex1 - 1]
        #for i in range(0, self.V):
        #    self.edges_list[self.V] = self.edges_list[self.V] + [i]

    def dfs(self, vertex, visited_list):
        vertex = vertex - 1
        visited_list[vertex] = True
        stack_l = []
        stack_l.append(vertex)
        while len(stack_l) > 0:
            vrtx = stack_l.pop()
            visited_list[vrtx] = True
            for i in self.edges_list[vrtx]:
                if visited_list[i] is False:
                    stack_l.append(i)
        return visited_list

    def check_aciclity(self):
        visited_list = [False]*self.V
        #for v_comp in self.edges_list[self.V]:
        for v_comp in range(0, self.V):
            if visited_list[v_comp] is True:
                continue
            check_list = [False]*self.V
            vertex = v_comp
            stack_l = []
            stack_l.append(vertex)
            while len(stack_l) > 0:
                vrtx = stack_l[len(stack_l) - 1]
                if visited_list[vrtx] is False:
                    visited_list[vrtx] = True
                    check_list[vrtx] = True
                else: 
                    check_list[vrtx] = False 
                    stack_l.pop()
                    continue
                for i in self.edges_list[vrtx]:
                    if visited_list[i] is False:
                        stack_l.append(i)
                    if check_list[i] is True:
                        return -1
        return 1

    def topologically_sort(self):
        #sorted_grph =  np.zeros(self.V, dtype=np.int64) 
        sorted_grph = []
        cnt = self.V - 1
        visited_list = [False]*self.V
        #for v_comp in self.edges_list[self.V]:
        for v_comp in range(0, self.V):
            if visited_list[v_comp] is True:
                continue
            check_list = [False]*self.V
            vertex = v_comp
            stack_l = []
            stack_l.append(vertex)
            while len(stack_l) > 0:
                vrtx = stack_l[len(stack_l) - 1]
                if visited_list[vrtx] is False:
                    visited_list[vrtx] = True
                    check_list[vrtx] = True
                else: 
                    check_list[vrtx] = False 
                    stack_l.pop()
                    if not (vrtx + 1) in sorted_grph:
                        sorted_grph.append(vrtx + 1)
                    #sorted_grph[cnt] = vrtx + 1
                    #cnt = cnt - 1
                    continue
                for i in self.edges_list[vrtx]:
                    if visited_list[i] is False:
                        stack_l.append(i)
                    if check_list[i] is True:
                        # graph is cyclic
                        return -1
        return sorted_grph[::-1]

    def conn_comp(self):
        counter = 0
        visited_list = [False] * self.V
        while (all(visited_list) is False):
            for i in range(0, len(visited_list)):
                if visited_list[i] is False:
                    visited_list = self.dfs(i + 1, visited_list)
                    counter = counter + 1
        return counter


if __name__ == "__main__":
    cnt = []
    with open("rosalind_ts.txt", "r") as f:
        #graphs_quant = int(f.readline().strip())
        #for i in range(0, graphs_quant):
        #    f.readline()
        vertex_quant, edges_quant = map(int, f.readline().strip().split())
        grph = myGrph(vertex_quant, edges_quant)
        grph.build_graph(f)
        rslt = grph.topologically_sort()
    with open("ts_answer.txt", "w") as f:
        for i in rslt:
            f.write(str(i) + " ")
