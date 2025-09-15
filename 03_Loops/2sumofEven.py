# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter a number : "))
sum_of_evens = 0

for i in range(1, n + 1):
    if i % 2 == 0:
          sum_of_evens += i

print("Sum of even numbers up to", n, "is:", sum_of_evens)  