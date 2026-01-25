n = int(input("Enter a number"))
print("Multiplication Table for", n)
for i in range(1,11):
    #print(n , "X" , i , "=" , n * i) #common and simple way

    print(f"{n} X {i} = {n * i}") #most common and modern
    
    