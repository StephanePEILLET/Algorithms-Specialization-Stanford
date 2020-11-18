# Optimized mergesort 

def mSort(list1:list, list2:list)->list:
    if len(list1)==0 or len(list2)==0:
        return list1 if len(list2)==0 else list2 
    elif list1[0] < list2[0]:
        return [list1[0]] + mSort(list1[1:], list2)
    else:
        return [list2[0]] + mSort(list1, list2[1:])
    
def mergeSort(inputs:list)->list:
    n = len(inputs)
    if n <= 1:
        return inputs
    else:
        return mSort(inputs[:n//2], inputs[n//2:])
'''
With tail recursion -> storing the values into the input of 
the recursive function. Python isn't really beneficial. However,
tail recursions are often more easier to debug than traditional 
recursions, so we did gain a bit by making it tail recursive.
'''

# With tail recursion
def mSort_T(list1:list, list2:list, sortedL:list=[])->list:
    if len(list1)==0 or len(list2)==0:
        return sortedL + list1 if len(list2)==0 else sortedL + list2 
    elif list1[0] < list2[0]:
        return mSort_T(list1[1:], list2, sortedL+[list1[0]])
    else:
        return mSort_T(list1, list2[1:], sortedL+[list2[0]])
    
def mergeSort_T(inputs:list)->list:
    n = len(inputs)
    if n <= 1:
        return inputs
    else:
        return mSort_T(inputs[:n//2], inputs[n//2:]) 
