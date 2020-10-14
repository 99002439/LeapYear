
import unittest
from leapYear import leapYear

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(leapYear(2020), False)
        self.assertEqual(leapYear(2019), False)
        
if __name__ == '__main__':
    unittest.main()
