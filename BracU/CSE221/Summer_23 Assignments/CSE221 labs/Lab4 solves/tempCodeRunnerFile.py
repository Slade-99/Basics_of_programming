

def build_graph():    ## This function builds the graph
    
    input_file = open("input5.txt", "r")

    first_line = input_file.readline()

    first_line = first_line.strip()
    row, column = first_line.split(" ")
    column = int(column)
    row = int(row)


    
    
    #We are just storing the input , Grapg is not yet prepared  ( 1 means .  2 means D   0 means #)
    storing = [[0]*(column+1)]*(row+1)
    print(storing)
    
    
    for i in range(1,row+1):
        new_line = input_file.readline()
        new_line = new_line.split()
        for j in range(0,column):
            if(new_line[j]=="."):
                storing[i][j+1] = 1
            elif(new_line[j]=="D"):
                storing[i][j+1] = 2
            else:
                storing[i][j+1] = 0


    print(storing)
    g = {}

    for i in range(1,row+1):
        g[i] = []
    return g

    
"""
def DFS(u,g):           ## Basic DFS function
    vis[u] = True
    print(u)
    
    results.append(u)


    for v in g[u]:
        if(vis[v]==False):
            DFS(v,g)

    return None






"""
    
    
g = build_graph() ##  This function builds a graph using adjacency list (using dictionary)


"""

start = 1 
vis = [False]*(len(g)+1)
    
    
results = []  ##  Variable created for holding the answers



  
DFS(start,g)    ## Calling DFS

    
    
    
output_file = open("output5.txt", "w+")   ## Printing results in the output file
for i in results:
    output_file.write(f"{i} ")


    """