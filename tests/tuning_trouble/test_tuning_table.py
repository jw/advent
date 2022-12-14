from advent.tuning_trouble.main import start_of_packet


def test_start_of_packet():
    assert start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert start_of_packet("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

    assert start_of_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert start_of_packet("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
