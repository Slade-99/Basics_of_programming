

def build_graph():    ## This function builds the graph
    
    input_file = open("input3.txt", "r")

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



def DFS(u,g):           ## Basic DFS function
    vis[u] = True
    print(u)
    
    results.append(u)


    for v in g[u]:
        if(vis[v]==False):
            DFS(v,g)

    return None







    
    
g = build_graph() ##  This function builds a graph using adjacency list (using dictionary)

start = 1 
vis = [False]*(len(g)+1)
    
    
results = []  ##  Variable created for holding the answers
    
DFS(start,g)    ## Calling DFS

    
    
    
output_file = open("output3.txt", "w+")   ## Printing results in the output file
for i in results:
    output_file.write(f"{i} ")