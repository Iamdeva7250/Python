#  Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = 22
day = "Wednesday"


age = int(input("Enter your age: "))

price = 12 if age >= 18 else 8
if day == "Wednesday":
    price -= 2

print(f"The ticket price is: ${price}")
