class Restaurant():
    """Type of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Information"""
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restairant(self):
        """"Open hours"""
        print("Restaurant " + self.restaurant_name + " has open at: 6-22")

restaurant1 = Restaurant("Goracy Piec", "Pizzeria")
restaurant2 = Restaurant("Placek babuni", "Plackarnia")
restaurant3 = Restaurant("Pierożek", "Bar Mleczny")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#restaurant.open_restairant()