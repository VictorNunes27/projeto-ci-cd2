import pytest
from math_utils import add, subtract,multiply

def test_add():
 assert add(2, 3) == 5
 assert add(5, 5) == 10

def test_subtract():
 assert subtract(5, 2) == 3
 assert subtract(1, 1) == 0

def teste_multiply():
  assert multiply(4,3) == 12
  assert multiply(2,3) == 6

def test_multiply_invalid_type():

 try:
   multiply("a", 3)
 except ValueError:
   assert True
