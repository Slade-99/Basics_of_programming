from queue import PriorityQueue


def matrix(file, vertices, edges):

    G = []

    for i in range(vertices+1):
        G.append([0]*(vertices+1))

    for i in range(edges):
        y = file.readline().strip("\n").split(" ")

        u = int(y[0])
        v = int(y[1])
        w = int(y[2])

        G[u][v] = w

    return G


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
    file_1 = open('input3.txt', 'r')

    test_cases = int(file_1.readline().strip("\n"))

    file_2 = open("output3.txt", "w")

    for i in range(test_cases):
        start = file_1.readline().strip("\n").split(" ")
        vertices = int(start[0])
        edges = int(start[1])
        graph = matrix(file_1, vertices, edges)

        destination = vertices

        output = dijkstras(graph, 1)


        y = output[1]
        z = output[0]
        print(z)
        print(y)
        track = []
        i = destination

        while i != None:
            track.append(i)
            i = y[i]


        j = len(track)

        while j>0:

            file_2.write(f"{track[j-1]} ")
            j-=1
        file_2.write(f"\n")


output = graphProcess()
