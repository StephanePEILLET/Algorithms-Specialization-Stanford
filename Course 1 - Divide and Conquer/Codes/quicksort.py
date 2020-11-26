def choose_pivot(inputs:list)->int:
    '''
        Return the indice of the randomly selected pivot in the input list.
    '''
    import random
    return random.choice(range(len(inputs)))        

def partition(inputs:list, idx_pivot:int)->(list, int):
    '''
        Partition an input list from the indices begin to end. 
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

def quicksort(inputs:list)->list:
    '''
        Sort an algorithm with the quicksort paradigm.
    '''  
    n = len(inputs)
    if n < 1:
        return inputs
    else:
        idx_pivot = choose_pivot(inputs)
        inputs, idx_pivot = partition(inputs, idx_pivot) 
        inputs[:idx_pivot] = quicksort(inputs[:idx_pivot])        
        inputs[idx_pivot+1:] = quicksort(inputs[idx_pivot+1:])
        return inputs