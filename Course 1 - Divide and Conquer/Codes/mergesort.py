def split(input_list:list)->(list, list):
    '''
        Split a list in two parts
    '''
    n = len(input_list)
    return input_list[:n//2], input_list[n//2:]

def swap_sort(A:list)->list:
    '''
        Sort a list of length 2 by comparing and swapping.
    '''
    output = [0,0]
    if A[0] < A[1]:
        output = [A[0],A[1]]
    else:
        output = [A[1],A[0]]
    return output

def merge(A:list, B:list)->list:
    '''
        Merge two lists in an sorted output.
    '''
    n = len(A)+len(B)
    output = [0]* n
    i,j = 0, 0

    for k in range(n):
        if i < len(A) and j < len(B):
            if A[i] < B[j]:
                output[k] = A[i]
                i += 1
            else: # B[j] < A[i]
                output[k] = B[j]
                j += 1
        else:
            if i == len(A):
                output[k] = B[j]
                j += 1
            else:
                output[k] = A[i]
                i += 1
    return output

def merge_sort(input_list:list)->list:
    '''
        Function to sort a list with merge sort paradigme with o(n * log(n) complexity)
    '''
    n = len(input_list)
    first_half, second_half = split(input_list)
    if n % 2 == 0:
        if n//2 == 2:
            first_half, second_half = swap_sort(first_half), swap_sort(second_half)
        else:
            first_half, second_half = merge_sort(first_half), merge_sort(second_half)
    else:
        # first_half is even and second_half is odd
        if len(first_half) == 1:
            second_half = swap_sort(second_half)
        elif len(first_half) == 2:
            first_half = swap_sort(first_half)
            second_half = merge_sort(second_half)
        else:
            first_half, second_half = merge_sort(first_half), merge_sort(second_half)

    output = merge(first_half, second_half)
    return output
