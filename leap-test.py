
import unittest
from leapYear import findLeap

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(findLeap(2020), True)
        self.assertEqual(findLeap(2019), False)
        
if __name__ == '__main__':
    unittest.main()
