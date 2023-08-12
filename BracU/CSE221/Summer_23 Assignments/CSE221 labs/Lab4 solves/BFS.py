

def build_graph():    ## This function builds the graph
    
    input_file = open("input2.txt", "r")

    first_line = input_file.readline()

    first_line = first_line.strip()
    vertices, edges = first_line.split(" ")
    edges = int(edges)
    vertices = int(vertices)


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

    return g


def BFS(g):

    
    while(len(Q)>0):
        u = Q[0]
        del Q[0]
        for v in g[u]:
            if(vis[v]==False):
                vis[v] = True
                answers.append(v)
                Q.append(v)





g = build_graph() ##  This function builds a graph using adjacency list (using dictionary)


Q = []
answers = []
vis = [False]*(len(g)+1)
vis[1] = True
Q.append(1)
answers.append(1)
BFS(g)



output_file = open("output2.txt", "w+")   ## Printing results in the output file
for i in answers:
    output_file.write(f"{i} ")