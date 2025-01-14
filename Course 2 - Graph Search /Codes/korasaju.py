#!/usr/bin/python
import os, sys, threading
from DFS import *

def sorted_dict(input_dict:dict)->dict:
    '''
        Sorted a dict by key values
    '''
    output_dict = {}
    for key in sorted(input_dict):
        output_dict[key] = input_dict[key]
    return output_dict


def get_reverse_graph(graph:dict)->dict:
    '''
        Return a graph with reversed links
    '''
    graph_reverse = {}
    for key in graph.keys():
        for value in graph[key]:
            if value == []:
                graph_reverse[key]=[]
            else:
                if value in graph_reverse.keys():
                    graph_reverse[value].append(key)
                else:
                    graph_reverse[value] = [key]
    return sorted_dict(graph_reverse)


def get_finishing_time_graph(graph:dict, finishing_time:dict)->dict:
    '''
        Return a new graph by replacing graph's node by their finishing time.
    '''
    ft_graph = {}
    for key in graph.keys():
        values = []
        for value in graph[key]:
            values.append(finishing_time[value])
        ft_graph[finishing_time[key]] = values
    return sorted_dict(ft_graph)


def korasaju(G:dict, Grev:dict=None, use_stack:bool=False,verbose:bool=False)->Params:
    '''
        Return SCCs of a graph with Korasaju's two passes algorithm.
    '''
    if Grev is None:
        Grev = get_reverse_graph(G)
        
    Grev_params = DFS_loop(Grev, use_stack=use_stack) # Run DFS_loop on reverse graph to compute the "magical ordering" of nodes
    G_finishing_time = get_finishing_time_graph(G, Grev_params.finishing_time)
    Gft_params = DFS_loop(G_finishing_time, use_stack=use_stack)
    Gft_params.leaders = set(Gft_params.leader.values())
    
    if verbose:
        print('---------Graphs---------') 
        print('Input  :                        ', G)
        print('Step 1 - Reverse graph :        ', Grev)
        print('Step 2 - Compute finishing time:', sorted_dict(Grev_params.finishing_time))
        print('Step 3 - Find the leaders :     ', G_finishing_time)
        print('---------Results--------')
        print('Leader for each node:           ', Gft_params.leader)
        print('Leaders of SCCs in the graphs:  ', Gft_params.leaders)
        print('SCCs (grouped by leader):       ', Gft_params.SCCs)
        
        return Gft_params
    
    else:
        return Gft_params


def load_data(filepath:str)->(dict, dict):
    '''
        Create graph and his reverse as dict from the input file
    '''
    file = open(filepath,"r")
    data = file.readlines()
    
    # Determine all nodes present in the graph
    nodes = set()
    for line in data:
        res = list(map(lambda x: int(x),line.split()))
        nodes.update(res)
    
    # Init all the nodes in the graph
    graph, graph_rev = {node:[] for node in nodes}, {node:[] for node in nodes}
    
    for line in data:
        node_start, node_target = list(map(lambda x: int(x),line.split())) 
        # Graph 
        if node_start not in graph.keys():
            graph[node_start] = [node_target]
        else:
            graph[node_start].append(node_target)
        # Reverese graph
        if node_target not in graph_rev.keys():
            graph_rev[node_target] = [node_start]
        else:
            graph_rev[node_target].append(node_start)
            
    return graph, graph_rev


def main(argv):
    filepath = str(argv)
    graph, graph_rev = load_data(filepath)
    
    # For large input file, I prefer to use stack method in order to avoid problems with depth of recursion.
    SCCs = korasaju(graph, graph_rev, use_stack=True).SCCs
    print(sorted(list(map(lambda x: len(x), list(SCCs.values()))), reverse=True)[:5])

    
if __name__ == '__main__':
    main(sys.argv[1])