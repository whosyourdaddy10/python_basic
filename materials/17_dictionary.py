# 25. Dictionary = Collection of key-value pairs

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# print(person["name"])

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome"
}

print(capitals["France"])
# or
print(capitals.get("France"))

# get keys
# print(capitals.keys())

# get values
# print(capitals.values())

# add item to dictionary
# capitals.update({"Spain": "Madrid"})

# remove item from dictionary
# capitals.pop("Germany")

# loop through dictionary
# for key, value in capitals.items():
#     print(key, value)

# loop through keys
# for key in capitals.keys():
#     print(key)



