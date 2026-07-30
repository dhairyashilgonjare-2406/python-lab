from collections import Counter
text = input("Enter A String: ")
frequencies = Counter(text)
print(dict(frequencies))