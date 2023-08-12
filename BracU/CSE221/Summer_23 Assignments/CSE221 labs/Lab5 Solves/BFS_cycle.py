

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


def BFS(g):

    list_1 = []
    while(len(Q)>0):
        u = Q[0]
        del Q[0]
        list_1.append(u)
        for v in g[u]:
            
            
            if(vis[v]==True):

                x = u
                
                for i in range(distance[u]-distance[v]):
                    x = parent[x]
                
                if(x==v):
                    print("Cycle Detected")
            
            
            
            if(vis[v]==False):
                vis[v] = True
                parent[v] = u
                
                distance[v] = distance[u]+1
                Q.append(v)


    


g = build_graph() ##  This function builds a graph using adjacency list (using dictionary)
distance = [0]*(len(g)+1)
parent = [0]*(len(g)+1)
Q = []
answers = []
vis = [False]*(len(g)+1)






for i in range(1,len(vis)):
    
    if(vis[i] is False):
            vis[i] = True
            Q.append(i)
            
            
            BFS(g)    ## Calling DFS
            

