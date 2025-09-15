x = 2 
y = 5
z = 8
print(x+y)
print(x+y+z)
print(x * y)
print(x * y * z)
print(x + y * z)
print((x + y) * z)
print(x + (y * z))

print(x + y * z - x)
print((x + y) * z - x)
print(x + (y * z) - x)


print(int(2.23)) 
print(float(2))
print(float(2.23))  


print(x ** 2) #this is for square

print(x ** 3) #this is for cube

print(x % 2)




print(repr("chai"))  # This will return the string representation of "chai"
print(str("chai"))   # This will return the string representation of "chai" as well


print(1 < 2)  # This will return True
print(4.0 != 5.0)
print(3.0 >= 2.0)
print(5.0 == 4.0)

print(x < y and y < z)
print(x < y or y < z)
print(not (x < y))


import math
print(math.sqrt(16))  # This will return the square root of 16
print(math.pi)
print(math.e)  # This will return the value of e (Euler's number)
print(math.factorial(5))
print(math.pow(2, 3))  # This will return 2 raised to the power of 3
print(math.ceil(2.3))
print(math.floor(2.7))  # This will return the largest integer less than or equal to 2.7
print(math.log(100, 10))
print(math.log(100))  # This will return the natural logarithm of 100

print(math.floor(-3.5))
print(math.floor(3.9))
print(math.ceil(-3.5))

print(math.trunc(2.8))



print(0o20)
print(0xFF)

print(oct(64))
print(hex(255))

print(bin(10))
print(int('0b1010', 2))  # Convert binary string to integer
print(int('0o10', 8)) # Convert octal string to integer
print(int('0xA', 16))  # Convert hexadecimal string to integer        



from random import random
print(random())  # This will return a random float between 0.0 and 1.0
from random import randint
print(randint(1, 10)) # This will return a random integer between 1 and 10 

l1 = [ 'lemon', 'orange', 'banana', 'apple'  ]
from random import choice
print(choice(l1))  # This will return a random element from the list l1

from random import shuffle
shuffle(l1)
print(l1)  # This will print the shuffled list

from random import sample
print(sample(l1, 2))  # This will return a list of 2 unique random elements from l1 


from decimal import Decimal
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(d1 + d2)  # This will return the sum of d1 and d2 with high precision
print(d1 * d2)  # This will return the product of d1 and d2 with high precision

print(d1 + d2 == Decimal('0.3'))  # This will return True, showing high precision arithmetic

print(d1 + d2 == 0.3)  # This will return False, showing low precision arithmetic

from fractions import Fraction
f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
print(f1 + f2)
print(f1 * f2)  # This will return the product of f1 and f2 as a fraction
print(f1 + f2 == Fraction(1, 2))  # This will return True, showing exact arithmetic with fractions
print(f1 + f2 == 0.5)  # This will return False, showing low precision arithmetic with float


setone = {1, 2, 3, 4, 5}

print(setone & {1, 3})
print(setone | {6, 7})  # Union of two sets
print(setone - {2, 4})  # Difference of two sets
print(setone ^ {1, 2, 6})  # Symmetric difference of two sets

print(bool)
print(bool(0))  # This will return False
print(bool(1))  # This will return True
