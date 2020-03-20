####  Course work #####

##################################  Variables #######################
# Assignment 2.2
# 2.2 Write a program that uses input to prompt a user for their name and then welcomes them. Note that input will pop up a dialog box. Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.

# name = input("Enter your name")
# print("Hello", name)

# Assignment 2.3
# 2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

# hrs = float(input("Enter Hours:"))
# rate = float(input("Enter Rate:"))
# pay = hrs * rate
# print("Pay:", pay)


##########  First Program #####

# # Get the name of the file and open it
# name = input("Enter file: ")
# handle = open(name, 'r')

# # Count word frequency
# counts = dict()
# for line in handle:
#     words = line.split()
#     for words in words:
#         counts[word] = counts.get(word,0) + 1

# # Find the most common word
# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# # All done
# print(bigword, bigcount)

######### End First Program

######## Conditional execution ###########

###  Assignment 3.1 ##########
# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input("Enter Rate:")
# rate = float(rate)
# o=0
# if h > 40 :
#     o = h-40
# rpay = (h-o) * rate
# opay = o * (rate * 1.5)
# print(opay + rpay)

# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

# score = input("Enter Score: ")
# score = float(score)
# if score >=.9 :
#     grade = "A"
# elif score >= 0.8:
#     grade = "B"
# elif score >= 0.7:
#     grade = "C"
# elif score >= 0.6:
#     grade = "D"
# elif score < 0.6:
#     grade = "F"
# print(grade)


############### Video Examples :
# x = 5 
# if x<10:
#     print('Smaller')
# if < 20:
#     print('Bigger')
# print('Finis')

# x = 0
# if x < 2:
#     print('small')
# elif x < 10:
#     print('Medium')
# else:
#     print('large')
# print('all done')
# small
# all done

###########  Try Except:
# try:
#     instr = int(string)
# except:
#     instr = -1






