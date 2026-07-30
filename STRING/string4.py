ch=input("Enter a string: ")

upper = 0
lower = 0

for i in ch:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("uppercase letter",upper)
print("owercase letter",lower)