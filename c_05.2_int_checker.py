response = ''
LOW = 5
HIGH = 100
loop = True
skip_main = False
def int_checker(question, int_type, exit_code):
    global loop
    global response
    global skip_main

    while True:
        response = input(question).lower()
        if response == exit_code:
            loop = False
            print("Exiting...")
            skip_main = True
            return ''
        if int_type == "integer":
            convert = int
            error = "Please enter an integer greater than 0"
        else:
            error = "Please enter an integer greater than 0"
            convert = float



        try:
            response = convert(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

while loop == True:
    test_int = int_checker("Enter a number greater than 0:\n", "integer", "xxx")
    if skip_main == False:
        if LOW > test_int:
            print(f"{test_int} is too low")
        elif HIGH < test_int:
            print(f"{test_int} is too high")
        else:
            print(f"{test_int} is a valid integer")
    else:
        loop = False

    test_float = int_checker("Enter a float greater than 0:\n", "float", "xxx")
    if skip_main == False:
        if LOW > test_float:
            print(f"{test_float} is too low")
        elif HIGH < test_float:
            print(f"{test_float} is too high")
        else:
            print(f"{test_float} is a valid float")
    else:
        loop = False