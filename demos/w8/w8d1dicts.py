#w8d1 - intro to dictionaries

#dictionaries are collections similar to arrays in javascript


#--CODE--
myCar = {
    "make": "Ford",
    "model": "Focus SE Hatchback",
    "year": 2014,
    "name": "Gwendoline",
    "color": "black"
}

print(myCar)

print(f"My car is a {myCar['color']} {myCar['year']} {myCar['make']} {myCar['model']} named {myCar['name']}.")
print(f"----------------------------------------------------------------------------------------------------")

yourCar = {
    "make": "Ford",
    "model": "F-150",
    "year": 2024,
    "name": "Gandalf",
    "color": "black",
    "friends": ["Tyler", "Tony", "Steve"]
}

print(yourCar)

print(f"My car is a {yourCar['color']} {yourCar['year']} {yourCar['make']} {yourCar['model']} named {yourCar['name']}.")
print(f"----------------------------------------------------------------------------------------------------")

#different methods of updating dicts without typing a new definition inside the dict
yourCar['plate'] = "12345"
yourCar.update({"wheels": "4"})

for key in yourCar:
    print(f"{key.upper():10}\t{yourCar[key]}")