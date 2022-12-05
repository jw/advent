from pathlib import Path

import humanize


def main() -> None:
    input_file = Path("input.txt")
    input_text = input_file.read_text()
    elves = [0]
    index = 0
    for line in input_text.split("\n"):
        if line == "":
            index = index + 1
            elves.append(0)
        else:
            elves[index] += int(line)
    print(
        f"Found {len(elves)} elves with a total of {humanize.intcomma(sum(elves))} calories."
    )
    print(
        f"The elf with the highest number of calories has {humanize.intcomma(max(elves))} calories."
    )
    top_three = sorted(elves, reverse=True)[:3]
    top_three_humanized = [
        humanize.intcomma(c) for c in sorted(elves, reverse=True)[:3]
    ]
    print(
        f"The top three elves have this number of calories: {top_three_humanized}; "
        f"the sum is: {humanize.intcomma(sum(top_three))}."
    )


if __name__ == "__main__":
    main()
