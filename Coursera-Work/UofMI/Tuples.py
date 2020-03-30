# #10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# # You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# #From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# #Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# key_value ={}
# #fh = input("Enter:")
# #if len(fname) <= 1 :
# fname = "mbox-short.txt"
# fh = open(fname)
# di = dict()
# for line in fh:
#     c = line.split()
#     if "From " in line:
#         a = line.rstrip()
#         c = line.split(':')
#         line = line[len(line)-14:-12]
#         di[line] = di.get(line,0) + 1
#         sorted(di.keys())
# for key in sorted(di.keys()):
#     print(key, di[key])

#################Tuples ##################

# (x,y) = (4,'fred')
# print(x)
# print(y)

# print( (0,1,2) < (5,1,2) )  # True
# print( (0,1,200000) < (0,3,4) ) # True
# print( ('Jones,', 'Sally' ) < ('Jones', 'Sam')) # False
# print( ('Jones,', 'Sally' ) > ('Adams', 'Sam')) # True


# ###  Sorted Tuples/Dictionaries
# d = {'a':10,'b':1,'c':22}
# print(d.items())
# dict_items = ([('a',10), ('c',22), ('b',1)])
# print(sorted(d.items()))

# ####  Loop in Key Order
# for k, v in sorted(d.items()):
#     print(k,v)

# #### Loop in Value Order
# tmp = list()
# for k, v in d.items():
#     tmp.append( (v,k) )
# print("tmp:",tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)

# # 10 Most Common words

# fhand = "String of String the String by String not including string"
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# lst = list ()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse = True)

# for val, key in lst[:10]:
#     print(key, val)

# ##  Shorter Version Converts Dictionary to and sorts it to tuples - reverses and takes the top 2 
# c = {'a':10, 'b':1, 'c':22}
# print( (sorted( [ (v,k) for k,v in c.items()])[::-1])[:2])


