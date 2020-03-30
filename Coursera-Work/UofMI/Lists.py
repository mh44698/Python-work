# #8.4 Open the file romeo.txt and read it line by line.
# # For each line, split the line into a list of words using the split() method.
# # The program should build a list of words.
# # For each word on each line check to see if the word is already in the list and if not append it to the list.
# # When the program completes, sort and print the resulting words in alphabetical order.
# stuff = list()
# b=0

# fname = ("romeo.txt")
# fh = open(fname)
# #fh = fh.strip('\n')
# for line in fh:
#     y = line.rstrip()
#     y = line.split()
#     c = 0
#     for i in y:
#         b = y[c]
#         b.rstrip()
#         c = c + 1
#         if (b not in stuff):
#             stuff.append(b)
#             stuff.sort()
# print(stuff)

######################################## Assignment # 2


# #From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# #You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# #Hint: make sure not to include the lines that start with 'From:'.


# stuff = list()
# #fh = input("Enter:")
# #if len(fname) <= 1 :
# fname = "mbox-short.txt"
# fh = open(fname)
# i = 0
# for line in fh:
#     c = line.split()
#     #print(c[1])
#     if line.startswith("From:"):
#         line = line[6:]
#         a = line.rstrip()
#         print(a)
#         i = i + 1
# count = i
# print("There were", count, "lines in the file with From as the first word")


#################################  Lists ###################################
#More than one variable.
lotto = [2, 14, 26, 41, 63]

# Replace string in a list:
# print(lotto)
# lotto[2] = 28
# print(lotto)

# Find Length of list:
# print(len(lotto))

# Range allow you to print up to but not including
#print(range(len(lotto)))

# Concatenating Lists
# a = [1,2,3]
# b = [4,5,6]
# c = a + b 
# print(c)

# # Slicing Lists
# t = [9, 41, 12, 3, 74, 15]
# print(t[1:3])
# print(t[:4])
# print(t[3:])
# print(t[:])

# # Building a list from scratch - Append
# stuff = list()  #empty list
# stuff.append('book')
# stuff.append(99)
# print(stuff)
# #['book', 99]

# # Is Something in the list? - in
# some = [1, 9, 21, 10, 16]
# print(9 in some)
# print(15 in some)
# print(20 not in some)

# # Sorting - sort
# friends = ['Joesph', 'Glenn', 'Sally']
# friends.sort()
# print(friends)

####  Math Functions on list
# print("length",len(lotto))
# print("max",max(lotto))
# print("min",min(lotto))
# print("sum",sum(lotto))
# print("average",sum(lotto)/len(lotto))

################ Part 3
# Strings and Lists

# # Split on white space on characters 
# abc = 'With three words'
# stuff = abc.split()
# print(stuff)
# #find the length of the first word in the list
# print(stuff[0])
# print(len(stuff[0]))
# # Split by comma delimiter
# abc = 'A,lot,of,commas'
# stuff = abc.split(',')
# print (stuff)

# #Example loop:
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip() # strips off whitespace to the right
#     if not line.startswith('From ')  : continue
#     words = line.split()
#     print(words[2])

# # Double Split
# line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# words = line.split()
# email = words[1]
# print(email)
# # - stephen.marquard@uct.ac.za
# # find the doman
# pieces = email.split('@')
# print(pieces[1])


################## Extras ##############
# #Reverse List
# print(t[::-1])
# #Remove Last item
# print(t[:-1])

# ####################Count
# alpha = ['a','a','e','e','e','e','i','o','u']  
# y = alpha.count(alpha[0]) 
# x = alpha.count('a') ## Returns 0 if none found
# print(x,y)

# ################### #extend
# aList = [123, 'xyz', 'zara', 'abc']
# bList = [2009, 'manni']
# aList.extend(bList)
# print (aList)
# cList = aList + bList
# print (cList)

####################### index
# Syntax list_name.index(element, start, end)
 
# list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 
  
# # Will print the index of '4' in list1 
# print(list1.index(4)) 
# print(list1.index(1,9,10)) # Out of bounds and stops
  
# list2 = ['cat', 'bat', 'mat', 'cat', 'pet'] 
# # Will print the index of 'cat' in list2  
# print(list2.index('cat')) 

# # #######################insert
# # vowel list
# vowel = ['a', 'e', 'i', 'u']
# # inserting element to list at 4th position
# vowel.insert(3, 'o')
# print('Updated List: ', vowel)

# ######################pop
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']
# remove and return the 4th item
i = 2
return_value = languages.pop(i)
print('Return Value:', return_value)
# Updated List
print('Updated List:', languages)

# # ######################remove
# # animals list
# animals = ['cat', 'dog', 'rabbit', 'guinea pig', 'rabbit']
# animals.remove('rabbit')
# animals.remove('rabbit')
# #animals.remove('rabbit') ## Too Many Cause a Traceback
# print('Updated animals list: ', animals)

# ######################reverse
# # Operating System List
# os = ['Windows', 'macOS', 'Linux']
# print('Original List:', os)
# os.reverse()
# print('Updated List:', os)



