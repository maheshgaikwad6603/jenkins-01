from unittest import TestCase
import unittest

class TestTestDemoCalculator(TestCase):
    def test_addition_one(self):
        print('invalid addtion one')

    def test_two(self):
        print('two')

class TestTestDemoCalculator_two(TestCase):
    def test_addition_two(self):
        print('invalid addtion two')
class TestTestDemoCalculator_three(TestCase):
    def test_addition_three(self):
        print('invalid addtion three')
class TestTestDemoCalculator_foue(TestCase):
   def test_addition_foue(self):
        print('invalid four')
class TestTestDemoCalculator_five(TestCase):
  def test_addition_five(self):
        print('invalid addtion five')


if __name__ == '__main__':
    unittest.main()
