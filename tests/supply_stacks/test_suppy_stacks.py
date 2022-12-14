from advent.supply_stacks.main import (
    Rule,
    get_lines,
    get_nodes,
    get_number,
    get_rule,
    get_rules,
    get_stacks,
    print_stack,
    process_1,
    process_2,
)


def test_get_nodes():
    assert get_nodes("", 0) == []
    assert get_nodes("", 1) == [None]
    assert get_nodes("", 2) == [None, None]
    assert get_nodes("[A]", 1) == ["A"]
    assert get_nodes("[A] [B]", 3) == ["A", "B", None]
    assert get_nodes("[A] [B] [C]", 3) == ["A", "B", "C"]
    assert get_nodes("[A]     [C]", 3) == ["A", None, "C"]
    assert get_nodes("[A]     [C]         [F]", 6) == ["A", None, "C", None, None, "F"]
    assert get_nodes("        [C]", 3) == [None, None, "C"]
    assert get_nodes("        [C]         [F]", 6) == [None, None, "C", None, None, "F"]
    assert get_nodes("[A]", 2) == ["A", None]
    assert get_nodes("        [C]         [F]", 10) == [
        None,
        None,
        "C",
        None,
        None,
        "F",
        None,
        None,
        None,
        None,
    ]


def test_get_lines():
    assert len(get_lines("test_1.txt")) == 9
    assert len(get_lines("test_2.txt")) == 10


def test_get_numbers():
    assert get_number(get_lines("test_1.txt")) == 3
    assert get_number(get_lines("test_2.txt")) == 4


def test_get_stacks():
    lines = get_lines("test_1.txt")
    stacks = get_stacks(lines, get_number(lines))
    assert len(stacks) == 3
    assert len(stacks[1]) == 3
    lines = get_lines("test_2.txt")
    stacks = get_stacks(lines, get_number(lines))
    print_stack(stacks)


def test_get_rule():
    assert get_rule("") is None
    assert get_rule("move 5") is None
    assert get_rule("move 10 from 20 to 30") == Rule(10, 19, 29)
    assert get_rule("[A] [B]") is None
    assert get_rule("[A]     [C]") is None


def test_get_rules():
    lines = get_lines("test_1.txt")
    rules = get_rules(lines)
    assert len(rules) == 4
    assert rules[0] == Rule(1, 1, 0)


def test_process_1():
    lines = get_lines("test_1.txt")
    stack = get_stacks(lines, get_number(lines))
    rules = get_rules(lines)
    assert process_1(stack, rules) == "CMZ"


def test_process_2():
    lines = get_lines("test_1.txt")
    stack = get_stacks(lines, get_number(lines))
    rules = get_rules(lines)
    assert process_2(stack, rules) == "MCD"
