import queue


def bfs(vrtx, adj_list, visited):
    q = queue.Queue()
    q.put(vrtx)
    while(not q.empty()):
        vrtxf = q.get()
        visited[vrtxf] = True
        for i in adj_list[vrtxf]:
            if (visited[i] == False):
                q.put(i)
    return visited

def bfs_modified(vrtx, adj_list, visited):
    q = queue.Queue()
    q.put(vrtx)
    
    depth = 0
    acc = 0
    while(not q.empty()):
        vrtxf = q.get()
        visited[vrtxf] = True
        if depth < 1:
            for i in adj_list[vrtxf]:
                if (visited[i] == False):
                    q.put(i)
        if depth >= 1:
            acc = acc + len(adj_list[vrtxf])
        depth = depth + 1
    return acc


if __name__ == "__main__":
    with open("rosalind_ddeg.txt", "r") as f:
        vertexes_quant, edges_quant = map(lambda x:int(x), f.readline().strip().split())
        z = [[]]*vertexes_quant
        for line in f:
            vertex, connected_vertex = map(lambda x:int(x), line.strip().split())
            z[vertex - 1] = z[vertex - 1] + [connected_vertex - 1]
            z[connected_vertex - 1] = z[connected_vertex - 1] + [vertex - 1]

    with open("ddeg_output.txt", "w") as f:
        for i in range(0, vertexes_quant):
            des_result = bfs_modified(i, z, [False]*vertexes_quant)
            print(des_result, end=' ')
            f.write(f"{des_result} ")

