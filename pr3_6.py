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
