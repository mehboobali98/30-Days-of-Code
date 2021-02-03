#!/bin/python3

import math
import os
import random
import re
import sys

def fun(N):
    if N < 1 or N > 100:
        return
    
    if N % 2 == 1:
        print("Weird")
    else:
        if N>=2 and N<=5:
            print("Not Weird")
        elif N>=6 and N<=20:
            print("Weird")
        elif N>20:
            print("Not Weird")
        
if __name__ == '__main__':
    N = int(input())
    fun(N)
