# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

input_str = input("Enter a String: ")

for char in input_str:
    if input_str.count(char) == 1:
        print("Char is : ", char)
        break
else:
    print("No non-repeated character found.")
    