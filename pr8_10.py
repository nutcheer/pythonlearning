names = ['1', '2', '3']
name1 = []

def make_great(names):
    for name in names:
        name1.append("the Great " + name)
    return name1
def show_magicians(names):
    for name in names:
        print(name)             

show_magicians(make_great(names))   
