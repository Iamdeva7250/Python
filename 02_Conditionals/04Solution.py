#  Fruit Ripeness Checker
#  Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"

color = input("Enter the color of the fruit (Green, Yellow, Brown): ")


if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
    else:
        print("Invalid color for Banana")

print(f"The fruit is a {fruit} and its color is {color}.")