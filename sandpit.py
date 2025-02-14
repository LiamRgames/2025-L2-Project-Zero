#Multiplication
number = 10
print(f"Multiplication: {number*3}")

#Exponential
number = 5
print(f"Exponential: {number**3}")

#String Duplication
num_string = "5"
print(f"String Duplication: {num_string*5}")

#String Length
text = "Hello my name is Groot"
text_length = len(text)
print(f"{text} is {text_length} characters long")


#Extracting Strings And Letters
languages = ["python", "mysql", "php", "html", "css", "javascript", "assembly"]

for i in languages:
    print(f"Is {i} the best programming language? ")
    print(f"It starts with the letter {i[0]}")
    print(f"The first 2 letters are {i[:2]}")
