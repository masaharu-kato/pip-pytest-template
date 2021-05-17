"""
    Test of mypkg.mycalc
"""
import pytest
import mypkg.mycalc as myc
import mypkg.myexcalc as myec

@pytest.mark.parametrize(
    'a, b, res', [
    (1, 2, 3),
    (-3, 9, 6),
    ("0", 5, 5),
    (5, "0", 5),
    (" 10", "23", 33),
    ("-15", "5 ", -10),
])
def test_myadd(a, b, res):
    assert myc.myadd(a, b) == res


@pytest.mark.parametrize(
    'a, b, res', [
    (1, 2, 3),
    (-3, "nine", None),
    ("???", 5, None),
    ("piyo", "hoge", None),
    (" 10", "23", 33),
    ("-15", "5 ", -10),
])
def test_myexadd(a, b, res):
    assert myec.myexadd(a, b) == res
