# car = "subaru"
# print("Is car == 'subaru'? I predict True")
# print(car == "subaru")
# 
# print("\nIs car == 'audi'? I predict False")
# print(car == "audi")

# person = "Yukti"
# print(person == "yukti")
# print(person.lower() == "yukti")

# number_1 = 21
# number_2 = 18
# print(number_1 > 10)
# print(number_1 < 10)
# print(number_1 == 21 and number_1 > 18)

# pizzas = ["anchovies", "pizza", "fungus", "cheese", "laptop"]
# print("anchovies" in pizzas)
# print("anchovies" not in pizzas)

# alien_color = "green"

# if alien_color == "red":
# 	print("Red gets 3 points!")
# elif alien_color == "green":
# 	print("Green gets 2 points!")
# elif alien_color == "yellow":
# 	print ("Yellow gets 1 point!")

# age = 12

# if age < 2:
#     print("You're a baby")
# elif age < 4:
#     print("You're a toddler")
# elif age < 13:
#     print("You're just a kid, ha lame")
# elif age < 20:
#     print("You're a teenager")
# elif age < 65:
#     print("You're an old person")

fruits = ["mango", "lemon", "pear", "cashew apple"]
favorite_fruit = "papaya"
print("Is " + favorite_fruit + " on Nitin's list of approved fruits?")
for fruit in fruits:
    if fruit.lower() == favorite_fruit:
        print(favorite_fruit.title() + " is on the approved fruit list, awesome!")
if favorite_fruit not in fruits:
    print("Sorry, " + favorite_fruit + " is not on the fruit list.")