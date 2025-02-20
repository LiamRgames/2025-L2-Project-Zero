response = ''
loop = True
def int_checker(question, int_type, exit_code):
    global loop
    global response
    if int_type == "integer":
        convert = int
        error = "Please enter an integer greater than 0"
    else:
        error = "Please enter an integer greater than 0"
        convert = float



    while True:
        response = input(question).lower()
        if response == exit_code:
            loop = False
            print("Exiting...")
            return ''



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
    if test_int != '':
        print(f"You entered {test_int}")
    test_float = int_checker("Enter a float greater than 0:\n", "float", "xxx")
    if test_float != '':
        print(f"You entered {test_float}")
