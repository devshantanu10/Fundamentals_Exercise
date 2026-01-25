def reverse_string(s):
  return s[::-1]

user_input = input("Enter a word:")

reversed_output = reverse_string(user_input)

print("The reversed string" , reversed_output)

# from loop

def reversed_string(poudel):
   reversed_string = ""

   for char in poudel:
        reversed_string  = char + reversed_string
   return reversed_string

user_input = input("Enter a word:")
print("reversed string" , reversed_string(user_input))



#reversed words in string


def reversed_words(sentence):
   words = sentence.split()

   reversed_words = " " . join(words[:: -1 ])
   return  reversed_words


user_input = input("Enter a sentence")

print("Reversed sentence" , reversed_words(user_input))




