from pathlib import Path


def areas(areas: str) -> set:
    left, right = areas.split("-")
    return set(range(int(left), int(right) + 1))


def main_one(name: str) -> int:
    input_file = Path(name)
    input_text = input_file.read_text()
    score = 0
    for line in input_text.split("\n"):
        left, right = line.split(",")
        left_areas = areas(left)
        right_areas = areas(left)
        print(f"{line}: {left_areas} vs {right_areas}")
    return score


def main_two(name: str) -> int:
    return 0


if __name__ == "__main__":
    main_one("input.txt")
