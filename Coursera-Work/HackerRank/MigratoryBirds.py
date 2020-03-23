#!/bin/python3

import math
import os
import random
import re
import sys
import collections
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
def migratoryBirds(arr):

    # Print the list
    print(arr)
    # collections = 0
    # calculate the frequency of each item
    data = collections.Counter(arr)
    data_list = dict(data)

    # Print the items with frequency
    print(data_list)

    # Find the highest frequency
    max_value = max(list(data.values()))
    mode_val = [num for num, 
                freq in data_list.items() if freq == max_value]
    mode_val = mode_val[0]
    print(mode_val)
    return(mode_val)
migratoryBirds(arr)