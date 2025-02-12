#Statement Decorator Multi Line and Flexible

def statement_decorator(message, decoration, lines):
    if lines1 == 1:
        print(f"{decoration1*3} {message1} {decoration1*3}")
    elif lines1 == 2:
        print(f"{decoration1 * 3} {message1} {decoration1 * 3}")
        for char in range(0, len(message1) + 8):
            print(decoration1, end="")
        print()
    else:
        for char in range(0, len(message1) + 8):
            print(decoration1, end="")
        print(f"\n{decoration1*3} {message1} {decoration1*3}")
        for char in range(0, len(message1) + 8):
            print(decoration1, end="")
        print()

#Main Loop
while True:
    message1 = str(input("Enter a message to see it decorated:\n"))
    decoration1 = input("Enter the decoration you want to be added(1 character or emoji only):\n")
    try:
        lines1 = int(input("Enter the number of lines:\n"))
        if message1 != '' and decoration1 != '' and lines1 != '' and lines1 in range(1, 4):
            statement_decorator(message1, decoration1, lines1)
        else:
            print("A value was not accepted, please try again")
    except ValueError:
        print("That value of lines is invalid, try again")
        lines1 = ''
