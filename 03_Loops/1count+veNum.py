# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
postive_count = 0

for num in numbers:
    if num > 0:
        postive_count += 1
        print(num)

print("Total positive numbers:", postive_count)
 