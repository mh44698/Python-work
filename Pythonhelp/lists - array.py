#Create List
thislist = ["apple", "banana", "cherry"]
print(thislist)
# -- or --
thislist = list(("apple", "banana", "cherry"))
print(thislist)
#Access List
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Replace an item in the string
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#Check to see if item is in a list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#Get Length of list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#Add Item at end of list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Add Item at specified Index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#Remove a specific Item
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#Remove Last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#Remove Specific index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#Empty a list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

##########################  More advanced ##############
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list








