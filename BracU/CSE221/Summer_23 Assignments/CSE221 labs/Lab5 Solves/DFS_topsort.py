

def build_graph():    ## This function builds the graph
    
    input_file = open("input.txt", "r")

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
    global timing
    timing += 1
    start_time[u] = timing
    vis[u] = True
    print(u)
    
    results.append(u)


    for v in g[u]:
        if(vis[v]==False):
            DFS(v,g)

    
    
    timing += 1
    end_time[u] = timing
    
    
    return None







    
    
g = build_graph() ##  This function builds a graph using adjacency list (using dictionary)

start = 1 
timing = 0
vis = [False]*(len(g)+1)
start_time = [0]*(len(g)+1)
end_time = [0]*(len(g)+1)
    
results = []  ##  Variable created for holding the answers
    

for i in range(len(vis)-1,0,-1):
    if(vis[i] is False):
        DFS(i,g)    ## Calling DFS


print(start_time)
print(end_time)
    
stack = []
for i in range(1,len(end_time)):
    stack.append((end_time[i],i))

stack.sort(reverse=True)
print(stack)
output_file = open("output.txt", "w+")   ## Printing results in the output file
for i in results:
    output_file.write(f"{i} ")