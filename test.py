from assignment1 import add, sub, mul, extended_euclidean, inverse, exponentiate


def test_add():
    assert add(5,8, 11) == 2

def test_sub():
    assert sub(5,8, 11) == 8

def test_mul():
    assert mul(5,8, 11) == 7


def test_extended_euclidean():
    n, m = extended_euclidean(150, 70)
    assert n*150 + m*70 == 10

def test_inverse():
    assert inverse(3, 17) == 6

def test_exponentiate():
    assert exponentiate(4, 3, 11) == 4

def test_negative_exponentiate():
    assert exponentiate(-4, 3, 11) == 3