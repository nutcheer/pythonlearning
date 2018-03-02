class Employee():
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = int(salary)

	def give_raise(self, raise_salary=5000):
		return raise_salary