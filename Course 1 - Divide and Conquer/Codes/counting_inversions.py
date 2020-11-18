def merge_and_count(A:list, B:list, verbose:bool=False)->(list, int):
    '''
        Merge two lists in an sorted output and count the number of inversions between the splits of a list.
    '''
    n = len(A)+len(B)
    count = 0
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

def count_split_inv(input_list:list, verbose=False)->(list, int):
    '''
        Function to sort a list with merge sort paradigme and count split inversions.
    '''
    n = len(input_list)
    first_half, second_half = split(input_list)
    if n % 2 == 0:
        if n//2 == 2:
            first_half, second_half = sorted(first_half), sorted(second_half)
        else:
            first_half, second_half = sorted(first_half), sorted(second_half)
    else:
        # first_half is even and second_half is odd
        if len(first_half) == 1:
            second_half = sorted(second_half)
        elif len(first_half) == 2:
            first_half = sorted(first_half)
            second_half = sorted(second_half)
        else:
            first_half, second_half = sorted(first_half), sorted(second_half)
    
    output, count = merge_and_count(first_half, second_half, verbose=verbose)
    return output, count

def sort_and_count(A:list)->int:
    '''
        Count the number of inversions in a list. 
    '''
    n = len(A)
    if n == 1:
        return 0    
    else:
        first_half, second_half = split(A)
        X = sort_and_count(first_half) 
        Y = sort_and_count(second_half) 
        _, Z = count_split_inv(A)    
        
    return X+Y+Z