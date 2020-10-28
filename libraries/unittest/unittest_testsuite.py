import unittest


def sum(a, b):
    return a + b


class Module1Test(unittest.TestCase):
    def test_sum1(self):
        self.assertEqual(sum(1, 2), 3)

    def test_sum2(self):
        self.assertEqual(sum(1, -1), 0)


class Module2Test(unittest.TestCase):
    def setUp(self):
        self.bag = [True, True]

    def tearDown(self):
        del self.bag

    def test_true(self):
        for element in self.bag:
            self.assertTrue(element)


def make_suite(testcase, tests):
    return unittest.TestSuite(map(testcase, tests))


if __name__ == "__main__":
    suite1 = make_suite(Module1Test, ['test_sum1', 'test_sum2'])
    suite2 = make_suite(Module2Test, ['test_true'])

    allsuites = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(allsuites)
