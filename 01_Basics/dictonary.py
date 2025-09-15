chai_types  = {"Masala chai" : "Spicy", "Green chai" : "Herbal", "Lemon chai" : "Citrus",}
print(chai_types)

print(chai_types["Masala chai"])
print(chai_types["Green chai"])
print(chai_types["Lemon chai"])

print(("Masala chai") + " is " + chai_types["Masala chai"])

chai_types["lemon chai"] = "Spicy"
print(chai_types)

for chai in chai_types:
    print(chai)
    
for chai in chai_types:
    print(chai, chai_types[chai])
  
for key, values in chai_types.items():
    print(key, values)
    
if "Masala chai" in chai_types:
    print("Masala chai is available.")
else:
    print("Masala chai is not available.")    
    

chai_types["earl grey"] = "Citrus"
print(chai_types)

chai_types.pop("lemon chai")
print(chai_types)

chai_types.popitem()
print(chai_types)

del chai_types["Masala chai"]
print(chai_types)

chai_types_copy = chai_types.copy()
print(chai_types_copy)


tea_shops = {
    "chai": {"masla chia" : "spicy", "Ginger chai" : "Zesty", "Green chai" : "Herabal"},
    "tea" : {"Black tea" : "Bold", "Green Tea" : "Fresh", "White Tea" : "Delicate"},
}
print(tea_shops)

print(tea_shops["chai"])

squared_numbers = {x : x**2 for x in range(10)}
print(squared_numbers)

squared_numbers.clear()
print(squared_numbers)


keys = ["Masala Chai", "Green Chai", "Lemon Chai", "Ginger Chai", "Mint Chai"]
default_values = "Delicious"

new_dict = dict.fromkeys(keys, default_values)
print(new_dict)
