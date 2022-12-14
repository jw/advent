import re
import string
from collections import deque, namedtuple
from pathlib import Path


def get_nodes(line: str, max: int) -> list[str]:
    nodes = []
    spaces = 0
    for c in line:
        if c == " ":
            spaces = spaces + 1
        elif c in string.ascii_uppercase:
            nodes.append(c)
        else:
            spaces = 0
        if spaces == 4:
            nodes.append(None)
            spaces = 0
    while len(nodes) < max:
        nodes.append(None)
    return nodes


def get_lines(name: str) -> list[str]:
    input_file = Path(name)
    input_text = input_file.read_text()
    return input_text.split("\n")


def get_number(lines: list[str]) -> int:
    for line in lines:
        for c in line:
            if c in string.digits:
                return max([int(c) for c in line.split()])
    raise ValueError("No number file found.")


def get_stacks(lines: list[str], max: int) -> list[deque]:
    all_nodes = []
    for line in lines:
        if line == "":
            break
        all_nodes.append(get_nodes(line, max))

    print()
    for nodes in all_nodes:
        print(nodes)

    # convert the list of nodes to a list of deques after removing the Nones
    stack_lists = list(zip(*all_nodes))
    stacks = []
    for sl in stack_lists:
        stacks.append(deque([node for node in sl if node is not None]))

    return stacks


Rule = namedtuple("Rule", ["amount", "from_stack", "to_stack"])


def get_rule(line: str) -> Rule | None:
    p = re.compile(r"move (\d+) from (\d+) to (\d+)")
    m = p.match(line)
    if m:
        return Rule(int(m.group(1)), int(m.group(2)) - 1, int(m.group(3)) - 1)
    return None


def get_rules(lines: list[str]) -> list[Rule]:
    rules_and_nones = [get_rule(line) for line in lines]
    return [rule for rule in rules_and_nones if rule is not None]


def print_stack(stack: list[deque]) -> None:
    for i, d in enumerate(stack, start=0):
        print(f"{i}: {d}")


def process_1(stacks: list[deque], rules: list[Rule]) -> str:
    print()
    print_stack(stacks)
    for rule in rules:
        print(rule)
        for _ in range(rule.amount):
            element = stacks[rule.from_stack].popleft()
            stacks[rule.to_stack].appendleft(element)
        print_stack(stacks)
    result = ""
    for d in stacks:
        result = result + d.popleft()
    return result


def process_2(stacks: list[deque], rules: list[Rule]) -> str:
    print()
    print_stack(stacks)
    for rule in rules:
        print(rule)
        elements = []
        for _ in range(rule.amount):
            elements.append(stacks[rule.from_stack].popleft())
        print(f"{elements=}")
        elements.reverse()
        for i in range(rule.amount):
            stacks[rule.to_stack].appendleft(elements[i])

        print_stack(stacks)
    result = ""
    for d in stacks:
        result = result + d.popleft()
    return result


def main_one(name: str) -> str:
    lines = get_lines(name)
    max = get_number(lines)
    stacks = get_stacks(lines, max)
    rules = get_rules(lines)
    return process_1(stacks, rules)


def main_two(name: str) -> str:
    lines = get_lines(name)
    max = get_number(lines)
    stacks = get_stacks(lines, max)
    rules = get_rules(lines)
    return process_2(stacks, rules)


if __name__ == "__main__":
    print(main_two("input.txt"))
