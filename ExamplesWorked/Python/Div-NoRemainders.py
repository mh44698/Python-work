# Task
# Given an integral number of watermelons w (1 ≤ w ≤ 100; 1 ≤ w in Haskell), check whether Pete and Billy can divide the melons so that each of them gets an even amount.
weight = 13
def divide(weight):
    print( weight > 2 and weight % 2 == 0 )
    return weight > 2 and weight % 2 == 0
divide(weight)