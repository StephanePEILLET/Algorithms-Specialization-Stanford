def median_of_three(inputs:list)-> int:
    '''
        Find the 'median of three' in a list, ie the median between the first, the middle and the last elements of the list.
    '''
    points = [inputs[0], inputs[(len(inputs)-1)//2], inputs[-1]]
    points.remove(min(points))
    return inputs.index(min(points))

def choose_pivot(inputs:list, select_pivot:str='random')->int:
    '''
        Return the indice of a pivot from the input list with a selected method.
    '''
    if select_pivot == 'median_of_three':
        return median_of_three(inputs)
    elif select_pivot == 'first':
        return 0 # first element of the list
    elif select_pivot == 'last':
        return len(inputs)-1
    elif select_pivot == 'median':
        import numpy as np
        return int(np.argwhere(inputs == np.percentile(inputs, 50, interpolation='nearest'))) # use the position of the median
    else:
        import random
        return random.choice(range(len(inputs))) # choose randomly 

def partition(inputs:list, idx_pivot:int)->(list, int):
    '''
        Partition an input list with a selected pivot.
    '''
    pivot = inputs[idx_pivot]
    inputs[idx_pivot], inputs[0] = inputs[0], inputs[idx_pivot] 
    i = 1 
    for j in range(1,len(inputs)):
        if inputs[j] < pivot:
            inputs[i], inputs[j] = inputs[j], inputs[i] 
            i+= 1 
    inputs[0], inputs[i-1] = inputs[i-1], inputs[0] 
    return inputs, i-1 

def quicksort(inputs:list, select_pivot:str='random')->list:
    '''
        Sort an algorithm with the quicksort paradigm.
    '''  
    n = len(inputs)
    if n < 1:
        return inputs
    else:
        idx_pivot = choose_pivot(inputs, select_pivot)
        inputs, idx_pivot = partition(inputs, idx_pivot) 
        inputs[:idx_pivot] = quicksort(inputs[:idx_pivot], select_pivot)        
        inputs[idx_pivot+1:] = quicksort(inputs[idx_pivot+1:], select_pivot)
        return inputs
    
def quicksort_with_count(inputs:list, select_pivot:str)->(list, int):
    '''
        Sort an algorithm with the quicksort paradigm and count the number of comparison done.
    '''  
    n = len(inputs)
    count = n-1
    if n < 1:
        return inputs, 0
    else:
        idx_pivot = choose_pivot(inputs, select_pivot)
        inputs, idx_pivot = partition(inputs, idx_pivot)
        inputs[:idx_pivot], c1 = quicksort_with_count(inputs[:idx_pivot], select_pivot)
        inputs[idx_pivot+1:], c2 = quicksort_with_count(inputs[idx_pivot+1:], select_pivot)
        count += (c1+c2)
        return inputs, count