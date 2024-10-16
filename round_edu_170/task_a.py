# https://codeforces.com/contest/2025/problem/A

import sys


def solve_task(line_a, line_b):
    len_a = len(line_a)
    len_b = len(line_b)

    i = 0

    while True:
        if len_a == i or len_b == i:
            break
        if line_a[i] != line_b[i]:
            break
        i = i + 1

    if i == 0:
        return len_a + len_b
    else:
        return (len_a - i) + (len_b - i) + i + 1


def solve(input_source=sys.stdin):
    n = int(input_source.readline().strip())

    while n > 0:
        line_a = input_source.readline().strip()
        line_b = input_source.readline().strip()
        solution = solve_task(line_a, line_b)
        print(solution)
        n = n - 1


if __name__ == "__main__":
    solve()