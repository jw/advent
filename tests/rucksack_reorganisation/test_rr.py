from advent.rucksack_reorganisation.main import main


def test_rr_example():
    assert main("test.txt") == 157
