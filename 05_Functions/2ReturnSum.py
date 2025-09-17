# 2. Function with Multiple Parameters
# Problem: Create a function that takes two numbers as parameters and returns their sum.


#function of Multiple Parameters

def return_sum(num1, num2):
    return num1 + num2
  
num1 = int(input("Enter the First number : "))
num2 = int(input("Enter the Second NUmber : "))

result = return_sum(num1, num2)

print(f"The Sum is {result} of {num1} and {num2}")

  