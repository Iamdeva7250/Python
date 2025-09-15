# 4. Reverse a String
# Problem: Reverse a string using a loop.

input_str = input("Enter a String : ")
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str
    
print("Reversed string:", reversed_str)

