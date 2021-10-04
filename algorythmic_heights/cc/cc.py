class myGrph:
    def __init__(self, V_quant, E_quant):
        self.V = V_quant
        self.E = E_quant
        self.edges_list = [[]] * self.V

    def build_graph(self, f):
        for i in range(0, self.E):
            vertex1, vertex2 = map(int, f.readline().strip().split())
            self.edges_list[vertex1 - 1] = self.edges_list[vertex1 - 1] + [vertex2 - 1]
            self.edges_list[vertex2 - 1] = self.edges_list[vertex2 - 1] + [vertex1 - 1]

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
    with open("rosalind_cc.txt", "r") as f:
        vertex_quant, edges_quant = map(int, f.readline().strip().split())
        grph = myGrph(vertex_quant, edges_quant)
        grph.build_graph(f)
    cnt = grph.conn_comp()
    with open("cc_answer.txt", "w") as f:
        f.write(str(cnt))
