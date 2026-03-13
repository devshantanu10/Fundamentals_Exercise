# num1 = int(input("Enter number 1"))
# num2 = int(input("Enter number 2"))


# def find_largest():
#     if num1 >= num2:
#         print(num1 , "is greater")
#     else:
#         print(num2 , "is greater")

# find_largest()



# def find_largest(a, b):
#     if a >= b:
#         print(a, "is greater")
#     else:
#         print(b, "is greater")

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))

# find_largest(num1, num2)
    



def find_largest(a,b):
    if a >= b:
        return a
    else:
        return b

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))


largest = find_largest(num1 , num2)
print(largest , "Is the greater number")