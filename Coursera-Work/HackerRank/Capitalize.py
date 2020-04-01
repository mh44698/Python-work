## Gives 
s = "mark holmes"
def solve(s):
    s = s.split()
    first = s[0]
    last = s[1]
    first = first.capitalize()
    last = last.capitalize()
    name = first+" "+last
    print(name)
    return (name)

solve(s)

# ❯ python Capitalize.py 
# Mark Holmes