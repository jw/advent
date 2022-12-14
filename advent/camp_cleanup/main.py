from pathlib import Path


def areas(areas: str) -> set:
    left, right = areas.split("-")
    return set(range(int(left), int(right) + 1))


def print_range(area: set) -> str:
    sorted_area = sorted(area)
    return f"{sorted_area[0]:02}-{sorted_area[-1]:02}"


def main_one(name: str) -> int:
    input_file = Path(name)
    input_text = input_file.read_text()
    wrapped = 0
    for line in input_text.split("\n"):
        left, right = line.split(",")
        left_areas = areas(left)
        right_areas = areas(right)
        updated = False
        if left_areas - right_areas == set() or right_areas - left_areas == set():
            updated = True
            wrapped = wrapped + 1
        print(f"{print_range(left_areas)} vs {print_range(right_areas)}: {wrapped} {'+' if updated else '-'}")
    print(f"{' ':15} {wrapped}")
    return wrapped


def main_two(name: str) -> int:
    input_file = Path(name)
    input_text = input_file.read_text()
    overlap = 0
    for line in input_text.split("\n"):
        left, right = line.split(",")
        left_areas = areas(left)
        right_areas = areas(right)
        updated = False
        if left_areas & right_areas != set():
            updated = True
            overlap = overlap + 1
        print(f"{print_range(left_areas)} vs {print_range(right_areas)}: {overlap} {'+' if updated else '-'}")
    print(f"{' ':15} {overlap}")
    return overlap


if __name__ == "__main__":
    main_two("input.txt")
