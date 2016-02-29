# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically
valid = True
words = []
while valid:
    wordIn = input("Enter a word! ")
    if wordIn == "quit":
        break
    else:
        words.append(wordIn)
words = sorted(words)
for i in words:
    print(i)
