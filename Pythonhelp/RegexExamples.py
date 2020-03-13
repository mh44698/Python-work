# ################################################### Search
# import re
# line = "Cats are smarter than dogs"
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print ("No match!!")

###################################################  Search and Replace

# import re
# phone = "2004-959-559 # This is Phone Number"
# # Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# print ("Phone Num : ", num)
# # Remove anything other than digits
# num = re.sub(r'\D', "", phone)    
# print ("Phone Num : ", num)

# ###################################################  Match 
# # A Python program to demonstrate working of re.match().  
# import re  
# # Lets use a regular expression to match a date string  
# # in the form of Month name followed by day number  
# regex = r"([a-zA-Z]+) (\d+)"
# match = re.search(regex, "I was born on June 24")  
# if match != None:  
#     # We reach here when the expression "([a-zA-Z]+) (\d+)"  
#     # matches the date string.  
#     # This will print [14, 21), since it matches at index 14  
#     # and ends at 21.   
#     print("Match at index % s, % s" % (match.start(), match.end())) 
#     # We us group() method to get all the matches and  
#     # captured groups. The groups contain the matched values.  
#     # In particular:  
#     # match.group(0) always returns the fully matched string  
#     # match.group(1) match.group(2), ... return the capture  
#     # groups in order from left to right in the input string  
#     # match.group() is equivalent to match.group(0)  
#     # So this will print "June 24"  
#     print("Full match: % s" % (match.group(0))) 
#     # So this will print "June"  
#     print("Month: % s" % (match.group(1))) 
#     # So this will print "24"  
#     print("Day: % s" % (match.group(2)))
# else:  
#     print("The regex pattern does not match.") 

###################################################  Find All 
import re
re.findall(r'\w','http://www.hackerrank.com/')
print( re.findall(r'\w','http://www.hackerrank.com/') )

################################################### Two or more consecutive volews

import re
x="abcdeefghiklmnoooopqrstuuvwxyz"
k = re.findall(r'(?<=[^aeiouAEIOU ])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU ])',x)
if k:
    for i in k:
        print (i)
else:
    print( -1 )



