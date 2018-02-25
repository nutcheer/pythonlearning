car1 = "Audi"
car2 = "Audi "
if car1 == car2 and car1.lower() == car2:
    print("Yes")
else:
    print("No")

cars = ('Audi', 'subaru', 'BMW', 'toyota')
if car1.lower() in cars or car1 in cars:
    print("Yes")
else:
    print("No")
