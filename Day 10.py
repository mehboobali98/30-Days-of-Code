#!/bin/python3

import math
import os
import random
import re
import sys

def convert_to_binary(n):
    binary_num = ""
    while n>=1:
        temp = n//2
        rem = n%2
        binary_num = binary_num + str(rem)
        n=temp
    return binary_num

def max_consc(bin_num):
    size = len(bin_num)
    max_count = 1
    temp_max = 1
    for i in range(size):
        if bin_num[i] != "1":
            continue
        if i != size - 1:
            if bin_num[i] == bin_num[i+1]:
                temp_max += 1
            elif bin_num[i] != bin_num[i+1]:
                if max_count < temp_max:
                    max_count = temp_max
                temp_max = 1
        else:
            if max_count < temp_max:
                max_count = temp_max
                    
    print(max_count)
                
if __name__ == '__main__':
    n = int(input())
    bin_num = convert_to_binary(n)
    max_consc(bin_num)
    
