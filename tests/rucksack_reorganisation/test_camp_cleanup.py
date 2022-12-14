from advent.camp_cleanup.main import areas


def test_camp_cleanup_areas():
    assert areas("1-2") == {1, 2}
    assert areas("1-3") == {1, 2, 3}
    assert areas("1-5") == {1, 2, 3, 4, 5}
    assert areas("10-12") == {10, 11, 12}
    assert areas("1-1") == {1}
    assert areas("100-100") == {100}
