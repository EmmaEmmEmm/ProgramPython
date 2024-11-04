import unittest
#import coverage
import mybmi
class TestBMI(unittest.TestCase):
    def test_computeBMIOK(self):
        self.assertEqual(mybmi.computeBMI(52, 1.55), 21.64)