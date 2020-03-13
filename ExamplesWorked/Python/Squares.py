def is_square(n):    
    if n>=0:
        if int(n**.5)**2 == n:
            print("True")
            return True
    print("False")
    return False
is_square(3)



###  While loop with a find in the If statement
# def is_square(n):  
#     i = 0  
#     squares = []
#     while i < 10:
#         i = i + 1
#         square = i * i
#         squares.append(square)
#     print(squares)
#     # print (squares.contains(n))
#     if n in squares:
#     #     #return True
#         print("True")
#     else:
#     #     #return False
#         print("True")


# # return False # fix me
# is_square(23)