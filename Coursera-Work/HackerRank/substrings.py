def count_substring(string, sub_string):
    # print (string)
    # print (sub_string)
    i = 0
    y = 0
    for i in range(0, len(string)):
        x = string[i:len(sub_string)+i]
        if sub_string == x:
            y = y + 1
    print(y)
    return (y)

count_substring("ABCDCDC","CDC")