#!/bin/python3

import math
import os
import random
import re
import sys

def print_reverse(arr):
    size = len(arr)
    i = size - 1
    while(i>=0):
        print(arr[i], end=" ")
        i -= 1


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print_reverse(arr)
