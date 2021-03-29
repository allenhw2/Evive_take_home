import unittest
from unittest.mock import patch, call

from io import StringIO

class TestMenu(unittest.TestCase):

    def foo(inStr):
        print ("hi"+inStr)

    def test_foo():
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        foo('test')                                   # Call unchanged function.
        sys.stdout = sys.__stdout__                   # Reset redirect.
        print ('Captured', capturedOutput.getvalue())   # Now works as before.

if __name__ == '__main__':
    unittest.main()