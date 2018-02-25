favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

names = ['jen', 'sarah', 'tiffany', 'nutcheer']

for name in favorite_languages.keys():
    if name in names:
        print(name+", thank you for your attending!")
    else:
        print(name+", I am glad to invite you to our survey.")
