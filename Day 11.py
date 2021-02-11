#!/bin/python3

import math
import os
import random
import re
import sys

def convolve(arr, filt, row, col):
    size = len(filt[0])
    hr_sum = 0
    for i in range(size):
        for j in range(size):
            hr_sum += arr[i+row][j+col] * filt[i][j]
    return hr_sum

def max_hour_glass(arr):
    filt = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    max_sum = -math.inf
    dim_x = ((len(arr[0]) - len(filt[0]) // 1) + 1)
    dim_y = dim_x
    
    for i in range(dim_x):
        for j in range(dim_y):
            hr_sum = convolve(arr, filt, i, j)
            if hr_sum > max_sum:
                max_sum = hr_sum
    return max_sum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum = max_hour_glass(arr)
    print(max_sum)
