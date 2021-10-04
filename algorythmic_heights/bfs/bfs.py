import queue


def bfs(vrtx, adj_list, visited):
    q = queue.Queue()
    q.put(vrtx)
    while(not q.empty()):
        vrtxf = q.get()
        visited[vrtxf] = True
        for i in adj_list[vrtxf]:
            if (visited[i] is False):
                q.put(i)
    return visited


def bfs_modified(vrtx, adj_list, visited, paths):
    q = queue.Queue()
    q.put(vrtx)

    curr_path = 0
    paths[vrtx] = 0
    while(not q.empty()):
        vrtxf = q.get()
        visited[vrtxf] = True
        curr_path = paths[vrtxf]
        for i in adj_list[vrtxf]:
            if (visited[i] is False):
                if paths[i] == -1:
                    # TODO: check if all ifs are needed
                    paths[i] = curr_path + 1
                elif paths[i] >= curr_path + 1:
                    paths[i] = curr_path + 1
                q.put(i)
    return


if __name__ == "__main__":
    with open("rosalind_bfs.txt", "r") as f:
        vertexes_quant, edges_quant = map(lambda x: int(x),
                                          f.readline().strip().split())
        z = [[]]*vertexes_quant
        for line in f:
            vertex, connected_vertex = map(lambda x: int(x),
                                           line.strip().split())
            z[vertex - 1] = z[vertex - 1] + [connected_vertex - 1]

    path_lengths = [-1]*vertexes_quant
    bfs_modified(0, z, [False]*vertexes_quant, path_lengths)
    with open("bfs_output.txt", "w") as f:
        for i in range(0, vertexes_quant):
            print(path_lengths[i], end=' ')
            f.write(f"{path_lengths[i]} ")
