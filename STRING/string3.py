s = input("enter a string: ")
rev = ''.join(reversed(s))
print("revers of string: ", rev)
if s == rev:
    print("string is palindrome")
else:
   print("string is not palindrome")
