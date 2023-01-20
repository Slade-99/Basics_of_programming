def readFile():

    f = open("input3.txt", "r")

    n = f.readline()

    n = n.strip()
    vertices, edges = n.split(" ")
    edges = int(edges)
    vertices = int(vertices)

    output = buildGraphUsingDictionary(vertices, edges, f)

    colour = {}
    for i in range(1, vertices+1):
        colour[i] = 0

    s = 1

    traversal = []
    traversal.append(s)

    def DFS(output,s):
        colour[s] = 1
        for i in output[s]:
            if colour[i] == 0:
                traversal.append(i)
                DFS(output,i)


    DFS(output,s)


    file_2 = open("output3.txt", "w+")

    for i in traversal:
        print(i, end=" ")
        file_2.write(f"{i} ")

    return output


def buildGraphUsingDictionary(v, c, f):

    graph = {}
    for i in range(1, v+1):
        graph[i] = []

    counter = 0
    while (counter < c):
        line = f.readline()
        x = line.split(" ")
        a = int(x[0])
        b = int(x[1])

        graph[a].append(b)
        graph[b].append(a)

        counter += 1

    return graph


G = readFile()
