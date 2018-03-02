import unittest
from pr11_3 import Employee

class EmployeeTestCase(unittest.TestCase):
	def setUp(self):
		self.salary = 100000
		self.employee = Employee('Albert', 'Einstein', self.salary)

	def test_give_default_raise(self):
		self.salary += int(self.employee.give_raise())
		self.assertEqual(self.salary, 105000)
		self.salary = 100000

	def test_give_custom_raise(self):
		self.salary += self.employee.give_raise(50000)
		self.assertEqual(self.salary, 150000)
		self.salary = 100000

unittest.main()