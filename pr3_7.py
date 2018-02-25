names = ['one','two','three']
message = ", I'm glad to invite you to my party."
print(names[0]+message)
print(names[1]+message)
print(names[2]+message)
print("I am sorry to hear that "+names[0]+" can not come to join us.")
names[0] = 'four'
print(names[0]+message)
print(names[1]+message)
print(names[2]+message)

print("I think that I find a bigger table for dinner!")
names.insert(0,"five")
names.insert(3,"six")
names.append("seven")
print(names[0]+message)
print(names[1]+message)
print(names[2]+message)
print(names[3]+message)
print(names[4]+message)
print(names[5]+message)
print("I am sorry that my new table can not reach at time.")
print("So I can only choose two guests.")

print(names.pop()+", I am sorry to tell you that you may not join our party.")
print(names.pop()+", I am sorry to tell you that you may not join our party.")
print(names.pop()+", I am sorry to tell you that you may not join our party.")
print(names.pop()+", I am sorry to tell you that you may not join our party.")
print(names[0] + ", You can still join the party!")
print(names[1] + ", You can still join the party!")
del names[1]
del names[0]
print(names)
