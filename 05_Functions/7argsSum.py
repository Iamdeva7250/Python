# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_All(*args):
    print(args)
    for i in args:
      print(i * 2)
    return sum(args)

print(sum_All(1, 5, 2))
print(sum_All(1,2,3,4,5))
print(sum_All(1,2,3,4,8,5,7,5))