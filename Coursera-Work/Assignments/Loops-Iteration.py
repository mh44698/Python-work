##################################  Loops/Iterations #######################
# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


lsf = None
ssf = None

while True:
    try:
       num = input("Enter a number: ")
    except:
        print("Invalid input")

    if num == "done" : break
    elif lsf is None:
        lsf = num
    elif num > lsf :
        lsf = num
    elif ssf is None:
        ssf = num
    elif num < ssf :
        ssf = num


print("Invalid input")
print("Maximum is", ssf)
print("Minimum is", lsf)



##########  First Function #####

# While
# n=5
# while n > 0:
#     print(n)
#     n =n-1
# print('Blastoff!')
# print(n)

# while True:
#     line = input('Enter done to Exit > ')
#     if line == 'done' :
#         break
#     print(line)
# print('Done!')

# while True:
#     line = input('> ')
#     if line[0] == '#' :
#         continue
#     if line == 'done' :
#         break
#     print(line)
# print('done!')

############  Definite loops

# for i in [5,4,3,2,1] :
#     print(i)
# print('Blast off')

# friends = ['Joesph', 'Glenn', 'Sally']
# for friend in friends:
#     print('Happy New year:', friend)
# print("Done!")

# Finding largetst Value

# largest_so_far = -1
# print('Before', largest_so_far)
# for the_num in [9,41,12,3,74,15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
# print('After', largest_so_far)

# finding the smallest value

# smallest = None
# print('before')
# for value in [9,41,12,3,74,15]:
#     if smallest is None:
#         smallest = value
#     elif value < smallest:
#         smallest = value
#     print(smallest, value)
# print('After', smallest)



























