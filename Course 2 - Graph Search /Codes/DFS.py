def DFS_intern(graph:dict, start_vertex:int, explored:list=[])->list:
    '''
        Intern loop to apply recursively DFS from a node to one of his not explored linked node.
    '''
    explored.append(start_vertex)
    for node in graph[start_vertex]:
        if node not in explored:
            DFS_intern(graph, node, explored=explored)

def DFS(graph:dict)-> list:
    '''
        Apply DFS on a graph and returned an exploring list.
        Here we apply DFS to every node not explored in the graph.
    '''
    nodes = list(graph.keys())
    explored = [nodes[0]]
    for node in nodes:
        if node not in explored:
            DFS_intern(graph, node, explored=explored)
    return explored