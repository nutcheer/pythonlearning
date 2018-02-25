class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.ctype = cuisine_type
        
    def describe_restaurant(self):
        print(self.name)
        print(self.ctype)
        
    def open_restaurant(self):
        print("It is open now")
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["1", '2', '3']
        
    def describe_restaurant(self):
        for flavor in self.flavors:
            print(flavor)
        
icecream = IceCreamStand('nutcheer', 'nsks')
icecream.describe_restaurant()
