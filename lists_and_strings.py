# Practice: lists and strings

# A list (shopping cart)
shopping_cart = ["Laptop", "Smartphone", "Headphones", "Backpack"]
print("Shopping cart:", shopping_cart)

# Indexing (positions start at 0)
first_item = shopping_cart[0]
print("First item:", first_item)

# Slicing (start is inclusive, end is exclusive)
some_items = shopping_cart[1:3]
print("Items from index 1 to 2:", some_items)

# Strings are also sequences
text = "python"
print("Original text:", text)
print("Uppercase:", text.upper())
print("Capitalized:", text.capitalize())

# Find returns the index of the first match, or -1 if not found
print("Index of 't' in 'python':", text.find("t"))
print("Index of 'z' in 'python':", text.find("z"))
