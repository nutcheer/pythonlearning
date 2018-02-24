name_list = ['1','2','3']
print(name_list[0])
print(name_list[1])
print(name_list[2] + ", I am glad to invite you to our party.")
print("But " + name_list[1] + " can't arrive.")
name_list[1] = '4'
print(name_list[0])
print(name_list[1])
print(name_list[2] + ", I am glad to invite you to our party.")

print("I find a bigger table.")
name_list.insert(0, '5') 
name_list.insert(2, '6')
name_list.append('7')
print(name_list)

print("I am sorry that I can only eat with two people.")
name1 = name_list.pop()
name2 = name_list.pop()
name3 = name_list.pop()
name4 = name_list.pop()
print(name1 + " , I am sorry to tell you that you can't arrive.")
print(name2 + " , I am sorry to tell you that you can't arrive.")
print(name3 + " , I am sorry to tell you that you can't arrive.")
print(name4 + " , I am sorry to tell you that you can't arrive.")

print(name_list[0] +", "+ name_list[1] + ", I am glad to invite you to our party.")

del name_list[1]
del name_list[0]

print(name_list)