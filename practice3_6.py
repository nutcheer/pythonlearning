name_list = ['1','2','3']
print(name_list[0])
print(name_list[1])
print(name_list[2] + ", I am glad to invite you to our party.")
print("But " + name_list[1] + " can't arrive.")
name_list[1] = '4'
print(name_list[0])
print(name_list[1])
print(name_list[2] + ", I am glad to invite you to our party.")

print("Sorry, I find a bigger table.")
name_list.insert(0, '5') 
name_list.insert(2, '6')
name_list.append('7')
print(name_list)
