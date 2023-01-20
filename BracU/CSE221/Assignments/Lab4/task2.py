def readFile():

    f = open("input2.txt", "r")


    n = f.readline()

    n = n.strip()
    vertices, edges = n.split(" ")
    edges = int(edges)
    vertices = int(vertices)


    output = buildGraphUsingDictionary(vertices,edges,f)

    colour = {}
    for i in range(1, vertices+1):
        colour[i] = 0


    s = 1
    traversal = []
    Q = []

    colour[s] = 1

    Q.append(s)

    while len(Q) != 0 :
        u = Q[0]

        traversal.append(u)
        Q = Q[1:]


        for i in output[u]:
            if colour[i] == 0:

                colour[i] = 1
                Q.append(i)


    file_2 = open("output2.txt", "w+")

    for i in traversal:
        print(i,end = " ")
        file_2.write(f"{i} ")













    return output





def buildGraphUsingDictionary(v,c,f):

    graph = {}
    for i in range(1,v+1):
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




