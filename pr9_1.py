class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.ctype = cuisine_type
        
    def describe_restaurant(self):
        print(self.name)
        print(self.ctype)
        
    def open_restaurant(self):
        print("It is open now")
        
restaurant = Restaurant("name", "ctype")
restaurant.describe_restaurant()
restaurant.open_restaurant()
