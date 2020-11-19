def merge_and_count(A:list, B:list, verbose:bool=False)->(list, int):
    '''
        Merge two lists in an sorted output and count the number of inversions between the splits of a list.
    '''
    n = len(A)+len(B)
    count = 0
    if verbose: 
        pairs = []
    output = [0]* n
    i,j = 0, 0
    
    for k in range(n):
        if i < len(A) and j < len(B): 
            if A[i] < B[j]:
                output[k] = A[i]
                i += 1
            else: # B[j] < A[i]
                output[k] = B[j]
                count += len(A) - i 
                if verbose: 
                    for x in range(len(A) - i):
                        pairs.append((B[j], A[i + x]))
                j += 1
        else:
            if i == len(A):
                output[k] = B[j]
                j += 1
            else:
                output[k] = A[i]
                i += 1
    if verbose: 
        print(f'Number of inversions : {count}')
        print('Inversion pairs: ', pairs)
    
    return output, count

def sort_and_count(inputs:list)->int:
    '''
        Count the number of inversions in a list. 
    '''
    n = len(inputs)
    if n == 1:
        return inputs, 0    
    else:
        left, X = sort_and_count(inputs[:n//2]) 
        rigth, Y = sort_and_count(inputs[n//2:]) 
        result, Z = merge_and_count(left, rigth)    
    return result, X+Y+Z