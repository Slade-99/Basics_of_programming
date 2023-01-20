from queue import PriorityQueue


def matrix(file, vertices, edges):

    G = []

    for i in range(vertices+1):
        G.append([0]*(vertices+1))

    for i in range(edges):
        y = file.readline().strip("\n").split(" ")

        u = int(y[0])
        v = int(y[1])
        w = -1*int(y[2])

        G[u][v] = w

    source = int(file.readline().strip("\n").split(" ")[0])


    return G,source


def dijkstras(G, source):

    q = PriorityQueue()
    size = len(G)
    distance = [9999]*size
    distance[source] = 0

    visited = [False]*size
    previous = [None]*size
    for i in range(size):
        v = i
        w = distance[i]
        q.put((w, v))

    while q.empty() == False:
        u = q.get()[1]

        if visited[u]:
            continue
        visited[u] = True

        for v in range(size):
            if G[u][v] != 0:
                alt = distance[u] + G[u][v]
                if alt < distance[v]:
                    distance[v] = alt
                    previous[v] = u

                    q.put((alt, v))

    return distance, previous


def graphProcess():
    file_1 = open('input5.txt', 'r')

    test_cases = int(file_1.readline().strip("\n"))

    file_2 = open("output5.txt", "w")

    for i in range(test_cases):
        start = file_1.readline().strip("\n").split(" ")
        vertices = int(start[0])
        edges = int(start[1])
        received = matrix(file_1, vertices, edges)

        graph = received[0]
        source = received[1]



        output = dijkstras(graph, source)
        x = output[0]

        y = output[1]



        print(x)
        print(y)

        i = 1
        paths = []
        while i<len(x):
            if x[i] ==0:
                paths.append(0)
                i += 1
            elif x[i] == 9999:
                paths.append(-1)
                i += 1
            else:
                highest_value = 9999
                j = i

                while(y[j]!= None):
                    v = j
                    u = y[j]
                    value = -1*graph[u][v]
                    if value<highest_value:
                        highest_value = value

                    j = y[j]

                paths.append(highest_value)
                i += 1


        for i in paths:
            file_2.write(f"{i} ")
        file_2.write("\n")


        print(graph)
        print(paths)








output = graphProcess()




