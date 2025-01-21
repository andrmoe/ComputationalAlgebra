from assignment1 import extended_euclidean

def test_extended_euclidean():
    n, m = extended_euclidean(150, 70)
    assert n*150 + m*70 == 10