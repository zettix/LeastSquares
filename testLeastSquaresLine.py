import LeastSquaresLine


import pytest


def test_one():
   with pytest.raises(Exception):
    LeastSquaresLine.FindLine([[1, 1]])

def test_two():
  m, b = LeastSquaresLine.FindLine([[0,0], [1, 1]])
  assert m == 1
  assert b == 0

def test_two_offset():
  m, b = LeastSquaresLine.FindLine([[1,10], [2, 11]])
  assert m == 1
  assert b == 9

def test_three():
  m, b = LeastSquaresLine.FindLine([[-1, 1], [0,0], [1, 1]])
  assert m == 0
  assert b == 2/3
