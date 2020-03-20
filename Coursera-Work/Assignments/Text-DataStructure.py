########  Strings

# fruit = 'banana'
# x=len(fruit)
# print(x)

# ## looping through string
# fruit = 'banana'
# index=0

# while index < len(fruit):
#     letter = fruit[index]
#     print("while loop:",index, letter)
#     index = index + 1
    
# for letter in fruit:
#     print("for loop:", letter)

## Looping and Counting
# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

##############  Slicing
s = "Monty Python"
#up to but not including
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])

fruit = 'banana'
print("n" in fruit)
print("m" in fruit)
print("nan" in fruit)

if "a" in fruit:
    print('Found it')

word = 'banana'
# String Comparison
if word == 'banana':
    print('All right, bananas.')
if word <'banana':
    print('Your word, ' + word + ', comes before banana')
elif word>'banana':
    print('Your word, ' + word + ', comes after banana')
else:
    print('All right, bananas.')

# Object Methods
greet = 'Hellow Bob'
zap = greet.lower()
print(zap)


# find
print(fruit.find("l"))















