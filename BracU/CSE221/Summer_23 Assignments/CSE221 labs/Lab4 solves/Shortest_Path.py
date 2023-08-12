

def build_graph():    ## This function builds the graph
    
    input_file = open("input5.txt", "r")

    first_line = input_file.readline()

    first_line = first_line.strip()
    vertices, edges, destination = first_line.split(" ")
    edges = int(edges)
    vertices = int(vertices)
    destination = int(destination)

    g = {}

    for i in range(1,vertices+1):
        g[i] = []

    for i in range(edges):
        new_line = input_file.readline()
        new_line = new_line.split(" ")
        u = int(new_line[0])
        v = int(new_line[1])

        g[u].append(v)
        g[v].append(u)

    return g,destination


def BFS(g):

    
    while(len(Q)>0):
        u = Q[0]
        del Q[0]
        for v in g[u]:
            if(vis[v]==False):
                vis[v] = True
                distance[v] = distance[u]+1
                parent[v] = u
                answers.append(v)
                Q.append(v)





g,destination = build_graph() ##  This function builds a graph using adjacency list (using dictionary)


Q = []
answers = []
vis = [False]*(len(g)+1)
vis[1] = True
Q.append(1)
answers.append(1)
distance = [0]*(len(g)+1)
parent = [0]*(len(g)+1)
BFS(g)




answers = []
answers.append(destination)
x = parent[destination]
while(x!=1):
    answers.append(x)
    x = parent[x]
answers.append(1)
answers.reverse()


output_file = open("output5.txt", "w+")   ## Printing results in the output file
output_file.write(f"Time: {distance[destination]}\n ")
for i in answers:
    output_file.write(f"{i} ")