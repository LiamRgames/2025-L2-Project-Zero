
def int_checker(question, int_type, exit_code=None):
    if int_type == "integer":
        convert = int
        error = "Please enter an integer greater than 0"
    else:
        error = "Please enter an integer greater than 0"
        convert = float



    while True:
        response = input(question).lower()
        if response == exit_code:
            return response


        try:
            response = convert(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

while True:
    test_int = int_checker("Enter a number greater than 0:\n", "integer", "xxx")
    print(f"You entered {test_int}")
    test_float = int_checker("Enter a number greater than 0:\n", "float")
    print(f"You entered {test_float}")