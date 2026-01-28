# Practice: if / elif / else conditions

age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ")

if age < 18:
    print("You get a youth discount")
elif age >= 18 and is_student == "yes":
    print("You get a student discount")
else:
    print("Regular price applies")
