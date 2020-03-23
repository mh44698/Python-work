import math
import os
import random
import re
import sys

n = int(input().strip())

def random_number(n):
    if n >= 6 and n <= 20:
        print("Weird")
    elif n >= 20 and n % 2 == 0:
        print("Not Weird")
    elif n % 2 != 0:
        print("Weird")
    elif n > 100:
        print("Weird")
    else:
        print("Not Weird")

random_number(n)
