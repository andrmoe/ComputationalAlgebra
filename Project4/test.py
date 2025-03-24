from random_squares import trial_division_factoring

def test_trial_division_factoring():
    factor_base = [2, 3, 5, 7, 11, 13]
    assert trial_division_factoring(5, factor_base) == [0, 0, 1, 0, 0, 0]
    assert trial_division_factoring(2*3**3*7, factor_base) == [1, 3, 0, 1, 0, 0]
    assert trial_division_factoring(7**100, factor_base) == [0, 0, 0, 100, 0, 0]
    assert trial_division_factoring(17, factor_base) == [0, 0, 0, 0, 0, 0]
