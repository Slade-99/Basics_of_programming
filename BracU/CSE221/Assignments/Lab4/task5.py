def readFile():

    f = open("input5.txt", "r")

    n = f.readline()

    n = n.strip()
    vertices, edges, destination = n.split(" ")
    edges = int(edges)
    vertices = int(vertices)
    destination = int(destination)

    x = buildGraphUsingDictionary(vertices, edges, f)
    return x,destination

def buildGraphUsingDictionary(v, c, f):

    graph = {}
    for i in range(v+1):
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








y = readFile()

graph = y[0]
destination = y[1]


source = 1


def BFS(graph,source):
    colour = ["white"]*(len(graph))
    distance = [9999]*(len(graph))
    parent = [None]*(len(graph))
    colour[source] = "grey"
    distance[source] = 0
    parent[source] = None


    queue = []
    queue.append(source)


    while len(queue) != 0:
        u = queue[0]
        queue = queue[1:]
        for i in graph[u]:
            if colour[i] == "white":
                colour[i] = "grey"
                distance[i] = distance[u]+1
                parent[i] = u
                queue.append(i)

        colour[u] = 'black'

    return distance,parent




g = BFS(graph,source)
distance= g[0]
parent = g[1]

def output(distance,parent,destination,source):
    answer = []
    i = destination
    answer.append(destination)
    while parent[i] != 1:
        answer.append(parent[i])
        i = parent[i]
    answer.append(source)

    file_2 = open("output5.txt", "w+")
    file_2.write(f"Time: {distance[destination]} ")
    file_2.write(f"\n ")
    print(distance[destination])
    j = len(answer) -1
    while (j>=0):
        print(answer[j],end=" ")
        file_2.write(f"{answer[j]} ")

        j -= 1



output(distance,parent,destination,source)