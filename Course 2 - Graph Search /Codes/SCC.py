# SCC algorithm with only list and global variables
import os, sys, threading

SCC_file = '../Data/SCC.txt'
filepath = os.path.join(os.getcwd(), SCC_file)
nbr_nodes = 875715

def load_data(filepath:str, nbr_nodes:int)->list:
    '''
        Create graph/graph reverse as lists from the input file.
    '''
    file = open(filepath,"r")
    data = file.readlines()
    G, Grev = [[] for x in range(nbr_nodes)], [[] for x in range(nbr_nodes)]
    for line in data:
        node_start, node_end = list(map(lambda x: int(x),line.split())) 
        G[node_start].append(node_end); Grev[node_end].append(node_start)
    return G, Grev   

def DFSrev(Grev:list, i:int)->None:
    '''
        Apply DFS from a defined node on Grev.
        Give a finishing time to every node of the graph to compute "magical ordering" of the nodes.
    '''
    global t, is_explored, finishing_time
    is_explored[i] = True
    for j in Grev[i]:
        if not is_explored[j]:
            DFSrev(Grev, j)
    t += 1
    finishing_time[i] = t 

def DFSrev_Loop(Grev:list)->None:
    '''
        Loop DFS on every node of the graph Grev.
    '''
    global t, is_explored, finishing_time
    is_explored = [False for x in range(nbr_nodes)]
    t = 0
    for i in range(len(Grev)-1, 0, -1):
        if not is_explored[i]:
            DFSrev(Grev, i)

def DFS(G:list, i:int)->None:
    '''
        Apply DFS from a defined node on G.
        Find the SCCs in the graph and list all the leaders.
    '''
    global is_explored, scc_size
    is_explored[i] = True
    for j in G[i]:
        if is_explored[j]:
            DFS(G, j)
    scc_size += 1                      

def DFS_Loop(G:list)->None:
    '''
        Loop DFS on every node of the graph G.
    '''
    global is_explored, finishing_time, SCCs, scc_size
    is_explored = [False for x in range(nbr_nodes)]
    for i in range(len(G)-1, 0, -1):
        if not is_explored[i]:
            scc_size = 0
            DFS(G, i)  
            SCCs.append(scc_size)
            
def Korasaju(filepath:str, nbr_nodes:int)->list:
    '''
        Apply Korasaju's two passes algorithms to find the five biggest Strongly Connected Components(SCC).
    '''
    global finishing_time, SCCs
    finishing_time = [[] for x in range(nbr_nodes)]
    SCCs = []
    G, Grev = load_data(filepath, nbr_nodes)     # 1 - Let Grev = G with all arcs reversed
    DFSrev_Loop(Grev)                            # 2 - Run DFS-Loop on Grev. Give a finishing time to every node of the graph to compute "magical ordering" of the nodes.
    DFS_Loop(G)                                  # 3 - Run DFS-Loop on G. Processinig all nodes by finishing time.
    return sorted(SCCs, reverse=True)[:5]