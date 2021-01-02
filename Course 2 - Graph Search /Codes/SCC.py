class Node:
    def __init__(self, index:int):
        self.index = index
        self.is_explored = False
        self.links = []
        self.links_rev = []
        self.finish_time = 0
    
    def add_link(self, link_index):
        self.links.append(link_index)
        
    def add_rev(self, link_index):
        self.links_rev.append(link_index)

class Graph:
    def __init__(self, nbr_nodes:int):
        self.t = 0
        self.s = 0
        self.leader = {}
        self.length = nbr_nodes
        self.nodes = {k: Node(k) for k in range(nbr_nodes)}
        
    def add_link_to_node(self, node_index, link_index):
        self.nodes[node_index].add_link(link_index)
        self.nodes[link_index].add_rev(node_index)
    
    def get(self,node_index):
        node = self.nodes[node_index]
        print(f'Node: {node.index} -linked to:{node.links} -is explored:{node.is_explored} f(i):{node.finish_time}')

def create_graph(file_name:str, nbr_nodes:int)->dict:
    '''
        From SCC file create a graph and reverse graph.
        SCC extract : 
                            1 1 
                            1 2 
                            1 5 
                            ...
                            2 47646      
                            2 47647 
                            2 13019 
                            2 47648 
                            ...
    '''
    file = open(file_name,"r")
    data = file.readlines()
    graph = Graph(nbr_nodes)
    
    for line in data:
        node_start, node_end = list(map(lambda x: int(x),line.split())) 
        graph.add_link_to_node(node_start, node_end)

    return graph        
        
def DFS(graph:dict, start_vertex:int)->None:
    graph[start_vertex].is_explored = True
    graph.leader[start_vertex] = graph[graph.s]
    for i in graph.nodes.keys():
        for j in graph[i].links:
            if graph[j].is_explored:
                DFS(graph, j)
    graph.t += 1
    graph[start_vertex].finish_time = graph.t 

def DFS_Loop(graph:Graph)->None:
    for i in range(graph.length, 0, -1):
        if not graph[i].is_explored:
            graph.s = i
            DFS(graph, i)    

def get_SCC(graph:dict)->int:
    return        

