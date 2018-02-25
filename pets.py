pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

def describe_pet(pet_name, animal_type = 'dog' ):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet( 'willie', 'dog')
describe_pet('willie')
