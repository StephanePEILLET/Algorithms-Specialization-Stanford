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

'''
With tail recursion -> storing the values into the input of 
the recursive function. Python isn't really beneficial. However,
tail recursions are often more easier to debug than traditional 
recursions, so we did gain a bit by making it tail recursive.
'''

# With tail recursion
def mSort_T(list1:list, list2:list, sortedL:list=[])->list:
    '''
        Merge two list already sorted in the right order with tail recursion.
    '''
    if len(list1)==0 or len(list2)==0:
        return sortedL + list1 if len(list2)==0 else sortedL + list2 
    elif list1[0] < list2[0]:
        return mSort_T(list1[1:], list2, sortedL+[list1[0]])
    else:
        return mSort_T(list1, list2[1:], sortedL+[list2[0]])
    
    
def mergeSort(inputs:list, f_sort:callable=mSort_T)->list:
    '''
        MergeSort algorithm on an input list.
    '''
    n = len(inputs)
    if n == 1:
        return inputs
    else:
        left = mergeSort(inputs[:n//2])
        right = mergeSort(inputs[n//2:])
        return f_sort(left, right)