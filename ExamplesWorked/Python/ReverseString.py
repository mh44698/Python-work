#Complete the solution so that it reverses the string value passed into it.

string = "world"
def solution(string):
    answer = ""
    #for i in range(len(string)): ## normal loop
    for i in reversed(string):
        answer += i
    print(answer)


solution(string)