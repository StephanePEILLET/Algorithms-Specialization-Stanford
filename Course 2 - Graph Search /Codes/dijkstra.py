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
        Compute dijkstra's score to each node in order to find the shortest path.
    '''
    A, B = {node:1000000 for node in graph}, {start_vertex: [start_vertex]}
    V, X = list(graph.keys()), [start_vertex]
    A[start_vertex] = 0
    
    while set(V) - set(X):
        # List all the nodes of X connected to V - X
        E = {}
        for node_v in X: 
            for node_w in graph[node_v]:
                if node_w not in X:
                    E[(node_v,node_w)] = graph[node_v][node_w] + A[node_v]

        # Looking for min edge in the connected nodes
        min_edge = min(E, key=E.get)
        node_v, node_w = min_edge
        
        # Updating A and B with new score and path 
        X.append(node_w)
        A[node_w] = graph[node_v][node_w] + A[node_v]
        B[node_w] = B[node_v] + [node_w] 
        
    return A, B


def dijkstra_shortest_path(graph:dict, node_source:int, node_target:int)->(int,list):
    '''
        Find shortest path in a graph betweens two nodes thanks to Dijkstra's algorithms.
    '''
    A, B = dijkstra_straightforward(graph, node_source)
    if type(node_target) is list:
        return [A[node] for node in node_target]
    else:
        return A[node_targe], B[node_target]