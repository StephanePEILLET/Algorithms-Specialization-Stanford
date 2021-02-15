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


def median_maintenance(numbers:list)->int:
    '''
        Compute median of an streaming input list and return the sum modulo 10000.
    '''
    import heapq
    import math
    
    medians, h_low, h_high = [], [], []

    for i, n in enumerate(numbers):
        try:
            h_low_max = -heapq.nsmallest(1, h_low)[0]
        except IndexError:
            h_low_max = float('-inf')

        try:
            h_high_min = heapq.nsmallest(1, h_high)[0]
        except IndexError:
            h_high_min = float('inf')

        if n < h_low_max:
            heapq.heappush(h_low, -n)
        elif n > h_high_min:
            heapq.heappush(h_high, n)
        else:
            heapq.heappush(h_low, -n)

        if len(h_high) - len(h_low) > 1:
            h_low_min = heapq.heappop(h_high)
            heapq.heappush(h_low, -h_low_min)
        elif len(h_low) - len(h_high) > 1:
            h_low_max = -heapq.heappop(h_low)
            heapq.heappush(h_high, h_low_max)

        # Position of the median
        k = math.floor(i / 2)

        if k > len(h_low) - 1:
            median = heapq.heappop(h_high)
            heapq.heappush(h_high, median)
        else:
            median = -heapq.heappop(h_low)
            heapq.heappush(h_low, -median)

        medians.append(median)

    return sum(medians) % 10000
