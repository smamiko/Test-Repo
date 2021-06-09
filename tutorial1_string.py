message = """Hello World."""

new_message = message.replace("World", "Universe")

print("What is in the variable? :", message)
print("How many characters? :", len(message))
print(
    "A trial of slicing :", message[:10]
)  # [x:y] ; x is the index number you want to start, y is the index after you want to finish.
print("all in lowercase :", message.lower())  # print the object with all lower case.
print("all in uppercase :", message.upper())
print(
    "Number of string 'l' :", message.count("l")
)  # print the number of string in the argument.
print(
    "A trial of finding a string :", message.find("with")
)  # print the starting index of the word in the argument. U/L matters.
print("Replaced word :", new_message)

greeting = "Hello"
name = "Rafal"

greet = greeting + ", " + name + ". Welcome!"
greet2 = "{}, {}. Welcome!".format(greeting, name)
greet3 = f"{greeting}, {name.upper()}. Welcome!"


print("Using pluses :", greet)
print("Using format :", greet2)
print("Using f-string :", greet3)

# print(dir(name))
# print(help(str.lower))
