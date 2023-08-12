

def build_graph():    ## This function builds the graph
    
    input_file = open("input5.txt", "r")

    first_line = input_file.readline()

    first_line = first_line.strip()
    row, column = first_line.split(" ")
    column = int(column)
    row = int(row)


    
    
    #We are just storing the input , Grapg is not yet prepared  ( 1 means .  2 means D   0 means #)
    storing = []
    for i in range(row+2):
        storing.append([])
        
    
    for i in range(row+2):
        for j in range(column+2):
            storing[i].append(0)


    
    for i in range(1,row+1):
        new_line = input_file.readline()
        new_line = new_line.split()
        new_line = new_line[0]
        
        for j in range(0,column):
            
            if(new_line[j]=="."):
                
                storing[i][j+1] = 1
                
            elif(new_line[j]=="D"):
                storing[i][j+1] = 2
            else:
                storing[i][j+1] = 0


   

    
    
    ## Each node of the graph is named as (1,1) / (1,2) / (3,4)  etc
    g = {}

    for i in range(1,row+1):
        for j in range(1,column+1):
            g[(i,j)] = []
    
    
    ## For each node we need to check 4 position, top, left, right and bottom and then connect the edges

    for i in range(1,row+1):
        for j in range(1,column+1):
            
            if((storing[i][j])==0):
                continue
            
            
            if((storing[i+1][j])==1 or (storing[i+1][j])==2):
                g[(i,j)].append((i+1,j))
            
            if((storing[i-1][j])==1 or (storing[i-1][j])==2):
                g[(i,j)].append((i-1,j))
            
            if((storing[i][j+1])==1 or (storing[i][j+1])==2):
                g[(i,j)].append((i,j+1))
            
            if((storing[i][j-1])==1 or (storing[i][j-1])==2):
                g[(i,j)].append((i,j-1))
    

    return g,storing,row,column

    

def DFS(u,g):           ## Basic DFS function
    vis[u] = True
   
    if(storing[u[0]][u[1]]==2):
        collected_diamonds[-1].append(1)
    
   
   


    for v in g[u]:
        if(vis[v]==False):
            
            DFS(v,g)

    return None







    
    
g,storing,row,column = build_graph() ##  This function builds a graph using adjacency list (using dictionary)




start = (1,1) 
vis = {}

def reset_graph():
    for i in range(1,row+1):
        for j in range(1,column+1):
            vis[(i,j)] = False


collected_diamonds = []  ##  Variable created for holding the collected diamonds



reset_graph()


# We will Run DFS from each node and check how many diamonds we can collect
for i in range(1,row+1):
    for j in range(1,column+1):
        collected_diamonds.append([])
        DFS((i,j),g)
        reset_graph()


maximum = 0

for i in collected_diamonds:
    if(len(i)>maximum):
        maximum = len(i)

    
output_file = open("output5.txt", "w+")   ## Printing results in the output file

output_file.write(f"{maximum}")

