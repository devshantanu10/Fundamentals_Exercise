def count_vowels(s):
     vowels = "aeiouAEIOU"
     count = 0

     for char in s:
         if char in vowels:
           count += 1
     return count


user_input = input("Enter a word:")
print("Numbers of vowels" , count_vowels(user_input))
          