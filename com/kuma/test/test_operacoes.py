import pytest

def soma(x,y):
  return x + y

def test_soma():
  assert soma([1,5]) == 6
