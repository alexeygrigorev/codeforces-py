from round_edu_170.task_c import find_consecutive_parts, solve_line
from round_edu_170.task_c import find_window_sum

def test_find_consecutive_parts_one():
    numbers = [1]
    pairs = [(n, 1) for n in numbers]
    
    actual = find_consecutive_parts(pairs)

    expected = [(0, 1)]

    assert actual == expected


def test_find_consecutive_parts_two():
    numbers = [1, 2, 3, 5, 6, 7]
    pairs = [(n, 1) for n in numbers]
    
    actual = find_consecutive_parts(pairs)

    expected = [(0, 3), (3, 6)]

    assert actual == expected



def test_find_consecutive_parts():
    numbers = [1, 3, 4, 5, 7, 8, 10]
    pairs = [(n, 1) for n in numbers]
    
    actual = find_consecutive_parts(pairs)

    expected = [(0, 1), (1, 4), (4, 6), (6, 7)]

    assert actual == expected


def test_find_window_sum_1():
    counts = [0, 1, 2, 3, 4, 5, 6, 7]
    actual = find_window_sum(counts, 3, 0, 8)
    expected = [3, 6, 9, 12, 15, 18]

    assert actual == expected


def test_find_window_sum_2():
    counts = [0, 1, 2, 3, 4, 5, 6, 7]

    actual = find_window_sum(counts, 3, 1, 8)
    expected = [6, 9, 12, 15, 18]
    assert actual == expected

    actual = find_window_sum(counts, 3, 1, 7)
    expected = [6, 9, 12, 15]
    assert actual == expected

    actual = find_window_sum(counts, 3, 3, 7)
    expected = [12, 15]
    assert actual == expected


def test_window_sum_3():
    counts = [2, 1]
    actual = find_window_sum(counts, 2, 0, 1)
    expected = [2]
    assert actual == expected

    actual = find_window_sum(counts, 2, 1, 2)
    expected = [1]
    assert actual == expected


def test_solve_1():
    k = 2
    A = [5, 2, 4, 3, 4, 3, 4, 5, 3, 2]

    result = solve_line(k, A)
    assert result == 6


def test_solve_3():
    k = 3
    A = [4, 5, 4, 4, 6, 5, 4, 4, 6]
    result = solve_line(k, A)
    assert result == 9

def test_solve_4():
    k = 2
    A = [1, 3, 1]

    result = solve_line(k, A)
    assert result == 2