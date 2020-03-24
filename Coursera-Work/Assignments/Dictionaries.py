# #9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# # The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# # The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# # After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# stuff = list()
# #fh = input("Enter:")
# #if len(fname) <= 1 :
# fname = "mbox-short.txt"
# fh = open(fname)
# di = dict()
# for line in fh:
#     c = line.split()
#     #print(c[1])
#     if line.startswith("From:"):
#         line = line[6:]
#         a = line.rstrip()
#         di[a] = di.get(a,0) + 1
#         #print(a)
# #print(di)
# largest = -1
# theword = None
# for k,v in di.items():
#    # print(k,v)
#     if v > largest :
#         largest = v
#         theword = k
# print(theword, largest)



################ Dictionaries 9.1
# # A bag of values with lables.  Key value Pair.
# # Associative Arrays

# purse = dict()
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75
# print(purse)
# print(purse['candy'])
# purse['candy'] = purse['candy'] + 2
# print(purse)

# # ---  OR ------
# jjj = {'chuck' : 1, 'fred' :42, 'jan':100}
# print(jjj)

############  Part 2 #########

### Histogram Problem ### Or Count

# ccc = dict()
# # print(ccc['csev'])
# print('csev' in ccc)  # - False as it is empty

# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else: 
#         counts[name] = counts[name] + 1
# print(counts)

# x = counts.get('zqian')
# print(x)

########################### Part 3 

# counts = dict ()
# # print("Enter a line of Text: ")
# # line = input('')
# line = "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car"
# words = line.split()
# print('Words:', words)
# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word,0) +1
# print('Counts', counts)

# ##### how to find the Max value
# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print("This is the Max of Counts:", bigword, bigcount)

# #### output of Dictionary:
# print(counts.keys())
# print(counts.values())
# print(counts.items())











