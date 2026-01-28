# Practice: inputs and type conversion

name = input("Enter your name: ")
age = input("Enter your age: ")

age_number = int(age)

print("Hello", name)
print("You are", age_number, "years old")
print("Type of age_number:", type(age_number))
