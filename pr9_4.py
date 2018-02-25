class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.ctype = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(self.name)
        print(self.ctype)
        print(self.number_served)
        
    def open_restaurant(self):
        print("It is open now")
        
    def set_number_served(self, number):
        self.number_served = int(number)
                
restaurant = Restaurant("name", "ctype")
restaurant.set_number_served(25)
restaurant.describe_restaurant()
restaurant.open_restaurant()
