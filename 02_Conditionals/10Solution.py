# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).


species = input("Enter your pet's species (Dog/Cat): ").strip().lower()
age = int(input("Enter your pet's age (in years): "))

if species == "dog":
    if age < 2:
        food = "Puppy food"
    elif age <= 7:
        food = "Adult dog food"
    else:
        food = "Senior dog food"

elif species == "cat":
    if age < 2:
        food = "Kitten food"
    elif age <= 5:
        food = "Adult cat food"
    else:
        food = "Senior cat food"

else:
    food = "Unknown species, please enter Dog or Cat"

print(f"Recommended food: {food}")
