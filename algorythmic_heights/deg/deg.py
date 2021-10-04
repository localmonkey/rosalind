

if __name__ == "__main__":
    z = []
    max_vertex = 0
    with open("test.txt", "r") as f:
        vertexes_quant, edges_quant = map(lambda x:int(x), f.readline().strip().split())
        z = [0]*vertexes_quant
        for line in f:
            vertex, connected_vertex = map(lambda x:int(x), line.strip().split())
            z[vertex - 1] = z[vertex - 1] + 1
            z[connected_vertex- 1] = z[connected_vertex - 1] + 1

    with open("deg_output.txt", "w") as f:
        for i in z:
            print(i, end=' ')
            f.write(f"{i} ")

