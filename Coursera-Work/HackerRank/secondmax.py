if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    zes = max(arr)
    i=0
    while(i<n):
        if zes ==max(arr):
            arr.remove(max(arr))
        i+=1
    print(max(arr))

# ❯ python secondmax.py 
# 5
# 2 3 6 6 5
# 5