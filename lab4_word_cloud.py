# LAB 4
# 07/12/20
# WORKING WITH DICTIONARIES

my_bikes = {
    "brand": "Kawasaki",
    "model": "Ninja",
    "year": 2020
}
print(my_bikes)

# GET() FUNCTION
m = my_bikes.get("model")
print(m)

# CHANGE DATA IN THE DICTIONARY
my_bikes["year"] = 2019
print(my_bikes)

# LISTS/PRINTS ALL THE KEYS
for bike in my_bikes:
    print(bike)

# LISTS/PRINTS ALL THE VALUES
for bike in my_bikes:
    print(my_bikes[bike])

# ANOTHER WAY OF THE DOING THE SAME AS ABOVE
for bike in my_bikes.values():
    print(bike)

# LISTS/PRINTS BOT THE KEYS AND VALUES WITHIN THE DICTIONARY
for key, value in my_bikes.items():
    print(key, value)

# CHECK IF A KEY EXISTS
if "model" in my_bikes:
    print("yes")

# CHECK IF A KEY EXISTS
if "cc" in my_bikes:
    print("It's her")
else:
    print("Nope, no CC in dictionary")

# CHECK NUMBER OF ITEMS IN DICTIONARY
print(len(my_bikes))