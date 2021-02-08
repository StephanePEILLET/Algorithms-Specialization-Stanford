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
        
        
def DFS(graph:dict, node_i:int, params:Params=False, use_stack:bool=False)->Params:
    '''
        Intern loop to apply DFS from a starting node to all of his linkend nodes not explored.
    '''
    if params == None:
        params = Params()
        
    if use_stack: # With stack method
        stack = [node_i]
        while stack:
            node_j = stack[-1]
            if node_j not in params.explored:
                    params.explored.append(node_j)
                    for el in reversed(graph[node_j]):
                        if el not in params.explored:
                            stack.append(el)
            else:              
                stack.pop()
                params.t += 1
                params.finishing_time[node_j]= params.t
                params.leader[node_j] = params.s
                params.SCCs[params.s].append(node_j) 
    
    else: # With recurrence method
        params.explored.append(node_i)
        params.leader[node_i]= params.s
        params.SCCs[params.s].append(node_i) 
        for node_j in graph[node_i]:
            if node_j not in params.explored:
                params = DFS(graph, node_j, params=params, use_stack=use_stack)
        params.t += 1
        params.finishing_time[node_i]= params.t
    
    return params 


def DFS_loop(graph:dict, use_stack:bool=False)-> list:
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
            params = DFS(graph, node, params=params, use_stack=use_stack)
    return params 