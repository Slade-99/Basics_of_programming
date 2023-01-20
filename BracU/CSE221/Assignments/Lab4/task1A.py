

def readFile():


    f = open("input1A.txt", "r")


    n = f.readline()


    n = n.strip()
    vertices,edges = n.split(" ")
    edges = int(edges)
    vertices = int(vertices)

    buildGraphUsingListofLists(vertices,edges, f)


def buildGraphUsingListofLists(v,c,f):

    graph = [[0]*(v+1) for i in range(v+1)]



    counter = 0
    while(counter<c):
        line = f.readline()
        x = line.split(" ")
        a = int(x[0])
        b = int(x[1])
        d = int(x[2])






        graph[a][b] = d
        counter += 1


    file_2 = open("output1A.txt", "w+")


    for i in graph:
        for j in i:
            file_2.write(f"{j} ")
        file_2.write("\n ")

    file_2.close()








readFile()

