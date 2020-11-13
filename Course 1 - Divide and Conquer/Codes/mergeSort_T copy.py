#!/usr/bin/python
import sys

if sys.getrecursionlimit() < 30000:
    sys.setrecursionlimit(30000)

def mSort_T(list1:lst, list2:list, sortedL:list=[])->list:
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

if __name__ == "__main__":
    filepath = '/Users/stephanepeillet/Downloads/data.txt'
    with open(filepath) as fp:
        try:
            data = [line.strip() for line in fp]
        finally:
            fp.close()

    print(mergeSort_T(data))
