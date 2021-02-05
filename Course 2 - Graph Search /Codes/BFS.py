def BFS(graph:dict, start_vertex:int)-> (list, dict):
    '''
        Breadth First Search(BFS) algorithm, navigate through a whole graph and return  
        the exploring order of the graph and the layers by which the graph has been explored.
    '''
    if start_vertex not in graph.keys():
        print('Starting vertex not in the graph ...')
        return [], {}
    
    explored, queue, exploring_order = [start_vertex], [start_vertex], [start_vertex]
    index = 1 ; layers = {0 : [start_vertex], index: []}; prev_queue = queue.copy()

    while queue:
        if all([node not in prev_queue for node in queue]):
            index += 1
            layers[index] = []
            prev_queue = queue.copy()
        
        v = queue.pop(0)
        for w in graph[v]:
            if w not in explored:
                explored.append(w); exploring_order.append(w); queue.append(w)
                layers[index].append(w)
                
    layers.popitem() 
    return exploring_order, layers


def BFS_shortest_path(graph:dict, start_vertex:int, target_vertex:int)->(int, list):
    '''
        Return the shortest path and his distance with BFS [and random selection].
    '''
    import random
    if start_vertex and target_vertex not in graph.keys():
        print('Used vertex not in the graph ...')
        return None, []
    
    exploring_order, layers = BFS(graph, start_vertex)
    
    for index, layer in layers.items():
        if target_vertex in layer:
            distance = index
    
    shortest_path = [0] * (distance+1)
    shortest_path[distance] = target_vertex
    
    for i in reversed(range(distance)):
        shortest_path[i] = random.choice([node for node in layers[i] if node in graph[shortest_path[i+1]]])             
    
    return distance, shortest_path


def BFS_SCC(graph:dict)->(int, list):
    '''
        Return the number of connected components and a list with its.
    '''
    import random 
    nodes = list(graph.keys())
    explored, SCCs = [nodes[0]], []
    
    for node in nodes:
        if node not in explored:
            exploring_order, _ = BFS(graph, node)
            explored.extend(exploring_order); SCCs.append(sorted(exploring_order))
    return len(SCCs), SCCs


def BFS_display(graph:dict, start_vertex:int, target_vertex:int=None)->None:
    '''
        Display order, layers, shortest path obtained thanks to BFS algorithm on a graph.
    '''
    exploring_order, layers = BFS(graph, start_vertex)
    print(f'Start exploration with the node {start_vertex}')
    print('- Exploring Order:', exploring_order); print('- Layers:', layers, '\n')
    
    if target_vertex is not None:
        distance, shortest_path = BFS_shortest_path(graph, 's', 'e')
        print(f'BFS shortest path: start vertex {start_vertex} and target vertex {target_vertex}')
        print(f'Distance path: {distance} and shortest path: {shortest_path}')