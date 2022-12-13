import string
from pathlib import Path

LOWER = {c: i for i, c in enumerate(string.ascii_lowercase, start=1)}
HIGHER = {c: i for i, c in enumerate(string.ascii_uppercase, start=27)}
PRIORITIES = LOWER | HIGHER


def main_one(name: str) -> None:
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


def main_two(name: str) -> None:
    input_file = Path(name)
    input_text = input_file.read_text()
    total = 0
    lines = input_text.split("\n")
    for i, (one, two, three) in enumerate(
        [lines[i : i + 3] for i in range(0, len(lines), 3)]
    ):
        common = list(set(one) & set(two) & set(three))[0]
        priority = PRIORITIES[common]
        print(f"{i * 3:03}-{i * 3 + 2:03}: {common} -> {priority:02}.")
        total = total + priority
    print()
    print(f"{' ':>14}{total}")


if __name__ == "__main__":
    main_two("input.txt")
