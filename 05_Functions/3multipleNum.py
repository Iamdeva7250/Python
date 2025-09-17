# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.


def multiply(a, b):
     return a * b
  
a = int(input("Enter the first Number for multiplication : "))
b = int(input("Enter the Second Number for multiplication: "))

result = multiply(a, b)


print(f"the multiplication is {result}")
# print(multiply('a' * 5))
