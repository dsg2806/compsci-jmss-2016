inp = input("Type a number here: ")

floatie = str(inp)
notNum = True

while notNum:
    try:
        inp = float(inp)
        notNum = False
    except ValueError:
        print("'" + floatie + "'" + " isn't a number you uncultured swine!")
        inp = input("Type a number here: ")


try:
    print(inp/0)
except ZeroDivisionError:
    print("Divided by zero!")
