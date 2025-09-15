chai = "Masala Cahi"
print(chai)

print(chai[0])  # This will return the first character of the string

slice_chai = chai[0:6]  # This will return the first five characters of the string
print(slice_chai)

print(chai[0:6])

num_list = "52465764316"
print(num_list[0:5])  # This will return the first five characters of the string
print(num_list[5:]) # This will return the characters from index 5 to the end of the string


print(chai.lower())  # This will return the string in lower case
print(chai.upper())  # This will return the string in upper case

chai = chai.replace("Masala", "Green")
print(chai)  # This will print the modified string with "Masala" replaced by "Green"

chai = "lemon, tea , ginger, green , mint "
print(chai.split())  # This will split the string into a list at each comma
print(chai.split(","))  # This will split the string into a list at each comma and return a list of strings


chai = "Masala Chai"
print(chai.find("Chai"))  # This will return the index of the first occurrence of "Chai" in the string

print(chai.find("chai"))

chai = " chai masla chai  msals chai chai chai "
print(chai.count("chai"))


chai_type = "Masala Chai"
quantity = 5
order = "I oredered {} cups of {} chai"
print(order.format(quantity, chai_type))  # This will format the string with the quantity and chai type 


chai_variety = ["Masala Chai", "Green Chai", "Lemon Chai", "Ginger Chai", "Mint Chai"\
  , "Black Chai", "Herbal Chai"]
print(chai_variety)
print("".join(chai_variety))
print(" ".join(chai_variety))
print(", ".join(chai_variety))
print("-".join(chai_variety))

print(len(chai))
# This will return the length of the list


chai = "he said , \",masala chai is awesome!\""
print(chai)  


chai = "Masala\nchai"
print(chai)

chai = r"Masala\nchai" 
print(chai)

chai = r"c:\user\pwd"
print(chai)  



tea_variety = ["Masala Chai", "Green Chai", "Lemon Chai", "Ginger Chai", "Mint Chai"
  , "Black Chai", "Herbal Chai",  "Oolong Tea", "Black Tea", "White Tea", "Green Tea"]

print(tea_variety)
print(tea_variety[0])
print(len(tea_variety))
print(tea_variety[0:5])  # This will return the first five elements of the list
print(tea_variety[5:])  # This will return the elements from index 5 to the end of the list

print(tea_variety[1:2]) # This will return the second element of th
tea_variety[1:2] = "lemon"
print(tea_variety)

tea_varieties = ['masla tae', 'greem tea', 'lemon tea', 'ginger tea', 'mint tea', 'black tea', 'herbal tea']
tea_varieties[1:2] = ["lemon"]
print(tea_varieties)  


tea_varieties = ['black', 'green', 'white', 'oolong', 'herbal']
for tea in tea_varieties:
    print(tea)

if "lemon" in tea_varieties:
    print("lemon tea is available.")
else:
    print("lemon tea is not available.")

tea_varieties.append("lemon tea")
print(tea_varieties)

if "lemon tea" in tea_varieties:
    print("lemon tea is available.")
else:
    print("lemon tea is not available.")


tea_varieties.pop()
print(tea_varieties)

tea_varieties.remove("green")
print(tea_varieties)

tea_varieties.insert(2, "lemon tea")
print(tea_varieties)

tea_varieties = ['black', 'green', 'lemon tea', 'white', 'oolong', 'herbal']
print(tea_varieties)

tea_varieties_copy = tea_varieties.copy()
print(tea_varieties_copy)


tea_varieties_copy.append("mint tea" )
print(tea_varieties_copy)


squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)

cube_numers = [x**3 for x in range(5)]
print(cube_numers)

