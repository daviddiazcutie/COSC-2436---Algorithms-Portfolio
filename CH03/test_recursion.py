"""Lab 03: Test Cases for Recursion"""
import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from recursion import fact, recursive_sum, recursive_count, recursive_max


class TestFactorial:
    def test_fact_1(self):
        assert fact(1) == 1
    
    def test_fact_5(self):
        assert fact(5) == 120
    
    def test_fact_3(self):
        assert fact(3) == 6


class TestRecursiveSum:
    def test_sum_basic(self):
        assert recursive_sum([2, 4, 6]) == 12
    
    def test_sum_empty(self):
        assert recursive_sum([]) == 0
    
    def test_sum_single(self):
        assert recursive_sum([42]) == 42


class TestRecursiveCount:
    def test_count_basic(self):
        assert recursive_count([1, 2, 3, 4, 5]) == 5
    
    def test_count_empty(self):
        assert recursive_count([]) == 0


class TestRecursiveMax:
    def test_max_basic(self):
        assert recursive_max([3, 7, 2, 9, 1]) == 9
    
    def test_max_single(self):
        assert recursive_max([42]) == 42
    
    def test_max_first(self):
        assert recursive_max([99, 1, 2, 3]) == 99


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
