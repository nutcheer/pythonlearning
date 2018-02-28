from random import randint

class Die():
	"""docstring for Die"""
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		print(str(randint(1, int(self.sides))))
# sides = 6
die6 = Die()
for x in range(1, 11):
	die6.roll_die()
# sides = 10
die10 = Die(10)
for x in range(1,11):
	die10.roll_die()
# sides = 20
die20 =Die(20)
for x in range(1,11):
	die20.roll_die()