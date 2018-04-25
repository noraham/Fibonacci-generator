"""ReadMe: Written in Python 2, running version 2.7.12
Usage: to run tests, uncomment lines 49-51 and run the file as usual
"""
from unittest import TestCase

Fibo_Seq= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def fibo(n):
    """Returns i-th (count starts at 0) num of the Fibonnaci Sequence.
       ith Fibo value is defined as the sum of the 2 numbers before it,
       = (i - 1) + (i - 2)
       so to find the nth element, continue to call fibo on i-1 and i-2nd terms
       until we get to base case, then add all adjacent terms to get to ith"""

    if n <= 1: # base case = 0 or 1, which is as low as we can go with Fibo Seq
        return n # recurse until bottom, add on the way back up
    else:
        return(fibo(n - 1) + fibo(n - 2))
    """heads up: recursive solution doesn't work for a number as big as 100, freezes script"""


def fibo_odd(n):
    """Returns n-th (count starts at 1) odd number of the Fibonacci Sequence.
       0 is considered even.
       pseudocode: fibo seq is even-odd-odd repeating. convert n-th odd into
       i-th from regular Fibo Seq then running that through fibo funct.
       Remember that in Python 2 division of ints is floor math."""

    return fibo(n + ((n - 1)/2))

def fibo_odd_version2(lst):
    """Given starting array, return 100th odd Fibonacci Number"""

    count = 1
    while count < 100:
        next_fib = lst[-1] + lst[-2]
        if next_fib % 2 == 1:
            count += 1
        lst.append(next_fib)
    return lst[-1]

def fibo_odd_version3(n):
    """Modified version2 so that starting array (Fibonacci Sequence) is consistent
       and user can specify which odd Fibo Num they want (not hard-coded)"""

    fib = [0, 1]
    count = 1
    
    if n <= count:
        return n # fail fast

    while count < n:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
        if next_fib % 2 == 1:
            count += 1

    return fib[-1]


class UnitTests(TestCase):
    """Tests the functions in this file"""

    def test_fibo(self):

        test = fibo(8)
        control = Fibo_Seq[8]
        assert test == control

        test = fibo(0)
        control = Fibo_Seq[0]
        assert test == control

    # def test_fibo_odd(self
        """heads up: recursive solution doesn't work for a number as big as 100, freezes script"""
    #     test = fibo_odd(100)
    #     assert test == 6161314747715278029583501626149

    def test_fibo_odd_version2(self):

        test = fibo_odd_version2([0, 1])
        assert test == 6161314747715278029583501626149

    def test_fibo_odd_version3(self):

        test = fibo_odd_version3(100)
        assert test == 6161314747715278029583501626149

if __name__ == "__main__":
    import unittest
    unittest.main()