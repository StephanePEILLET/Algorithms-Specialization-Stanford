def DFS_find_cycle(graph:dict)->bool:
    '''
        NOT FINISHED 
        Apply DFS on a graph and find if the graph is acyclic. Here we apply DFS to every node not explored in the graph.
    '''
    
    def DFS(graph:dict, node_i:int, explored:list)-> (list, bool):
        '''
            Intern loop to apply DFS from a starting node to all of his linkend nodes not explored.
        '''
        stack = [node_i]
        while stack:
            node_j = stack[-1]
            if node_j not in explored:
                explored.append(node_j)
                for el in reversed(graph[node_j]):
                    if el not in explored:
                        stack.append(el)
            else:              
                stack.pop()               
        return explored, False
    
    nodes = list(graph.keys())
    explored = []; is_cycle = False
    for node in reversed(nodes):
        if node not in explored:
            if not is_cycle:
                explored, is_cycle = DFS(graph, node, explored)
            else:
                return is_cycle
    return is_cycle 


def kruskal_straightforward(graph:dict)->(list, int):
    '''
        Implementation of Kruskal's Algorithm to find MST in a graph and its cost.
    '''
    from heapq import heappush, heappop 

    T, heap, costs = set(), [], []
    for node1 in graph.keys():
        for node2 in graph[node]:
            heappush(heap, (graph[node][edge], set((node1, node2)))) # Sorted edge by increasing cost

    while heap:
        cost, i = heappop(heap)
        if not DFS_find_cycle(T.union(i)): # If T Union {i} has no cycles
            T.add(i)
            costs.append(cost)
            
    return T, sum(costs)