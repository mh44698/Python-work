#Replaces spaces with a character
#return line.replace(" ", "-")


#Replaces the letter in the string 
# string = string[:position] + character + string[position+1:]
# return string

# # Compare a string to a substring counts the number of repeating times
# string = 'ABCDCDC'
# sub_string = 'CDC'
# def count_substring(string, sub_string):
#     i = 0
#     y = 0
#     for i in range(0, len(string)):
#         x = string[i:len(sub_string)+i]
#         if sub_string == x:
#             y = y + 1
#     print(y)
#     # return (y)
# count_substring(string, sub_string)


####  Full blown answer
def merge_the_tools(S, N):
    # S, N = input(), int(input()) 
    for part in zip(*[iter(S)] * N):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

if __name__ == '__main__':

###  HTML PARSER
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))

############  Runner up with possible multiple first places
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     zes = max(arr)
#     i=0
#     while(i<n):
#         if zes ==max(arr):
#             arr.remove(max(arr))
#         i+=1
#     print(max(arr))

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
# marksheet=[]
# scorelist=[]
# if __name__ == '__main__':
#         for _ in range(int(input())):
#                 name = input()
#                 score = float(input())
#                 marksheet+=[[name,score]]
#                 scorelist+=[score]
#         b=sorted(list(set(scorelist)))[1] 

#         for a,c in sorted(marksheet):
#              if c==b:
#                     print(a)












