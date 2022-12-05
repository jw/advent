import string
from pathlib import Path

LOWER = {c: i for i, c in enumerate(string.ascii_lowercase, start=1)}
HIGHER = {c: i for i, c in enumerate(string.ascii_uppercase, start=27)}
PRIORITIES = LOWER | HIGHER


def main(name: str):
    input_file = Path(name)
    input_text = input_file.read_text()
    total = 0
    for line in input_text.split("\n"):
        half = len(line) // 2
        left = line[:half]
        right = line[half:]
        common_list = list(set(left).intersection(right))
        assert len(common_list) <= 1, "Common is too large!"
        common = list(set(left).intersection(right))[0]
        print(f"{left:>25} vs {right:<25}: {common} = {PRIORITIES[common]:04d}")
        total = total + PRIORITIES[common]
    print()
    print(f"{' ':>25}    {' ':<25}      {total}")


if __name__ == '__main__':
    main("input.txt")
