import unittest
from utils import Utils

class UtilsTest(unittest.TestCase):

    def test_reversed_integer(self):
        self.assertEqual(Utils.reversed(6789), 9876)
        self.assertEqual(Utils.reversed(-4321), -1234)
        self.assertEqual(Utils.reversed(0), 0)
    

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            Utils.reversed("1234")
        with self.assertRaises(TypeError):
            Utils.reversed("-4321")

    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            Utils.reversed(123.4)
        with self.assertRaises(TypeError):
            Utils.reversed(-123.4)

    def test_formatter_integer(self):
        self.assertEqual(Utils.formatter(12345), {"binary": "11000000111001", "octal": "30071"})
        self.assertEqual(Utils.formatter(-54321), {"binary": "-1101010001110001", "octal": "-152361"})

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            Utils.formatter("6789")
        with self.assertRaises(TypeError):
            Utils.formatter("-9876")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            Utils.formatter(678.99)
        with self.assertRaises(TypeError):
            Utils.formatter(-678.99)

if __name__ == '__main__':
    unittest.main()
