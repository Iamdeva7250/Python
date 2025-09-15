# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

input_num = int(input("Enter a number to compute its Factorial : "))

factorial = 1

while input_num > 0:
    factorial *= input_num
    input_num -= 1

print("Factorial is:", factorial) 