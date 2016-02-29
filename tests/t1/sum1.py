# write a program that reads in 10 numbers, then prints the sum of those
total = 0
for i in range(0,10):
    inputN = input("Type in a number here! ")
    inputN = int(inputN)
    total += inputN
print(total)