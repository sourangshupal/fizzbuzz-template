import unittest
from io import StringIO
import sys
from main import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def _capture(self, n):
        buf = StringIO()
        sys.stdout = buf
        fizzbuzz(n)
        sys.stdout = sys.__stdout__
        return buf.getvalue().strip().split("\n")

    def test_fizz(self):
        out = self._capture(3)
        self.assertEqual(out[2], "Fizz")

    def test_buzz(self):
        out = self._capture(5)
        self.assertEqual(out[4], "Buzz")

    def test_fizzbuzz(self):
        out = self._capture(15)
        self.assertEqual(out[14], "FizzBuzz")

    def test_number(self):
        out = self._capture(1)
        self.assertEqual(out[0], "1")

    def test_length(self):
        out = self._capture(10)
        self.assertEqual(len(out), 10)

if __name__ == "__main__":
    unittest.main()
