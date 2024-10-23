import sys

from collections import Counter


def find_consecutive_parts(pairs):
    if len(pairs) == 0:
        return []

    results = []
    n = len(pairs)

    prev = pairs[0][0] - 1
    start = 0

    for end in range(n):
        cur = pairs[end][0]

        if prev + 1 != cur:
            results.append((start, end))
            start = end

        prev = cur

    results.append((start, n))

    return results


def find_window_sum(counts, k, start, end):
    l = end - start
    if l <= k:
        return [sum(counts[start:end])]

    sums = []

    i = start
    s = sum(counts[i:i+k])
    sums.append(s)

    while i < end - k:
        s = s - counts[i] + counts[i+k]
        sums.append(s)
        i = i + 1

    return sums


def find_largest_sum_suboptimal(counts, k, start, end):
    sums = find_window_sum(counts, k, start, end)
    return max(sums)


def find_largest_sum(counts, k, start, end):
    l = end - start
    if l <= k:
        return sum(counts[start:end])

    i = start
    s = sum(counts[i:i+k])
    best_sum = s

    while i < end - k:
        s = s - counts[i] + counts[i+k]
        if s > best_sum:
            best_sum = s
        i = i + 1

    return best_sum


def solve_line(k, A):
    card_counts = Counter(A)
    card_counts = sorted(card_counts.items())

    consecutive_parts = find_consecutive_parts(card_counts)
    counts = [count for (k, count) in card_counts]

    max_sum = 0

    for start, end in consecutive_parts:
        current_best_sum = find_largest_sum(counts, k, start, end)
        if current_best_sum > max_sum:
            max_sum = current_best_sum

    return max_sum


def solve(input_source=sys.stdin):
    t = int(input_source.readline().strip())

    for _ in range(t):
        _, k = input_source.readline().strip().split()
        k = int(k)

        A = list(map(int, input_source.readline().split()))
        result = solve_line(k, A)
        print(result)
        
        

if __name__ == "__main__":
    solve()