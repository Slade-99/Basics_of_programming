from queue import PriorityQueue



def graphProcess():
    file_1 = open('input1.txt','r')

    contents = file_1.read()

    listed = contents.split("\n")

    final = []

    file_1.close()

    for i in listed:
        for j in i.split(" "):
            final.append(j)



    mapping_list = []
    for i in final:
        if i not in mapping_list and i not in "1234567890":
            mapping_list.append(i)




    vertices_count = len(mapping_list)

    G = []

    for i in mapping_list:
        G.append([0]*vertices_count)


    for i in range(0,len(final),3):
        u = final[i]
        v = final[i+1]
        w = final[i+2]


        mapped_u = mapping_list.index(u)
        mapped_v = mapping_list.index(v)

        G[mapped_u][mapped_v] = int(w)


    return G,mapping_list

output = graphProcess()

G = output[0]
vertices = output[1]

source = vertices.index("Motijheel")


def dijkstras(G,source):

    q = PriorityQueue()
    size = len(G)
    distance = [9999]*size
    distance[source] = 0


    visited = [False]*size
    previous = [None]*size
    for i in range(size):
        v = i
        w = distance[i]
        q.put((w,v))




    while q.empty() == False:
        u = q.get()[1]

        if visited[u]:
            continue
        visited[u] = True

        for v in range(size):
            if G[u][v] != 0:
                alt = distance[u] + G[u][v]
                if alt< distance[v]:
                    distance[v] = alt
                    previous[v] = u





                    q.put((alt,v))


    return distance,previous









x = dijkstras(G,source)
z= x[0]
y = x[1]


destination = vertices.index("MOGHBAZAR")


i = source
file_2 = open("output1.txt", "w")
while i != destination:

    file_2.write(f"{vertices[i]}->")
    print(f"{vertices[i]}->" ,end="")

    i = y.index(i)


file_2.write(f"{vertices[destination]}")
print(vertices[destination])


file_2.close()

"""
We use BFS for finding the shortest path if the edges are unweighted or the weight in all the edges are same.



"""