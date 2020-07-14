import unittest


def sum(a, b):
    return a + b

class ModuleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')   
    
    def setUp(self):
        self.bag = [True, True]

    def tearDown(self):
        del self.bag

    def test_true(self):
        for element in self.bag:
            self.assertTrue(element)
    
    def testSum1(self):
        self.assertEqual(sum(1, 2), 3)
    
    def testSum2(self):
        self.assertEqual(sum(1, -1), 0)


if __name__ == "__main__":
    unittest.main()
