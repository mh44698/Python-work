a = [5,6,7]
b = [3,6,10]
def compareTriplets(a, b):
    c = 0
    d = 0
    i=0
    while i < len(a):
        if a[i] > b[i]:
            c = c + 1
        elif a[i] < b[i]:
            d = d + 1
        i = i + 1
    print(c,d)

compareTriplets(a, b)