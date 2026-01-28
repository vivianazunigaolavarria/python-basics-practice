# Practice: dictionaries and sets

# Dictionary example (key: value pairs)
person = {
    "name": "Vivi",
    "age": 30,
    "is_student": True
}

print("Person dictionary:", person)
print("Name:", person["name"])
print("Age:", person.get("age"))

# Update a value
person["age"] = 31
print("Updated age:", person["age"])

# Loop through dictionary items
for key, value in person.items():
    print(key, "->", value)

print("\n--- Sets example ---")

# Set example (no duplicate values)
followers = {"Ana", "Luis", "Ana", "Carlos"}
print("Followers set:", followers)

# Add and remove items
followers.add("Maria")
followers.remove("Luis")

print("Updated followers:", followers)

# Check membership
print("Is Ana a follower?", "Ana" in followers)
print("Is Juan a follower?", "Juan" in followers)
