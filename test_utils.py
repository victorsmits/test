# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
      self.assertEqual(fact(3),6)    
      self.assertEqual(fact(2),1)
      pass
    def test_roots(self):
        self.assertEqual(roots(1,0,1),result(x1="", x2=""))
        self.assertEqual(roots(2,2,2),)
        # À compléter...
        pass
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
