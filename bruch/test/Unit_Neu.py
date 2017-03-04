"""
Created on 04.03.2017

@author: Daniel May
"""
import unittest

from bruch.Bruch import *


class TestNeu(unittest.TestCase):
    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def test_makeBruchCopy(self):
        num = 3
        denom = 4
        b4 = Bruch(num, denom)
        b5 = Bruch._Bruch__makeBruch(b4)
        assert (b4 == b5)

    def testNegInt(self):
        value = -5
        b4 = Bruch(value)
        assert (-b4 == -value)

    def teststrInt(self):
        b4 = Bruch(-5)
        str1 = "(-5)"
        assert (str(b4) == str1)

    def testraddInt(self):
        val1 = 3
        val2 = -3
        b4 = val1 + Bruch(val2)
        assert (b4 == val1 + val2)

    def testTupleInt(self):
        z, n = Bruch(5)
        assert (z == 5 and n == 1)


if __name__ == "__main__":
    unittest.main()
