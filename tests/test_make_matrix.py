import pytest
from make_matrix import *


def test_make_constant_matrix():
    assert make_constant_matrix(2, 2, 0) == [[0, 0], [0, 0]]


def test_random_matrix():
    matrix = random_matrix(2, 3)
    assert len(matrix) == 2
    assert len(matrix[0]) == 3
