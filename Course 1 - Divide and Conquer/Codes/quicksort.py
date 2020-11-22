def choose_pivot(inputs:list)->int:
    '''
    Return the indice of the randomly selected pivot in the input list.
    '''
    import random
    return random.choice(range(len(inputs)))

def partition(inputs:list, begin:int, end:int)->list:
    '''
    Partition an input list from the indices begin to end. 
    '''
    pivot = inputs[begin]
    i = begin+1
    for j in range(begin+1, end):
        if inputs[j] < pivot:
            swap(A[j], A[i])
            i+= 1
    swap(A[l], A[i-1])
    return inputs    

def quicksort(inputs:list)->list:
    '''
    Sort an algorithm with the quicksort paradigm.
    '''                     
    n = len(inputs)
    if n == 1:
        return inputs
    else:
        idx_pivot = choose_pivot(inputs)
        partition(inputs, 0, idx_pivot) # left partition
        partition(inputs, idx_pivot, n) # right partition                   
        quicksort(inputs[0, idx_pivot-1])
        quicksort(inputs[idx_pivot+1, n])