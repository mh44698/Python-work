def breakingRecords(scores):
    i = 0
    maxcount = 0
    mincount = 0
    min = scores[0]
    max = scores[0]
    while i < len(scores):
        if scores[i] > max:
            max = scores[i]
            maxcount = maxcount + 1
        elif scores[i] < min:
            min = scores[i]
            mincount = mincount + 1
        i = i + 1
    return(maxcount, mincount)