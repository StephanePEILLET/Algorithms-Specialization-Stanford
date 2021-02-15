#!/usr/bin/python
import os

def load_data(filepath)->list:
    '''
        Load data for Mediane Maintenance exercice.
    '''
    file = open(filepath, 'r')
    result = []
    for line in file.readlines():
        result.append(int(line.split()[0]))
    return result


def median_maintenance(data:list)->int:
    '''
        Compute median of an streaming input list and return the sum modulo 10000.
    '''
def median_maintenance(data:list)->int:
    '''
        Compute median of an streaming input list and return the sum modulo 10000.
    '''
    import heapq, math
    
    medians, h_low, h_high = [], [], []

    for index, el in enumerate(data):
        half_index = math.floor(index/2)
        
        h_low_max = -heapq.nsmallest(1, h_low)[0] if h_low else float('-inf')
        h_high_min = heapq.nsmallest(1, h_high)[0] if h_high else float('inf')

        if el < h_low_max:
            heapq.heappush(h_low, -el)
        elif el > h_high_min:
            heapq.heappush(h_high, el)
        else:
            heapq.heappush(h_low, -el)

        if len(h_high)-1 > len(h_low):
            h_low_min = heapq.heappop(h_high)
            heapq.heappush(h_low, -h_low_min)
        elif len(h_low)-1 > len(h_high):
            h_low_max = -heapq.heappop(h_low)
            heapq.heappush(h_high, h_low_max)

        if half_index > len(h_low)-1:
            median = heapq.heappop(h_high)
            heapq.heappush(h_high, median)
        else:
            median = -heapq.heappop(h_low)
            heapq.heappush(h_low, -median)

        medians.append(median)

    return sum(medians)%10000