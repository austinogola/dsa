class Graph(object):

    def __init__(self):
        self.adjacencyList={}

    def addVertex(self,name):
        if name in self.adjacencyList:
            None
        else:
            self.adjacencyList[name]=[]

    def addEdge(self,parent,child):
        if parent in self.adjacencyList:
            self.adjacencyList[parent].append(child)
            self.adjacencyList[child]=[parent]
        else:
            self.adjacencyList[parent]=[]
            self.adjacencyList[child]=[]
            self.adjacencyList[parent].append(child)
            self.adjacencyList[child].append(parent)

    def removeEdge(self,parent,child):
        self.adjacencyList[parent].remove(child)
        self.adjacencyList[child].remove(parent)

    def removeVertex(self,name):
        if name in self.adjacencyList:
            while (len(self.adjacencyList[name])>0):
                parent=self.adjacencyList[name][-1]
                self.adjacencyList[name].pop()
                self.adjacencyList[parent].remove(name)
            self.adjacencyList.pop('Nigeria')

    def bfs(self):




gr=Graph()
gr.addVertex('Kenya')
gr.addVertex('Nigeria')
gr.addVertex('Egypt')
gr.addEdge('Kenya','Uganda')
gr.addEdge('Egypt','Algeria')
gr.addEdge('Kenya','Tanzania')
gr.addEdge('Zambia','DRC')
gr.removeEdge('Kenya','Uganda')
gr.addEdge('Nigeria','Ghana')
gr.addEdge('Nigeria','Togo')
gr.removeVertex('Nigeria')

print(gr.adjacencyList)
