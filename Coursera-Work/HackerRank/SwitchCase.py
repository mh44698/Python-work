def swap_case(s):
    i = 0
    output = ""
    while i < len(s):
        if s[i].isupper():
            x = s[i].lower()
            output = output + x
        elif s[i].islower():
            x = s[i].upper()
            output = output + x
        else:
            x = s[i]
            output = output + x
        i = i +1
    print(output)
    return output
swap_case("HackerRank.com presents \"Pythonist 2\".")