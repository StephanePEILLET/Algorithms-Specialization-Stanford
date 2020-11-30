def kargerMinCut(graph:dict)->dict:
    '''
        Cut a graph in order to find minCuts with Karger algorithm.
    '''
    import random
    n = len(graph)
    if n == 2:
        return graph
    else:
        # Select randomly an edge (two nodes) in the graph
        n1_to_cut = random.choice(list(graph.keys()))
        n2_to_cut = random.choice(graph[n1_to_cut])
        # Connected n1 to n2 
        graph[n1_to_cut].extend(graph[n2_to_cut].remove(n1_to_cut))  
        for i in graph[n2_to_cut]:
            if n1_to_cut in graph[i]: 
                graph[i].remove(n1_to_cut)
            else:
                graph[i] = [n1_to_cut if node==n2_to_cut else node for node in graph[i]]
        graph.pop(n2_to_cut)
        # Continue as long as there are only two nodes left
        kargerMinCut(graph)

def countingCuts(graph:dict)->dict:
    '''
        Count the numbers of mincuts in a graph.
        Do n trials and returns the best result with a minimum of cuts.
    '''
    results = []
    n = len(graph)
    for x in range(n):
        temp_graph = graph.copy()
        results.append(len(kargerMinCut(temp_graph)[0]))
    return min(results)

