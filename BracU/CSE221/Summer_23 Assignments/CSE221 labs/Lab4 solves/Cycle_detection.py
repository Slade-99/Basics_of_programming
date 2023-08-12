

def build_graph():    ## This function builds the graph
    
    input_file = open("input4.txt", "r")

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
       

    return g



def DFS(u,g):           ## Basic DFS function
    vis[u] = 1
    
    
    results.append(u)


    for v in g[u]:
        
        
        if(vis[v]==1):
           
            cycle.append(0)     ## Cycle has been detected
        
        
        
        if(vis[v]==0):
            DFS(v,g)




    vis[u] = 2




    
    
g = build_graph() ##  This function builds a graph using adjacency list (using dictionary)
cycle = []      ## Will contain a 0 if a cycle is detected
start = 1 
vis = [0]*(len(g)+1)
    
    
results = []  ##  Variable created for holding the answers
    
DFS(start,g)    ## Calling DFS

print(cycle)
if(len(cycle)>0):
    final = "Yes"
else:
    final = "No"
    
    
output_file = open("output4.txt", "w+")   ## Printing results in the output file
output_file.write(f"{final} ")