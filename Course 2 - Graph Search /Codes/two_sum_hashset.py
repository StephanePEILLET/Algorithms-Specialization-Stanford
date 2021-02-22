#!/usr/bin/python 

def load_data(filepath:str)->list:
    '''
        Load data in a list and cast every value in a integer.
    '''
    file = open(filepath, 'r')
    data = []
    for line in file.readlines():
        data.append(int(line))
    return data

def two_sum_hash(A:list)->int:
    '''
        Looking for the number of possible T = X + Y with X, Y in input list A.
    '''  
    from tqdm.notebook import tqdm
    A = sorted(A)
    H, T = dict.fromkeys(A), {}
    for t in tqdm(range(-10000, 10000 + 1)):
        for x in H:
            if t-x in H and t not in T:
                T[t]= (x, t-x)
    return len(T)