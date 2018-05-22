str1 = input("Enter any string:")
str2 = '' # initializing empty string
for i in range(len(str1)):
    str2 += str1[len(str1)-1-i] # storing reversed string
# checking condition for palindrome string
if str1 == str2:
    print("Palindrome")
else:
    print("not palindrome")
