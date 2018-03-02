import unittest
from pr11_1 import function

class CCTestCase(unittest.TestCase):
	"""docstring for Test_city_country"""
	def test_city_country(self):
		formatted_cc = function('santiago', 'chile')
		self.assertEqual(formatted_cc, 'Santiago, Chile')

	def test_city_country_population(self):
		formatted_ccp = function('santiago', 'chile', '5000000')
		self.assertEqual(formatted_ccp, 'Santiago, Chile - population 5000000')

unittest.main()