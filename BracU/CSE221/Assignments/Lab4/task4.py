def readFile():

    f = open("input4.txt", "r")

    n = f.readline()

    n = n.strip()
    vertices, edges= n.split(" ")
    edges = int(edges)
    vertices = int(vertices)


    x = buildGraphUsingDictionary(vertices, edges, f)

    return x


def buildGraphUsingDictionary(v, c, f):

    graph = {}
    for i in range(v+1):
        graph[i] = []

    counter = 0
    while (counter < c):
        line = f.readline()
        x = line.split(" ")
        a = int(x[0])
        b = int(x[1])

        graph[a].append(b)


        counter += 1

    return graph


y = readFile()

y.pop(0)
print(y)



class DFS:
    def __init__(self,graph):
        self.graph = graph
        self.colour = ["white"]*(len(graph)+1)
        self.parent = [None]*(len(graph)+1)
        self.time = 0
        self.distance = [None]*(len(graph)+1)
        self.finish = [None]*(len(graph)+1)
        self.backedge = []



    def dfs_start(self):
        for i in self.graph:
            if self.colour[i] == "white":
                self.dfs_visit(i)

    def dfs_visit(self,u):
        self.time = self.time +1
        self.distance[u] = self.time
        self.colour[u] = "grey"
        for j in self.graph[u]:
            if self.colour[j] == "white":
                self.parent[j] = u
                self.dfs_visit(j)
            elif self.colour[j] == "grey":
                self.backedge.append(1)

        self.colour[u] = "black"
        self.time = self.time + 1
        self.finish[u] = self.time


    def output(self):
        return self.backedge


file_2 = open("output4.txt", "w+")
given = DFS(y)
given.dfs_start()
final = given.output()
if len(final)>0:
    print(True)
    file_2.write(f"True ")

else:
    print(False)
    file_2.write(f"False ")
