import unittest
from sample_lib import test_function

class TestSampleLib(unittest.TestCase):

    def test_function(self):
        self.assertEqual(test_function(True), 3)
        self.assertEqual(test_function(False), 2)

if __name__ == '__main__':
    unittest.main()