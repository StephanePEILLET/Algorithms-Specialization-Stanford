#!/usr/bin/python
import os, sys


def load_data(filepath:str)->dict:
    '''
        Load graph data into a dict with the form: {node1:{linked_node1:dist1, linked_node2:dist2,...}, node2:...}
    '''
    graph = {}
    file = open(filepath, "r")
    data = file.readlines()
    for line in data:
        temp = line.split()
        node = int(temp[0])
        nodes_linked = {}
        for x in temp[1:]:
            edge, length = x.split(',')
            nodes_linked[int(edge)] =  int(length)  
        graph[node] = nodes_linked
    return graph


def dijkstra_straightforward(graph:dict, start_vertex:int)->(dict, dict):
    '''
        Compute dijkstra's score to each node in order to find the shortest path. (Implemented with no optimization)
    '''
    A, B = {node:1000000 for node in graph}, {start_vertex: [start_vertex]}
    V, X = list(graph.keys()), [start_vertex]
    A[start_vertex] = 0
    
    while set(V) - set(X): 
        E = {} # List all the nodes of X connected to V - X
        for node_v in X: 
            for node_w in graph[node_v]:
                if node_w not in X:
                    E[(node_v,node_w)] = graph[node_v][node_w] + A[node_v]
        
        if E: 
            min_edge = min(E, key=E.get) # Looking for the edge with the min djikstra score (A[v] + Lvw) in E
            node_v, node_w = min_edge

            # Updating A and B with new score and path 
            X.append(node_w)
            A[node_w] = graph[node_v][node_w] + A[node_v]
            B[node_w] = B[node_v] + [node_w] 
            
        else: # No more nodes in X are connected to V-X
            break
            
    return A, B


def dijkstra_heap(graph:dict, start_vertex:int)->(dict, dict):
    '''
        Apply dijstra's algorithms with heap data structure.
    '''
    from heapq import heappush, heappop
    A, B = {node:1000000 for node in graph}, {start_vertex: [start_vertex]}
    V, X = list(graph.keys()), [start_vertex]
    A[start_vertex] = 0

    while set(V) - set(X): 
        heap = []
        for node_v in X:
            for node_w in graph[node_v]:
                if node_w not in X:
                    heappush(heap, (graph[node_v][node_w] + A[node_v], node_v, node_w)) 
        if heap:
            score, node_v, node_w = heappop(heap)
            X.append(node_w)
            A[node_w] = score
            B[node_w] = B[node_v] + [node_w] 
        else:
            break

    return A, B


def dijkstra_shortest_path(graph:dict, node_source:int, node_target:int, heap:bool=False)->(int,list):
    '''
        Find shortest path in a graph betweens two nodes thanks to Dijkstra's algorithms.
    '''
    if heap:
        A, B = dijkstra_heap(graph, node_source)
    else: 
        A, B = dijkstra_straightforward(graph, node_source)
        
    if type(node_target) is list:
        return [A[node] for node in node_target]
    else:
        return A[node_targe], B[node_target] 