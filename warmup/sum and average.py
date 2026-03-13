numbers = []

for i in range(5):
    n = int(input("Enter a number: "))
    numbers.append(n)


    total = sum(numbers)
    average = total/len(numbers)

    print("sum:" , total)
    print("Average:" , average)