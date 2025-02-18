
def not_blank(question):
    numbers_in_response = 0
    while True:
        response = input(question)
        if response != '':
            for char in response:
                if char.isdigit():
                    numbers_in_response += 1
            if numbers_in_response == 0:
                return response
            else:
                print("There was a number in your response. Please try again")
                numbers_in_response = 0
        else:
            print("That value is invalid")

def int_checker(question):
    error = "Please enter a valid age"
    while True:
        response = input(question).lower()

        try:
            response = int(response)
            if response == int(response):
                return response
            else:
                print(error)

        except ValueError:
            print(error)

while True:
    user_name = not_blank("Name: ")
    user_age = int_checker("Age: ")
    if user_age > 70:
        print(f"{user_name} is too old for this")
        continue
    elif user_age < 5:
        print(f"{user_name} is too young for this")
        continue
    else:
        print(f"{user_name} has successfully purchased a ticket")
