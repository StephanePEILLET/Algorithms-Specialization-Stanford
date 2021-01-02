class Node:
    def __init__(self, index:int):
        self.index = index
        self.is_explored = False
        self.links = []
        self.finish_time = 0
    
    def add_link(self, link_index):
        self.links.append(link_index)

class SCC:
    def _init_(self):
        self.nodes = {}
        self.SCC_size = 0
    
class Graph:
    def __init__(self, nbr_nodes:int):
        self.t = 0
        self.s = 0
        self.leader = {}
        self.nbr_nodes = nbr_nodes
        self.nodes = {k: Node(k) for k in range(nbr_nodes)}
        self.nodes_reverse = {k: Node(k) for k in range(nbr_nodes)}
        self.SCCs = []
        
    def add_link_to_node(self, node_index, link_index):
        self.nodes[node_index].add_link(link_index)
        self.nodes_reverse[link_index].add_link(node_index)
    
    def get_node(self,node_index):
        node = self.nodes[node_index]
        print(f'Node: {node.index} -linked to:{node.links} -is explored:{node.is_explored} f(i):{node.finish_time}')
        return node
    
    def DFS(G:dict, start_vertex:int, on_reverse:bool=False)->None:
        G = graph.nodes if not on_reverse else graph.nodes_reverse
        G[start_vertex].is_explored = True
        graph.leader[start_vertex] = G[graph.s]
        for i in G.keys():
            for j in G[i].links:
                if G[j].is_explored:
                    DFS(graph, j, on_reverse)
        graph.t += 1
        graph[start_vertex].finish_time = graph.t 

    def DFS_Loop(graph:Graph, on_reverse:bool=False)->None:
        G = graph.nodes if not on_reverse else graph.nodes_reverse
        for i in range(graph.nbr_nodes, 0, -1):
            if not G[i].is_explored:
                graph.s = i
                DFS(graph, i, on_reverse)    

    def Korasaju(graph:dict)->int:
        DFS_loop(graph_rev)
        scc = DFS_loop2(graph, num_nodes)
        return len(graph.SCCs)  