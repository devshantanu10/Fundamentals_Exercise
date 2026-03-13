def count_vowels():
    word = input("enter a word: ")
    count = 0

    for letter in word:
        if letter in "aeiou":
            count+= 1
    print("Number of vowels: " , count)

count_vowels()

            