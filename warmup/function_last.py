def analyze(numbers):
    total = 0
    largest  = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        total += num

        if num > largest:
            largest = num

        if num < smallest:
            smallest = num 

    return total , largest, smallest

nums = []

for i in range(5):
    n = int(input("Enter a number: "))
    nums.append(n)


total , largest , smallest = analyze(nums)


print("Sum:" , total)
print("Largest: " , largest)
print("Smallest: " , smallest)