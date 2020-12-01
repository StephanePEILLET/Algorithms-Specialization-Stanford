def kargerMinCut(graph:dict, verbose:bool=False)->int:
    '''
        Cut a graph in order to find minCuts with Karger algorithm.
    '''
    import random
    
    n = len(graph)
    if n == 2:
        return len(graph[next(iter(graph))])
    else:
        # Select randomly an edge (two nodes) in the graph
        n1_to_cut = random.choice(list(graph.keys()))        
        n2_to_cut = random.choice(graph[n1_to_cut])
        
        if verbose:
            print('Before transformation')
            print('graph', graph)
            print('n1_to_cut', n1_to_cut)
            print('n2_to_cut', n2_to_cut)
            print(f'graph[{n1_to_cut}] : {graph[n1_to_cut]}')
            print(f'graph[{n2_to_cut}] : {graph[n2_to_cut]}')
            
        [graph[n1_to_cut].remove(n2_to_cut) for t in range(graph[n1_to_cut].count(n2_to_cut))]
        [graph[n2_to_cut].remove(n1_to_cut) for t in range(graph[n2_to_cut].count(n1_to_cut))]
        graph[n1_to_cut].extend(graph[n2_to_cut])
        
        for i in graph[n2_to_cut]:   # Replace node n2 connection to n1
            graph[i] = [n1_to_cut if node==n2_to_cut else node for node in graph[i]] 
        
        graph.pop(n2_to_cut) # Delete the second randomly chosen node    
        
        if verbose:
            print('After transformation')
            print('graph', graph)

        return kargerMinCut(graph, verbose) # Continue as long as there are only two nodes left

def countingCuts(graph:dict)->int:
    '''
        Count the numbers of mincuts in a graph.
        Do n trials and returns the best result with a minimum of cuts.
    '''
    import copy
    results = []
    n = len(graph)
    for x in range(n):
        temp_graph = copy.deepcopy(graph)
        results.append(kargerMinCut(temp_graph))
    return min(results)