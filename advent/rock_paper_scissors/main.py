from pathlib import Path

# A X Rock
# B Y Paper
# C Z Scissors

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6

SCORE_TABLE_ONE = {
    # loss
    # Rock < Scissors: A Z
    ("A", "Z"): SCISSORS + LOSS,
    # Paper < Rock: B X
    ("B", "X"): ROCK + LOSS,
    # Scissors < Paper: C Y
    ("C", "Y"): PAPER + LOSS,
    # draws
    # Rock = Rock: A X
    ("A", "X"): ROCK + DRAW,
    # Paper = paper: B Y
    ("B", "Y"): PAPER + DRAW,
    # Scissors = Scissors: C Z
    ("C", "Z"): SCISSORS + DRAW,
    # wins
    # Rock > Paper: A Y
    ("A", "Y"): PAPER + WIN,
    # Paper > Scissors: B Z
    ("B", "Z"): SCISSORS + WIN,
    # Scissors > Rock: C X
    ("C", "X"): ROCK + WIN,
}


# A X Rock
# B Y Paper
# C Z Scissors
# X Lose
# Y Draw
# Z Win

SCORE_TABLE_TWO = {
    # lose
    # Rock Lose: A Scissors
    ("A", "X"): SCISSORS + LOSS,
    # Paper Lose: B Rock
    ("B", "X"): ROCK + LOSS,
    # Scissors Lose: C Paper
    ("C", "X"): PAPER + LOSS,
    # draw
    # Rock Draw: A Rock
    ("A", "Y"): ROCK + DRAW,
    # Paper Draw: B Paper
    ("B", "Y"): PAPER + DRAW,
    # Scissors Draw: C Scissors
    ("C", "Y"): SCISSORS + DRAW,
    # wins
    # Rock Win: A Paper
    ("A", "Z"): PAPER + WIN,
    # Paper Win: B Scissors
    ("B", "Z"): SCISSORS + WIN,
    # Scissors Win: C Rock
    ("C", "Z"): ROCK + WIN,
}


def main_one(name: str) -> int:
    input_file = Path(name)
    input_text = input_file.read_text()
    score = 0
    for line in input_text.split("\n"):
        left, right = line.split()
        score += SCORE_TABLE_ONE[(left, right)]
    print(score)
    return score


def main_two(name: str) -> int:
    input_file = Path(name)
    input_text = input_file.read_text()
    score = 0
    for line in input_text.split("\n"):
        left, right = line.split()
        score += SCORE_TABLE_TWO[(left, right)]
    print(score)
    return score


if __name__ == "__main__":
    main_two("input.txt")
