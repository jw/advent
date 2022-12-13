from advent.rucksack_reorganisation.main import main_one


def test_rr_example():
    assert main_one("test.txt") == 157
