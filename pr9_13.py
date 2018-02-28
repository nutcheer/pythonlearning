from collections import OrderedDict
# practice6.4
my_python = {
    'print': 'print something on your screen',
    'add': 'add something to your list',
    'remove': 'remove your value from your list',
    'append': 'add something to the end of your list',
    'lower': 'change your string into lower',
}
for function, value in my_python.items():
    print(function+":"+value)

# practice9.13
my_python = OrderedDict()

my_python['print'] = 'print something on your screen'
my_python['add'] = 'add something to your list'
my_python['remove'] = 'remove your value from your list'
my_python['append'] = 'add something to the end of your list'
my_python['lower'] = 'change your string into lower'

for function,value in my_python.items():
	print(function + ": " + value)
	