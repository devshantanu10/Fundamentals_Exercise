# num = int(input("Enter a number"))

# def check(num):
#     if num%2 == 0:
#         print(num , "Is the even number")

#     else:
#         print(num , "Is the odd number")

# check(num)


# def check(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# num = int(input("Enter a number: "))
# result = check(num)

# print(num, "is", result)


def check(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))


print(num1, "is" , check(num1))
print(num2, "is" , check(num2))





