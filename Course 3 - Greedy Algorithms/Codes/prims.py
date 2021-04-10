def load_data(filepath:str)->(dict, int, int):
    '''
        Load graph from edges.txt
    '''
    graph = {}
    file = open(filepath, 'r')
    lines = [list(map(int, line.strip().split(' '))) for line in file.readlines()]
    
    n_nodes, n_edges = lines.pop(0)
    
    for line in lines:
        node1, node2, cost = line
        
        # Define edge from node1 to node2
        if node1 in graph.keys():
            graph[node1][node2] = cost
        else:
            graph[node1] = {node2 : cost}
            
        # Then also define edge from node2 to node1
        if node2 in graph.keys():
            graph[node2][node1] = cost
        else:
            graph[node2] = {node1 : cost}
            
    return graph, n_nodes, n_edges 

def prims(graph:dict, start_vertex:int=None)->(list, int):
    '''
        Prim's Algorithms straigthforward implementation with heap data structure for finding MST in a graph.
    '''
    import random
    from heapq import heappush, heappop
    
    if not start_vertex:
        start_vertex = random.choice(list(graph.keys()))
    costs, T = [], []
    X = [start_vertex] ; V = list(graph.keys()) # All nodes 
    
    while set(V) - set(X):
        heap = []
        for node in X:
            for edge in graph[node]:
                if edge not in X:
                    heappush(heap, (graph[node][edge], node, edge)) 
        if heap:  
            cost, node1, node2 = heappop(heap)
            X.append(node2)
            T.append((node1, node2))
            costs.append(cost)
        else:
            break
            
    return T, sum(costs)