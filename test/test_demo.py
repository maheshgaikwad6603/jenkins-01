
# import unittest
#
# def add(x,y):
#     return  x + y
#
# class SimpleTest(unittest.TestCase):
#     def testadd1(self):
#         self.assertEqual(add(4,5),9)
#
# class additon(unittest.TestCase):
#     def addtion_no(self):
#         print("addition of two no")
#
# if __name__=='__main__':
#     unittest.main()

import unittest

def add_numbers(x, y):
    return x + y
def sub_numbers(x, y):
    return x - y


class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-1, 1), 0)
        print("test add number")
class TestSubNumbers(unittest.TestCase):
    def test_sub_numbers(self):
        self.assertEqual(sub_numbers(8, 3), 5)
        self.assertEqual(sub_numbers(3, 2), 1)
        self.assertEqual(sub_numbers(5, 4), 1)
        print("test sub numbers")


if __name__ == '__main__':
    unittest.main()
