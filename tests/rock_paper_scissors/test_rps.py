from advent.rock_paper_scissors.main import main_one, main_two


def test_rpc_example_one():
    assert main_one("test_1.txt") == 15


def test_rpc_complete_one():
    assert main_one("test_2.txt") == 45


def test_rpc_example_two():
    assert main_two("test_1.txt") == 12


def test_rpc_complete_two():
    assert main_two("test_2.txt") == 33
