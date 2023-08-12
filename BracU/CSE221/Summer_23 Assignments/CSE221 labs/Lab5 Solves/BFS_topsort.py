

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

    
    p = {}

    for i in range(1,vertices+1):
        p[i] = []
    
    for i in range(edges):
        new_line = input_file.readline()
        new_line = new_line.split(" ")
        u = int(new_line[0])
        v = int(new_line[1])

        g[u].append(v)
        p[v].append(u)

    return g,p


def BFS(g):

    list_1 = []
    while(len(Q)>0):
        u = Q[0]
        del Q[0]
        list_1.append(u)
        for v in g[u]:
            ans =1
            
            
            for x in p[v]:
                if(vis[x]==False):
                    ans = 0
            
            
            
            if(vis[v]==False and ans==1):
                vis[v] = True
                answers.append(v)
                Q.append(v)


    return list_1


g,p = build_graph() ##  This function builds a graph using adjacency list (using dictionary)


Q = []
answers = []
vis = [False]*(len(g)+1)
vis[1] = True
Q.append(1)
answers.append(1)
x = BFS(g)

print(x)


