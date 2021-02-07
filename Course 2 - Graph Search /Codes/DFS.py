class Params:
    '''
        Parameters passed during graph exploration
    '''
    def __init__(self):
        self.explored = []
        self.s = 0
        self.leader = {}
        self.leaders = []
        self.t = 0
        self.finishing_time = {}
        self.SCCs = {}

def DFS_simple_exploration(graph:dict, start_vertex:int, params:Params=None)->list:
    '''
        Apply recursively DFS from a starting node to explored all linked nodes.
    '''
    if params == None:
        params = Params()
    params.explored.append(start_vertex)
    for node in graph[start_vertex]:
        if node not in params.explored:
            params = DFS_simple_exploration(graph, node, params=params)
    return params   
        
        
def DFS(graph:dict, node_i:int, params:Params=None)->Params:
    '''
        Intern loop to apply recursively DFS from a node to one of his not explored linked node.
    '''
    if params == None:
        params = Params()
    params.explored.append(node_i)
    params.leader[node_i]= params.s
    params.SCCs[params.s].append(node_i) 
    for node_j in graph[node_i]:
        if node_j not in params.explored:
            params = DFS(graph, node_j, params=params)
    params.t += 1
    params.finishing_time[node_i]= params.t
    return params 


def DFS_loop(graph:dict)-> list:
    '''
        Apply DFS on a graph and returned an exploring list.
        Here we apply DFS to every node not explored in the graph.
    '''
    nodes = list(graph.keys())
    params = Params()
    for node in reversed(nodes):
        if node not in params.explored:
            params.s = node
            params.SCCs[params.s] = []
            params = DFS(graph, node, params=params)
    return params 
