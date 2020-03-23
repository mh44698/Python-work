# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

# text = "X-DSPAM-Confidence:    0.8475";
# apple = str.find(text,'.')-2
# apple = text[apple:29]
# apple = float(apple)
# print(apple)


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

# ##############  Slicing
s = "Monty Python"
# #up to but not including
# print(s[0:4])
# prints start up to the 4th place
# print(s[6:7])
# prints place 6
# print(s[:2])
# prints start up to not including 2
# print(s[8:])
# prints 8 to the end
# print(s[:])

###############  Additional references#################
# prints entire string
# print(s[:6] + s[6:])
# prints entire string using concatenation
# print(s[4:8:2])
# prints 4-7 and skips ever 2nd character
# print(s[::-1])
# Reverses String

##  string to variables
# tim = '16:30:10'
# hrs, mins, secs = tim.split(':')
# print(hrs, mins, secs)

## string Replace
# Remove Spaces
# s = s.replace(' ','')
# print(s)

###############  End Additional references#################



# fruit = 'banana'
# print("n" in fruit)
# print("m" in fruit)
# print("nan" in fruit)

# if "a" in fruit:
#     print('Found it')

# word = 'banana'
# # String Comparison
# if word == 'banana':
#     print('All right, bananas.')
# if word <'banana':
#     print('Your word, ' + word + ', comes before banana')
# elif word>'banana':
#     print('Your word, ' + word + ', comes after banana')
# else:
#     print('All right, bananas.')

# # Object Methods
# greet = 'Hellow Bob'
# zap = greet.lower()
# print(zap)


# # find
# print("position of letter ",greet.find("l"))
# #.upper
# #.lower

## Search & Replace
# greet = 'Hello Bob'
# nstr = greet.replace('Bob', 'Jane')
# print(nstr)

# nstr = greet.replace('o', 'X')
# print(nstr)

# # Stripping whitespace
# greet = '    Hello Bob '
# print((greet.lstrip()))
# print((greet.rstrip()))
# print((greet.strip()))

# ###  Starts with Prefix

# line = 'Please have a nice day'
# print(line.startswith('Please'))
# print(line.startswith('P'))
# print(line.startswith('p'))























