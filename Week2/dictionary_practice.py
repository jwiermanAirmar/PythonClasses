# Python Class #2 on dictionaries
# https://www.w3schools.com/python/python_dictionaries.asp

# Dictionaries are a collection of key and value pairs that go together.
car = {"make": "Honda", "model": "Civic", "year": 2014, "color": "white"}

# You can give a dictionary a key, and it'll return its corresponding value.
print("The car's make is: " + car["make"])

# You can get a list keys of a dictionary with .keys()
car_dictionary_keys = car.keys()
print("Car dictionary keys are: " + str(car_dictionary_keys))

# You can also get a list of values of a dictionary with .values()
car_dictionary_values = car.values()
print("Car dictionary values are: " + str(car_dictionary_values))

# You can add a value by calling a new key in the dictionary, and setting it to a value.
car["doors"] = 4
print("Updated car dictionary: " + str(car))

# Keys are unique! So if you try to set something that already exists, it overwrites the previous value.
car["color"] = "blue"
print("Updated car color: " + str(car))

# Dictionaries are a great way to organize lots of data, because they can contain other dictionaries.
civic = {"type": "sedan", "drivetrain": "2wd", "doors": 4}
f150 = {"type": "truck", "drivetrain": "4wd", "doors": 2}

# Adding two dictionaries into a single dictionary.
vehicles = {"civic": civic, "f150": f150}

# To retrieve info about the f150 from our dictionary of vehicles, we just do this:
print("F150 information: " + str(vehicles["f150"]))

# For nested dictionaries, you can chain keys to dig down further:
print("F150 drivetrain is: " + vehicles["f150"]["drivetrain"])
