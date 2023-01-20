def readFile():

    f = open("input1B.txt", "r")


    n = f.readline()

    n = n.strip()
    vertices, edges = n.split(" ")
    edges = int(edges)
    vertices = int(vertices)


    buildGraphUsingDictionary(vertices,edges,f)


def buildGraphUsingDictionary(v,c,f):

    graph = {}
    for i in range(v+1):
        graph[i] = []


    print(graph)

    counter = 0
    while (counter < c):
        line = f.readline()
        x = line.split(" ")
        a = int(x[0])
        b = int(x[1])
        d = int(x[2])


        graph[a].append(b)
        graph[a].append(d)




        counter += 1

    file_2 = open("output1B.txt", "w+")


    for i in graph:
        if graph[i] != []:
            print(f"{i}:",end = " ")

            file_2.write(f"{i}: ")


            for j in range(0,len(graph[i]),2):
                print(f"({graph[i][j]},{graph[i][j+1]})",end = " ")

                file_2.write(f"({graph[i][j]},{graph[i][j+1]}) ")

            file_2.write(f"\n")
            print()

        else:
            print(f"{i}:")

readFile()


"""
a) If it is an undirected graph then we had to append twice for each edge.
b) Not possible beacuse in adjacency matrix we can store only one value for each connection between nodes.
"""


