# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read
total = 0
valid = True
while valid:
    inputN = input("Type in a number here! ")
    inputN = int(inputN)
    if inputN == -1:
        break
    else:
        total += inputN
print(total)