class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nThe restaurant's name is " + self.name)
        print("The restaurant's cuisine type is " + self.cuisine + ".")
        print(str(self.number_served) + " customers have been served.")

    def open_restaurant(self):
        print(self.name + " is open for business!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self):
        self.number_served += 1


# my_restaurant = Restaurant("Papa Nitin's", "Indian")
# my_restaurant.set_number_served(7)
# my_restaurant.increment_number_served()
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# bappa_restaurant = Restaurant("Kochi Restaurant", "Oriental")
# bappa_restaurant.describe_restaurant()
# bappa_restaurant.open_restaurant()

# harris_restaurant = Restaurant("Harry's Halal", "Italian")
# harris_restaurant.describe_restaurant()
# harris_restaurant.open_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("\nAvailable flavors are:")
        for flavor in self.flavors:
            print("\t" + flavor.title())

nitin_ice_cream = IceCreamStand("Nitin's Ice Cream", "gelato", ["vanilla", "coconut", "cherry"])
nitin_ice_cream.describe_restaurant()
nitin_ice_cream.show_flavors()