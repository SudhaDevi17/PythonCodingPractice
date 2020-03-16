#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        i = i+1
        symbol = "#"
        nullSymbol = " "
        if(i<= n):
            j = n - i
            print("{0}{1}".format(nullSymbol*j, symbol * i) )

if __name__ == '__main__':
    n = int(input())

    staircase(n)
