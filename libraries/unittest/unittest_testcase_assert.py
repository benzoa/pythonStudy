import unittest_my_math as mymath
import unittest

class TestNGLE(unittest.TestCase):
	def test_add_integers(self):
		result = mymath.add(1, 2)
		
		self.assertEqual(result, 3)
		self.assertNotEqual(result, 5)

	def test_add_strings(self):
		result = mymath.add('My life suddenly took ', 'a turn for the better.')
		
		self.assertIn('turn for', result)
		self.assertNotIn('tongchun', result)

	def test_compare_integers(self):
		retult = mymath.compare(10, 10)

		self.assertTrue(retult)

	def test_compare_strings(self):
		retult = mymath.compare('ngle', 'tongchun')

		self.assertFalse(retult)

	def test_multiply(self):
		result = mymath.multiply(10, 2)

		self.assertGreater(result, 10)

	def test_subtract(self):
		result = mymath.subtract(5, 5)

		self.assertGreaterEqual(result, -3)

	def test_divide(self):
		result = mymath.divide(3, 9)

		self.assertLess(result, 6)

	def test_involution(self):
		result = mymath.involution(3, 3)

		self.assertLessEqual(result, 81)


if __name__ == '__main__':
	unittest.main()
