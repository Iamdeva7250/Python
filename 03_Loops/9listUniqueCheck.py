# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]

items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for i in items:
    if i in unique_items:
        print(f"Duplicate found: {i}")
        break
    unique_items.add(i)
else:
    print("All items are unique.")    
    
    